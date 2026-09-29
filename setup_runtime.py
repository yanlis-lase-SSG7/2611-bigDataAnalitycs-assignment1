"""Bootstrap the project-local Windows x64 runtime; never run the analysis pipeline."""
import argparse
import base64
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import zipfile

JAVA_VERSION = "17.0.20.1"
JAVA_FOLDER = "jdk-17.0.20.1+1"
JAVA_URL = "https://aka.ms/download-jdk/microsoft-jdk-17.0.20.1-windows-x64.zip"
JAVA_SHA256 = "3d9006956fc8af5601cd24ffc4f468bef48279c7ebd8171b9bdf90d0aabfbf1f"
SPARK_VERSION = "4.0.4"
HELPER_COMMIT = "7386986d5d8a079b5cd4464f4599766dd27e7d13"
HELPERS = {
    "winutils.exe": "496a591eb1e67df2a620f710d529ba6ddfe1c19149e6647cc4e320bb0efd8553",
    "hadoop.dll": "d7ab36a68518748cef142be2da5069b4c763c2cd764c1d2e6ac48c7200405be3",
}


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def download(url, target, expected):
    if target.is_file():
        if sha256(target) == expected:
            print(f"Verified cache: {target.name}", flush=True)
            return
        raise RuntimeError(f"Checksum mismatch in cache: {target}. Move it aside before retrying.")
    print(f"Downloading {target.name} ...", flush=True)
    request = urllib.request.Request(url, headers={"User-Agent": "BDA-runtime-setup/1"})
    # Only this script's new temporary file is removed on failure.
    with tempfile.NamedTemporaryFile(dir=target.parent, suffix=".part", delete=False) as stream:
        partial = Path(stream.name)
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                if not response.url.startswith("https://"):
                    raise RuntimeError("Download redirected away from HTTPS")
                shutil.copyfileobj(response, stream)
            stream.close()
            if sha256(partial) != expected:
                raise RuntimeError(f"Downloaded checksum mismatch: {target.name}; installation stopped")
            partial.rename(target)
        finally:
            stream.close()
            if partial.exists():
                partial.unlink()


def publish_directory(source, target):
    """Reuse matching existing files; refuse to replace conflicting local work."""
    if target.exists():
        for item in source.rglob("*"):
            if item.is_file():
                current = target / item.relative_to(source)
                if not current.is_file() or sha256(current) != sha256(item):
                    raise RuntimeError(
                        f"Existing runtime differs at {current}. Preserve/rename {target} "
                        "and rerun setup; no existing file has been replaced."
                    )
        print(f"Reusing verified runtime: {target.name}", flush=True)
    else:
        # Copy rather than rename: Windows can temporarily lock extracted Java folders.
        shutil.copytree(source, target)


def prepare_java(runtime, staging):
    cache = runtime / "downloads"
    cache.mkdir(exist_ok=True)
    archive = cache / "microsoft-jdk-17.0.20.1-windows-x64.zip"
    download(JAVA_URL, archive, JAVA_SHA256)
    java_stage = staging / "java"
    java_stage.mkdir()
    with zipfile.ZipFile(archive) as package:
        for member in package.infolist():
            output = (java_stage / member.filename).resolve()
            if not output.is_relative_to(java_stage.resolve()):
                raise RuntimeError("Unsafe Java archive path")
        package.extractall(java_stage)
    extracted = java_stage / JAVA_FOLDER
    if not (extracted / "bin/java.exe").is_file():
        raise RuntimeError("Java archive layout does not match the pinned version")
    publish_directory(extracted, runtime / JAVA_FOLDER)


def prepare_helpers(runtime, staging):
    hadoop = staging / "hadoop"
    (hadoop / "bin").mkdir(parents=True)
    sources = {}
    for name, checksum in HELPERS.items():
        url = f"https://raw.githubusercontent.com/cdarlint/winutils/{HELPER_COMMIT}/hadoop-3.3.6/bin/{name}"
        existing = runtime / "hadoop/bin" / name
        target = hadoop / "bin" / name
        if existing.is_file() and sha256(existing) == checksum:
            shutil.copy2(existing, target)
        else:
            download(url, target, checksum)
        sources[name] = {"source": url, "sha256": checksum}
    # Existing sources.json is historical metadata, so do not replace it.
    publish_directory(hadoop, runtime / "hadoop")
    return sources


def prepare_spark(runtime, staging):
    distribution = importlib.metadata.distribution("pyspark")
    if distribution.version != SPARK_VERSION:
        raise RuntimeError(f"PySpark {SPARK_VERSION} required; install requirements.txt first")
    spark = staging / "spark-home"
    count = {"bin": 0, "jars": 0}
    for member in distribution.files or []:
        parts = member.parts
        if len(parts) < 3 or parts[0] != "pyspark" or parts[1] not in count:
            continue
        source = Path(distribution.locate_file(member))
        if not source.is_file():
            raise RuntimeError(f"Missing installed PySpark file: {member}")
        if not member.hash or member.hash.mode != "sha256":
            raise RuntimeError(f"Missing SHA-256 package RECORD entry: {member}")
        checksum = base64.urlsafe_b64encode(bytes.fromhex(sha256(source))).decode().rstrip("=")
        if checksum != member.hash.value:
            raise RuntimeError(f"Installed PySpark checksum mismatch: {member}")
        destination = spark.joinpath(*parts[1:])
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        count[parts[1]] += 1
    if not all(count.values()):
        raise RuntimeError("PySpark package does not contain bin and jars")
    launcher = spark / "bin/spark-class2.cmd"
    text = launcher.read_text(encoding="utf-8")
    old = 'for /f "tokens=*" %%i in (%LAUNCHER_OUTPUT%) do ('
    new = 'for /f "usebackq tokens=*" %%i in ("%LAUNCHER_OUTPUT%") do ('
    if old not in text:
        raise RuntimeError("Unexpected Spark launcher; refusing an unverified patch")
    text = (text.replace(old, new)
            .replace('> %LAUNCHER_OUTPUT%', '> "%LAUNCHER_OUTPUT%"')
            .replace('del %LAUNCHER_OUTPUT%', 'del "%LAUNCHER_OUTPUT%"'))
    launcher.write_text(text, encoding="utf-8", newline="\r\n")
    publish_directory(spark, runtime / "spark-home")


