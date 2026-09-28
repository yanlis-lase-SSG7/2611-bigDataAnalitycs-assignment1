# Current Task

Last updated: 2026-09-28

## Current Objective

Initial repository setup and GitHub publication for Assignment I, preserving existing local work and the remote README commit.

## Current Status

In progress

## Completed

- Inspected notebooks, reports, datasets, runtime, outputs, and existing documentation.
- Initialized local Git and retained existing origin/main history.
- Added .gitignore, AGENTS.md, dependency versions, and project documentation.
- Excluded datasets, runtime, environment, backups, course materials and large generated files.
- Archived and removed outdated/duplicate Markdown from the active folder.
- Documented project paths, Windows runtime prerequisites, and validated results.

## Remaining Work

- [ ] Complete project initialization commit.
- [ ] Push main to GitHub.
- [ ] Verify origin/main tracking and clean working tree.
- [ ] Finalize this document and push the documentation commit.

## Technical Decisions

Repository files are the persistent source of truth across devices; chat history is not required.
Keep notebooks with saved outputs, the current Word report, small aggregate result tables, and useful project documentation.
Use project-relative discovery or BDA_PROJECT_DIR instead of a fixed D: path. Keep all runtime/data/output files local to the selected project.
No Git LFS: large datasets and generated files remain local and can be recreated or transferred separately.

## Known Issues / Risks

- A clone does not contain source datasets, .venv, .runtime, or large generated outputs. Follow README for local setup before running notebooks.
- Windows-specific Spark runtime is required; the tested Spark launcher was patched for paths with spaces. Multi-node production execution is not validated.
- Model precision is low; temporal validation and intervention cost evaluation remain future work.
- Student must complete the AI declaration before submission. Video preparation remains separate from repository initialization.

## Validation

### Build

NOT AVAILABLE — notebook/Python project without a build step.

### Tests

PASS — all three notebook schemas and Python cells validated; saved outputs contain no errors; current model metrics checked. Candidate scan found no obvious secret patterns, including DOCX XML. All 24 candidate files are under 5 MiB; total approximately 0.48 MiB. Staged content review is required immediately before commit.
Full pipeline is not rerun solely for Git initialization; previously saved local runs are inspected.

## Recommended Next Step

Complete commit and push, then prepare Assignment I slides/video from the report and presentation notes.
