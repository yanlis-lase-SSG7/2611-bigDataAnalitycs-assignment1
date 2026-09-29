# Current Task

Last updated: 2026-09-29

## Current Objective

Publish automatic Windows runtime setup and lecturer packaging guidance so the project can be rerun without receiving machine-local Java/Spark binaries.

## Current Status

Ready for review

## Completed

- Added setup_runtime.py for Windows x64 / 64-bit Python 3.11 after requirements installation.
- Pinned Microsoft OpenJDK 17.0.20.1 and its publisher archive SHA-256; pinned Hadoop helpers to an immutable commit with known SHA-256 checksums.
- Copy Spark bin/jars from PySpark 4.0.4 only after validating package RECORD hashes; patch all three launcher path quoting sites for paths containing spaces.
- Record 837 runtime file hashes and smoke-test Java/Spark with a five-row Parquet write/read. Fresh runtime installation passed in an isolated ignored test directory, using existing installed Python dependencies.
- Verification-only --check rerun also passed: identical 837 file hashes and successful Java/Spark/Parquet smoke test without downloads.
- Existing conflicting runtime files are preserved; bad downloaded/cache checksums stop setup. Four integrity/preservation tests pass.
- Updated README, notebook guide and runtime guide with setup commands and lecturer ZIP contents. Dataset still supplied separately; .venv/.runtime excluded from ZIP and Git.
- Report PDF, Word and 11-slide PPT remain unchanged; narration is 1,238 words with a 9:30 target, not a measured recording duration.

## Remaining Work

- User reviews setup and lecturer packaging guidance on the target device. Commit/push is authorized; determine publication state from actual Git HEAD, origin/main and working tree.
- Create lecturer ZIP when requested; upload/SharePoint contents have not been verified.
- Student rehearses/records video (maximum 10 minutes), completes AI declaration and regenerates report PDF if changed.

## Technical Decisions

- Setup is an explicit command before notebook execution, not a silent download triggered inside a notebook. Python itself and requirements installation remain prerequisites.
- Windows x64 only; macOS/Linux/ARM64/Colab require adaptation. No system PATH edits or global Java installation.
- Microsoft Java source: https://learn.microsoft.com/en-us/java/openjdk/download. Hadoop helper repository is third-party, not an official Apache Windows binary distribution.
- Installed package RECORD and local manifest establish consistency, not publisher signatures. Download checksums are pinned in source.
- No analytic logic, saved notebook output or presentation metrics changed. Notebook order remains 01 -> 02 -> 03; local Spark prototype and low precision limitations still apply.

## Files Changed

- setup_runtime.py
- tests/test_setup_runtime.py
- README.md
- notebooks/README.md
- docs/runtime-prerequisites.md
- docs/current-task.md

## Known Issues / Risks

- First setup needs internet and disk space for Python dependencies, the approximately 187 MB Java archive, runtime and staging copies.
- Fresh runtime validated on the current Windows computer with existing Python dependencies, not on an independent lecturer device or newly installed Python environment.
- If existing unrecorded runtime differs, preserve/rename the indicated folder before retrying; script does not overwrite it.
- Video duration/audio/privacy of presenter notes and student AI declaration remain user review items.

## Validation

### Build

PASS — fresh runtime download/checksum, Spark launcher patch, Java version, Spark 4.0.4 and five-row Parquet round trip in a path containing spaces. --check rerun passed without downloads.

### Tests

PASS — four unittest safety checks (preserve conflicting local work, reject corrupt cache/downloads, detect modified runtime). Full analytics pipeline NOT RUN because analytic code did not change.

### Lint / Static Analysis

PASS — Python compile checks and git diff --check. Final source/documentation diff reviewed; dataset, runtime and QA artifacts remain ignored. Publication state is verified from Git separately.

## Environment Notes

- Windows x64, Python 3.11, PySpark 4.0.4, Java 17. Existing main project runtime remains unchanged.
- Ignored .report_review/runtime setup test/ contains isolated runtime testing artifacts. Earlier failed launcher attempt and corrected build remain there for QA; only the corrected build passed.
- Canonical root: D:\Private Project\bda\BDA_Olist_Project. main tracks origin/main; see actual Git status for publication state.

## Recommended Next Step

Package source, setup script, guides, raw CSVs and small saved reports for the lecturer. Use setup_runtime.py before notebooks; exclude environments, runtime, backups and generated large datasets.

## Useful Commands

```powershell
.\.venv\Scripts\python.exe setup_runtime.py
.\.venv\Scripts\python.exe setup_runtime.py --check
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe run_local_notebooks.py
```