def runtime_hashes(runtime):
    files = {}
    for folder in (JAVA_FOLDER, "hadoop/bin", "spark-home/bin", "spark-home/jars"):
        for path in sorted((runtime / folder).rglob("*")):
            if path.is_file():
                files[path.relative_to(runtime).as_posix()] = sha256(path)
    return files


def check_manifest(runtime):
    path = runtime / "setup-manifest.json"
    if not path.is_file():
        raise RuntimeError("Setup manifest missing; run setup_runtime.py without --check first")
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if manifest.get("java_version") != JAVA_VERSION or manifest.get("spark_version") != SPARK_VERSION:
        raise RuntimeError("Runtime manifest versions differ from setup pins")
    expected = manifest.get("files", {})
    if not expected or expected != runtime_hashes(runtime):
        raise RuntimeError("Runtime files differ from the setup manifest; installation stopped")
    print(f"PASS: {len(expected)} runtime files match the setup manifest", flush=True)


def smoke_test(runtime):
    java = runtime / JAVA_FOLDER
    result = subprocess.run([str(java / "bin/java.exe"), "-version"],
                            capture_output=True, text=True, check=True, timeout=30)
    if f'"{JAVA_VERSION}"' not in result.stderr + result.stdout:
        raise RuntimeError("Unexpected Java version")
    environment = os.environ.copy()
    temporary = runtime / "tmp"
    temporary.mkdir(exist_ok=True)
    environment.update({
        "JAVA_HOME": str(java), "HADOOP_HOME": str(runtime / "hadoop"),
        "SPARK_HOME": str(runtime / "spark-home"),
        "PYSPARK_PYTHON": sys.executable, "PYSPARK_DRIVER_PYTHON": sys.executable,
        "TMP": str(temporary), "TEMP": str(temporary), "TMPDIR": str(temporary),
        "PATH": str(java / "bin") + os.pathsep + str(runtime / "hadoop/bin")
                + os.pathsep + environment.get("PATH", ""),
    })
    code = '''
import sys, tempfile
from pathlib import Path
from pyspark.sql import SparkSession
root = Path(sys.argv[1])
spark = (SparkSession.builder.master("local[2]").appName("BDA_Runtime_Check")
    .config("spark.driver.bindAddress", "127.0.0.1")
    .config("spark.driver.host", "127.0.0.1")
    .config("spark.local.dir", str(root / "tmp"))
    .config("spark.sql.warehouse.dir", (root / "tmp/warehouse").as_uri())
    .getOrCreate())
try:
    assert spark.version == "4.0.4", spark.version
    with tempfile.TemporaryDirectory(dir=root / "tmp", prefix="setup_check_") as work:
        path = str(Path(work) / "rows.parquet")
        spark.range(5).write.parquet(path)
        rows = sorted(row.id for row in spark.read.parquet(path).collect())
        assert rows == list(range(5)), rows
    print("PASS: Java 17 / Spark 4.0.4 / Parquet write-read (5 rows)")
finally:
    spark.stop()
'''
    subprocess.run([sys.executable, "-c", code, str(runtime)], env=environment,
                   check=True, timeout=180)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify installed files and smoke-test, without downloads")
    parser.add_argument("--project-dir", type=Path, default=Path(__file__).resolve().parent,
                        help="Project root; defaults to the directory containing this script")
    args = parser.parse_args()
    if os.name != "nt" or platform.machine().lower() not in {"amd64", "x86_64"}:
        parser.error("This setup supports Windows x64 only")
    if sys.version_info[:2] != (3, 11) or sys.maxsize <= 2**32:
        parser.error("Use 64-bit Python 3.11")
    if importlib.metadata.version("pyspark") != SPARK_VERSION:
        parser.error("Install requirements.txt with this Python interpreter first")
    runtime = args.project_dir.resolve() / ".runtime"
    runtime.mkdir(parents=True, exist_ok=True)
    if not args.check and not (runtime / "setup-manifest.json").exists():
        with tempfile.TemporaryDirectory(dir=runtime, prefix="setup_staging_") as work:
            staging = Path(work)
            prepare_java(runtime, staging)
            sources = prepare_helpers(runtime, staging)
            prepare_spark(runtime, staging)
        manifest = {"java_version": JAVA_VERSION, "java_archive_url": JAVA_URL,
                    "java_archive_sha256": JAVA_SHA256, "spark_version": SPARK_VERSION,
                    "spark_source": "Installed PySpark package, SHA-256 verified against its RECORD",
                    "helpers": sources, "files": runtime_hashes(runtime)}
        (runtime / "setup-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    check_manifest(runtime)
    smoke_test(runtime)
    print("Runtime ready. Provide datasets_raw/, then run notebooks 01 -> 02 -> 03.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError,
            importlib.metadata.PackageNotFoundError, zipfile.BadZipFile) as error:
        print(f"SETUP FAILED: {error}", file=sys.stderr)
        sys.exit(1)
