# Current Task

Last updated: 2026-09-28

## Current Objective

Publish the reviewed report revision and prepare a short Assignment I presentation followed by a live demo in the same video, within the 10-minute limit.

## Current Status

Ready for review

## Completed

- Strengthened section 1.2 using DHL Group 2026 survey context and OECD 2019 platform trust/reviews discussion, with explicit limits on transfer to historical Olist data.
- Connected business priorities to stakeholder decisions and consistent success measures; no unmeasured cost savings or numeric intervention targets claimed.
- Removed nine uncited bibliography entries; all 14 remaining references have body citations.
- Corrected graph labels implying observed hubs/bottlenecks. Kept all table values, notebook source, analytics outputs and student declaration wording unchanged.
- Updated presentation notes. Rendered and visually inspected all 19 report pages; bibliography/form pages rechecked after final layout corrections.
- Prepared docs/presentation-video.md: nine-slide storyboard, narration and sources, seven-minute presentation followed by a two-minute demo and 15-second closing.
- Added demo_assignment1.py, a standard-library read-only checker for saved ingestion/model/graph reports. It does not rerun the analytics pipeline.

## Remaining Work

- Student completes AI declaration; Codex did not select a contribution percentage.
- Create PPTX from the prepared storyboard, review slides, rehearse and record one video (maximum 10 minutes). PPTX authoring runtime is unavailable in this session.
- Export submission PDF after final student edits.

## Technical Decisions

- External surveys explain market relevance, not Olist customer behavior in 2016–2018. Faster delivery preference differs from lateness against an estimated timestamp.
- Review differences are associations; state graphs do not prove transit, hub locations or physical bottlenecks. Intervention impacts/costs are not measured.
- Verified results remain authoritative: 96,470 labeled orders, 7,826 delayed; review 4.2943 versus 2.5665; Parquet savings 54.93%.
- Student declaration wording preserved; form layout corrections only.
- Local project root/BDA_PROJECT_DIR controls reads/writes. Datasets/runtime and generated QA remain ignored. main tracks origin/main; publication requires user authorization.
- User authorized commit and push of this checkpoint. Determine publication state from actual Git HEAD, origin/main and working tree rather than a historical documentation entry.
- Demo recalculates metrics from saved aggregates and checks cross-report consistency. It does not prove current raw/Parquet contents, split disjointness or absence of leakage. Full notebook execution occurred previously.

## Files Changed

- Laporan Big Data Analytics - 2702751284.docx: section 1.2, references, graph labels and layout.
- docs/presentation-notes.md: market/business context aligned with report.
- docs/presentation-video.md: slide storyboard, timed narration, demo and recording procedure.
- demo_assignment1.py: read-only saved-result checker.
- README.md: links to video preparation and demo usage.
- docs/current-task.md: current video preparation and publication state.

## Known Issues / Risks

- Repository instructions guide Codex; they do not install a background service or Git hook or synchronize files outside Codex.
- Cross-device updates require successful commit/push and pull. Another laptop needs datasets, dependencies and Windows runtime separately to execute notebooks.
- Spark remains a one-machine prototype; warehouse is conceptual. NoSQL/graph database deployment and dashboard remain proposed. Low model precision, temporal validation and intervention cost evaluation remain future work.
- AI declaration remains the student's responsibility; do not determine its percentage.
- The Presentations skill requires load_workspace_dependencies and its artifact-tool runtime; neither is available here. No PPTX has been authored. Storyboard/narration and demo are available for the next step.

## Validation

### Build

NOT AVAILABLE — notebook/Python project without a build step.

### Tests

PASS — demo all/ingestion/model/graph modes succeed; corrupted ingestion status, confusion counts and graph counts fail; source report hashes unchanged. Full analytics pipeline NOT RUN because no analytic logic changed.

### Lint / Static Analysis

PASS — report citations, unchanged table values, current metrics and declaration wording verified; notebook source unchanged. All 19 Word-rendered pages inspected; form clipping corrected. Demo/notebook Python syntax and staged whitespace checks pass. Six intended files reviewed, all below 5 MiB, with no credentials found by content review and heuristic scan. Report matches the reviewed SHA-256. Local QA in .report_review remains ignored.

## Environment Notes

- Windows; Python 3.11; PySpark 4.0.4; Java 17. requirements.txt records dependencies.
- Use .venv/Scripts/python.exe and kernel bda-local. Run notebooks 01 → 02 → 03; run_local_notebooks.py is the supported runner.
- Root discovery or BDA_PROJECT_DIR selects the checkout. Keep reads, writes and staging local; no Colab/Google Drive.
- Restore .runtime/jdk-*, .runtime/hadoop/bin and .runtime/spark-home on another laptop. Tested Windows launcher handles paths with spaces; see docs/runtime-prerequisites.md.

## Recommended Next Step

Create PPTX from docs/presentation-video.md when the required authoring runtime is available, rehearse the demo, complete the student declaration and record the presentation/demo as one video.

## Useful Commands

```powershell
git status
git log -5 --oneline
git diff
git diff --cached
git pull --ff-only
.\.venv\Scripts\python.exe run_local_notebooks.py
.\.venv\Scripts\python.exe demo_assignment1.py
```

The runner executes/saves all three notebooks and replaces generated outputs. Run only when intended and local prerequisites are available.
