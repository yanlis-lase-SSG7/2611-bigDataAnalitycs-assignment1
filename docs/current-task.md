# Current Task

Last updated: 2026-09-28

## Current Objective

Revise Assignment I presentation into a complete PowerPoint-only explanation with conversational speaker notes, detailed project/technology rationale and previously executed demo results; commit and push the reviewed changes.

## Current Status

Ready for review

## Completed

- Updated presentations/Assignment_I_Olist_2702751284.pptx to 11 editable 16:9 slides.
- Rewrote speaker notes as natural Indonesian narration in short paragraphs. Sources and target timing appear separately after narration.
- Explained the project, background problem, goals, stakeholders, pipeline/grain, tech stack and rationale, governance and implementation limits.
- Incorporated the user's successful ingestion/model/graph demo results into slides 7/9/10, with a PASS summary and closing on slide 11.
- Replaced the previous PowerPoint-to-VS-Code recording flow with a complete PowerPoint-only presentation. Updated README, narration copy and recording guide.
- Exported/inspected all slide layouts in native PowerPoint. Fixed the tech-stack table/caption overlap and rechecked the corrected slide. Final notes-only revision preserves visible slide content.
- Validated package, geometry, notes/source/timing consistency and metrics. New PPT matches the reviewed candidate byte-for-byte; previous PPT is preserved in Git and ignored QA backup.

## Remaining Work

- User rehearses the 1,040-word narration with a stopwatch and records the video, maximum 10 minutes. 9:10 is a target, not measured recording duration.
- Confirm final recording shows the slides, with notes/Presenter View only on the private display, and verify audio/readability.
- Student completes AI declaration and exports final submission PDF after final Word edits.

## Technical Decisions

- Prior user approval permits local PowerPoint COM authoring instead of the unavailable artifact-tool runtime. No new project dependencies added.
- Same canonical PPT filename updated as requested. Native text/tables remain editable; slide advance is manual.
- Results explicitly represent earlier read-only checks of saved reports, not live ingestion/training in the recording. demo_assignment1.py remains optional for separate verification/Q&A.
- Spark runs local[4] on one machine. pandas remains suitable for this dataset size. Warehouse is conceptual; NoSQL/physical graph database/dashboard are proposed.
- Baseline: 96,470 labels / 7,826 delayed, reviews 4.2943 versus 2.5665, storage savings 54.93%. Model: unweighted RF, threshold 0.099536, validation F1 0.2168, test recall 45.41%, precision 14.47%, 4,186 FP. Graph: 27 nodes / 409 routes, SP–RJ 8,158 orders / 15.49% delay.
- Review associations do not establish causation; state graph does not show transit or physical hub locations. External surveys provide context distinct from Olist data.
- User explicitly authorized commit and push. Actual Git HEAD, origin/main and status determine publication state.

## Files Changed

- presentations/Assignment_I_Olist_2702751284.pptx: 11-slide full-PPT presentation.
- docs/presentation-notes.md: exact spoken narration and sources.
- docs/presentation-video.md: timing and private-notes recording guidance.
- README.md: revised presentation/recording links.
- docs/current-task.md: current scope and verified state.

## Known Issues / Risks

- Actual video duration, recording setup and audio are not yet verified. Rehearsal is required.
- Low model precision, temporal validation and intervention cost evaluation remain future work; operational impact and cluster scalability are not demonstrated.
- Student fills AI declaration; do not choose the percentage.
- Git excludes datasets/runtime/generated QA. Another computer needs local prerequisites separately to run notebooks.

## Validation

### Build

PASS — Microsoft PowerPoint authored/exported the 11-slide deck. Reviewed candidate copied unchanged to the canonical PPT path.

### Tests

PASS — all 11 notes match the narration/source/timing data; metrics match saved reports and user's demo; PPT-only flow checked. No notebook/model logic changed, so full analytics pipeline NOT RUN.

### Lint / Static Analysis

PASS — package integrity and layout/heading validators: zero findings and zero warnings. All visible slide content inspected, final changed slide rechecked. Whitespace checks pass. Word and notebook files unchanged. Generated QA/scripts/backups remain ignored.

## Environment Notes

- Windows, Microsoft PowerPoint, Python 3.11 in .venv. PowerPoint authoring/export session closed after saving.
- .report_review/full_ppt/ contains ignored QA, source JSON, intermediate decks and old PPT backup; not required for viewing/rehearsing the deliverable.
- Notebook stack remains PySpark 4.0.4, Java 17, pandas and NetworkX. See docs/runtime-prerequisites.md.
- Local project/BDA_PROJECT_DIR controls reads/writes. No Colab/Google Drive. main tracks origin/main.

## Recommended Next Step

Rehearse the revised PPT using conversational notes, perform a short recording test to keep notes off-screen, then record the entire presentation in PowerPoint and check duration/audio.

## Useful Commands

```powershell
git status
git log -5 --oneline
git diff
.\.venv\Scripts\python.exe demo_assignment1.py
```

The demo is optional for pre-recording checks; no terminal interaction is required in the presentation video.
