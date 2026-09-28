# Current Task

Last updated: 2026-09-28

## Current Objective

Make Codex continuity automatic across office and home laptops through repository context, continuous documentation maintenance, and synchronization before authorized commits/pushes.

## Current Status

Completed

## Completed

- Replaced manual command-triggered workflow with automatic session initialization and ongoing documentation maintenance in AGENTS.md.
- Defined automatic pre-commit documentation synchronization and pre-push verification, preserving authorization scope and unrelated local work.
- Replaced historical initialization/cleanup summaries with current development context and the required task-state structure.
- Documented normal cross-device usage in README. No notebook logic, dependencies, Git ignore rules or runtime configuration changed.
- Final review confirmed the automatic workflow matches the requested behavior; user authorized commit and push.

## Remaining Work

- No workflow implementation or review work remains. Publication is checked against actual Git state rather than a historical session entry.
- Project follow-up: prepare Assignment I slides/video (maximum 10 minutes) and complete the student AI declaration before submission. These deliverables were not created by this workflow task.

## Technical Decisions

- Actual source and Git history take precedence over stale documentation or chat history.
- Keep task state concise; durable guidance belongs in README, AGENTS.md, notebooks/README.md and docs/runtime-prerequisites.md.
- Documentation maintenance is automatic during Codex work; commits and publication still require user authorization.
- Commit-only requests do not authorize pushing. Push requests include needed documentation synchronization, without silently committing unrelated implementation changes.
- main tracks origin/main at https://github.com/yanlis-lase-SSG7/2611-bigDataAnalitycs-assignment1.git. Inspect Git status/history to determine the current publication state.
- Datasets, .venv, .runtime and large outputs remain local; small aggregate reports and saved notebook outputs are tracked. No Git LFS.

## Files Changed

- AGENTS.md: automatic session, documentation, commit/push and task-transition policies.
- docs/current-task.md: current-state structure; obsolete history removed.
- README.md: normal office/home continuity workflow and local setup limitation.

## Known Issues / Risks

- Repository instructions guide Codex; they do not install a background service or Git hook or synchronize files outside Codex.
- Cross-device updates require successful commit/push and pull. Another laptop needs datasets, dependencies and Windows runtime separately to execute notebooks.
- Spark remains a one-machine prototype; warehouse is conceptual. NoSQL/graph database deployment and dashboard remain proposed. Low model precision, temporal validation and intervention cost evaluation remain future work.
- AI declaration remains the student's responsibility; do not determine its percentage.

## Validation

### Build

NOT AVAILABLE — notebook/Python project without a build step.

### Tests

NOT RUN — full analytics pipeline unnecessary for documentation-only changes. Saved outputs remain from prior local execution.

### Lint / Static Analysis

PASS — workflow sections and task-state structure checked; eight local Markdown links resolve; all three notebooks pass schema/cell syntax checks and contain no saved errors. Changed documentation was reviewed for obvious secrets and inappropriate generated files; only AGENTS.md, README.md and docs/current-task.md are included. Whitespace checks pass.

## Environment Notes

- Windows; Python 3.11; PySpark 4.0.4; Java 17. requirements.txt records dependencies.
- Use .venv/Scripts/python.exe and kernel bda-local. Run notebooks 01 → 02 → 03; run_local_notebooks.py is the supported runner.
- Root discovery or BDA_PROJECT_DIR selects the checkout. Keep reads, writes and staging local; no Colab/Google Drive.
- Restore .runtime/jdk-*, .runtime/hadoop/bin and .runtime/spark-home on another laptop. Tested Windows launcher handles paths with spaces; see docs/runtime-prerequisites.md.

## Recommended Next Step

On another laptop, pull the latest main, open VS Code and give a normal task. Next project work is Assignment I slides/video and the student AI declaration. Codex should replace this completed objective when that work begins, preserving relevant unresolved project notes.

## Useful Commands

```powershell
git status
git log -5 --oneline
git diff
git diff --cached
git pull --ff-only
.\.venv\Scripts\python.exe run_local_notebooks.py
```

The runner executes/saves all three notebooks and replaces generated outputs. Run only when intended and local prerequisites are available.
