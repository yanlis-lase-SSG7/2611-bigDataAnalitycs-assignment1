# Current Task

Last updated: 2026-09-28

## Current Objective

Create a nine-slide Assignment I PPTX from docs/presentation-video.md, with speaker notes, sources and a transition to a short live demo in the same video.

## Current Status

Ready for review

## Completed

- Created presentations/Assignment_I_Olist_2702751284.pptx with nine editable 16:9 slides and eight native tables.
- Included storyboard narration, sources and target presentation timing in all nine speaker notes. Notes for slide 9 include the two-minute demo and closing script.
- Exported every slide using Microsoft PowerPoint and inspected all nine images individually. No visual clipping or overlap found.
- Verified PPTX structure, slide count/aspect, notes, source URLs, metrics and demo commands. Updated README and video guide to reference the actual deck.
- Report/storyboard/demo checkpoint remains published at 0168e1e2d3c13076643d7bdc5a11ae1048333b10. Word and notebooks were not modified by the PPT task.
- User ran all three demo sections locally and shared successful results matching the PPT/report: ingestion 54.93% savings, model recall 45.41% / precision 14.47%, graph SP–RJ 8,158 orders / 15.49% delay.

## Remaining Work

- User reviews the PPT and rehearses with a stopwatch. Seven-minute presentation, two-minute demo and 15-second closing are targets, not measured recording duration.
- Record one video of at most 10 minutes, keeping the recording running when switching from PowerPoint to VS Code.
- Student completes the AI declaration and exports the submission PDF after final student edits.

## Technical Decisions

- User explicitly approved local PowerPoint authoring as a replacement for the unavailable skill-required artifact-tool runtime. Used PowerPoint COM, without adding project dependencies.
- Deck uses Aptos, navy/teal on white, editable text/native tables and manual slide advance. No external images or embedded raw records.
- Assignment I problem/design/governance/data preparation remains the main focus. ML/graf are early exploration; warehouse is conceptual, databases/dashboard are proposed and Spark local[4] is one machine.
- All displayed results follow verified saved outputs: 96,470 labeled orders / 7,826 delayed, review 4.2943 versus 2.5665, storage savings 54.93%, test recall 45.41% / precision 14.47%, SP–RJ 8,158 orders / 15.49% delay.
- Reviews are associations and the state graph does not show transit or physical hubs. External DHL/OECD sources provide context distinct from historical Olist behavior.
- Demo script checks consistency of saved aggregate reports. It does not rerun ingestion/training or prove split disjointness/leakage absence.
- User authorized commit and push of the PPT/documentation checkpoint. Determine publication state from actual HEAD, origin/main and working tree rather than a historical documentation entry.

## Files Changed

- presentations/Assignment_I_Olist_2702751284.pptx: new presentation.
- README.md: actual PPT link and availability.
- docs/presentation-video.md: deck usage and rehearsal guidance.
- docs/current-task.md: current PPT state and verification.

## Known Issues / Risks

- Recording duration/audio/readability must be verified after rehearsal and recording. Presenter View should not appear in the audience recording.
- A layout heuristic estimated possible table overflow on slide 4; native PowerPoint render shows full table and footer with clear separation. COM bound diagnostics also gave false text-box warnings resolved by visual review.
- Model precision remains limited; temporal validation and intervention costs remain future work. No measured operational impact or cluster performance.
- AI declaration remains the student's responsibility; do not choose its percentage.
- Another laptop needs datasets/dependencies/runtime separately to run notebooks. Git excludes these and generated QA.

## Validation

### Build

PASS — native PowerPoint saved the PPTX and exported all nine slides to PNG in ignored .report_review/ppt_review/.

### Tests

PASS — PPTX ZIP integrity, nine slide/note pairs, 16:9 dimensions, eight native tables, narration/source URLs, displayed model metrics and demo commands checked. User also confirmed all three demo sections pass locally. Analytics pipeline NOT RUN because analytic logic did not change.

### Lint / Static Analysis

PASS — skill package integrity validator: zero findings; geometry/heading validator: zero findings, one heuristic table warning visually resolved. All nine slide renders inspected individually. Word/notebook changes absent. Whitespace checks passed. QA/build scripts and PNGs remain ignored.

## Environment Notes

- Windows with Microsoft PowerPoint installed; current user authorized its local automation. PowerPoint authoring/export session was closed after saving.
- Python 3.11 in .venv for verification. No python-pptx or additional packages installed for deck creation.
- Notebook stack remains PySpark 4.0.4, Java 17 and Windows runtime. See docs/runtime-prerequisites.md.
- Local root/BDA_PROJECT_DIR controls input/output. No Colab or Google Drive.
- main tracks origin/main. Inspect actual Git state before any future publication.

## Recommended Next Step

Review the PPT in PowerPoint, rehearse the seven-minute narrative and live demo using docs/presentation-video.md, then record the continuous video and verify its actual duration/audio/readability.

## Useful Commands

```powershell
git status
git log -5 --oneline
git diff
.\.venv\Scripts\python.exe demo_assignment1.py
.\.venv\Scripts\python.exe demo_assignment1.py --section model
```

Notebook Run All is unnecessary during the short demo unless outputs actually need regeneration.
