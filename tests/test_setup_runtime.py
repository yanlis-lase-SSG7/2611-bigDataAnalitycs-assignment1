"""Integrity and local-work preservation checks for the runtime installer."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import setup_runtime as setup


class RuntimeSafetyTests(unittest.TestCase):
    def test_conflicting_runtime_is_preserved(self):
        with tempfile.TemporaryDirectory() as work:
            root = Path(work)
            staged, existing = root / "staged", root / "existing"
            staged.mkdir()
            existing.mkdir()
            (staged / "java.exe").write_bytes(b"new")
            (existing / "java.exe").write_bytes(b"local work")
            with self.assertRaisesRegex(RuntimeError, "no existing file has been replaced"):
                setup.publish_directory(staged, existing)
            self.assertEqual((existing / "java.exe").read_bytes(), b"local work")

    def test_corrupt_cached_download_never_gets_executed_or_replaced(self):
        with tempfile.TemporaryDirectory() as work:
            target = Path(work) / "java.zip"
            target.write_bytes(b"corrupt")
            with patch("urllib.request.urlopen") as network:
                with self.assertRaisesRegex(RuntimeError, "Checksum mismatch"):
                    setup.download("https://example.com/java.zip", target, "0" * 64)
                network.assert_not_called()
            self.assertEqual(target.read_bytes(), b"corrupt")

    def test_bad_network_checksum_leaves_no_archive(self):
        import io

        class Response(io.BytesIO):
            url = "https://example.com/java.zip"

        with tempfile.TemporaryDirectory() as work:
            target = Path(work) / "java.zip"
            with patch("urllib.request.urlopen", return_value=Response(b"untrusted bytes")):
                with self.assertRaisesRegex(RuntimeError, "Downloaded checksum mismatch"):
                    setup.download("https://example.com/java.zip", target, "0" * 64)
            self.assertEqual(list(Path(work).iterdir()), [])

    def test_modified_runtime_is_detected(self):
        with tempfile.TemporaryDirectory() as work:
            runtime = Path(work)
            folder = runtime / "hadoop/bin"
            folder.mkdir(parents=True)
            path = folder / "hadoop.dll"
            path.write_bytes(b"original")
            manifest = {"java_version": setup.JAVA_VERSION,
                        "spark_version": setup.SPARK_VERSION,
                        "files": {"hadoop/bin/hadoop.dll": hashlib.sha256(b"original").hexdigest()}}
            (runtime / "setup-manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
            path.write_bytes(b"changed")
            with self.assertRaisesRegex(RuntimeError, "differ from the setup manifest"):
                setup.check_manifest(runtime)


if __name__ == "__main__":
    unittest.main()
