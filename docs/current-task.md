# Current Task

Last updated: 2026-09-29

## Current Objective

Clarify the 11-slide presenter narration using everyday Indonesian, concrete explanations of the workflow and metrics, and a realistic reading pace within the 10-minute recording limit.

## Current Status

Ready for review

## Completed

- Updated speaker notes in the existing 11-slide PPT through native PowerPoint; visible slide text, tables and layouts preserved.
- Made explanations more concrete: timestamp delay/baseline, aggregate-before-join with repeated values, technology roles, train/validation/test, threshold, precision/recall and false positives, state graph and the meaning of PASS.
- Narration has 1,238 words in short paragraphs, with references/timing separate. Reading target changed to 9:30 (approximately 130 words/minute); actual recording must be measured.
- Updated the exact narration copy and recording timing guide. Added three private comprehension prompts to the Markdown narration for rehearsal, outside spoken text.
- Exported all 11 slides and verified their pixels are identical to the previously reviewed renders. Package and note/source/timing checks pass.

## Remaining Work

- User rehearses the 1,238-word narration with a stopwatch and records the video, maximum 10 minutes. 9:30 is a target, not measured recording duration; a slower pace requires shortening the explanation.
- Confirm final recording shows the slides, with notes/Presenter View only on the private display, and verify audio/readability.
- Student completes AI declaration and exports final submission PDF after final Word edits.

## Technical Decisions

- Prior user approval permits local PowerPoint COM authoring instead of the unavailable artifact-tool runtime. No new project dependencies added.
- Same canonical PPT filename updated as requested. Native text/tables remain editable; slide advance is manual.
- Results explicitly represent earlier read-only checks of saved reports, not live ingestion/training in the recording. demo_assignment1.py remains optional for separate verification/Q&A.
- Spark runs local[4] on one machine. pandas remains suitable for this dataset size. Warehouse is conceptual; NoSQL/physical graph database/dashboard are proposed.
- Baseline: 96,470 labels / 7,826 delayed, reviews 4.2943 versus 2.5665, storage savings 54.93%. Model: unweighted RF, threshold 0.099536, validation F1 0.2168, test recall 45.41%, precision 14.47%, 4,186 FP. Graph: 27 nodes / 409 routes, SP–RJ 8,158 orders / 15.49% delay.
- Review associations do not establish causation; state graph does not show transit or physical hub locations. External surveys provide context distinct from Olist data.
- User authorized commit and push of the narration revision. Determine publication state from actual HEAD, origin/main and working tree. Pre-existing Word/PDF changes remain outside this revision.

## Files Changed

- presentations/Assignment_I_Olist_2702751284.pptx: updated notes only; visible slides unchanged.
- docs/presentation-notes.md: exact spoken narration and sources.
- docs/presentation-video.md: timing and private-notes recording guidance.
- README.md: updated 9:30 duration target.
- docs/current-task.md: current scope and verified state.

## Known Issues / Risks

- Actual video duration, recording setup and audio are not yet verified. Rehearsal is required.
- Low model precision, temporal validation and intervention cost evaluation remain future work; operational impact and cluster scalability are not demonstrated.
- Student fills AI declaration; do not choose the percentage.
- Git excludes datasets/runtime/generated QA. Another computer needs local prerequisites separately to run notebooks.
- Pre-existing user changes remain local in the Word report, plus an untracked submission PDF. They are excluded from the narration commit; review/publish separately if requested.

## Validation

### Build

PASS — Microsoft PowerPoint edited notes, saved a new candidate and exported all 11 slides. Verified candidate copied to the canonical PPT path.

### Tests

PASS — all 11 notes match the narration/source/timing data; all 11 exported slide images are pixel-identical to the reviewed originals. Text encoding and 570-second target verified. No notebook/model logic changed, so full analytics pipeline NOT RUN.

### Lint / Static Analysis

PASS — package integrity validator reports zero findings. Visible slide texts and rendered pixels unchanged, so previous visual layout review remains valid. Whitespace checks pass. Generated QA/scripts/backups remain ignored. Pre-existing Word/PDF user changes remain separate.

## Environment Notes

- Windows, Microsoft PowerPoint, Python 3.11 in .venv. PowerPoint authoring/export session closed after saving.
- .report_review/notes_20260929/ contains ignored notes data, before/candidate decks, native renders and verification.json. These are not required to view or rehearse the deliverable.
- Notebook stack remains PySpark 4.0.4, Java 17, pandas and NetworkX. See docs/runtime-prerequisites.md.
- Local project/BDA_PROJECT_DIR controls reads/writes. No Colab/Google Drive. main tracks origin/main.

## Recommended Next Step

Rehearse the clearer narration at a comfortable pace. Explain the three comprehension prompts in docs/presentation-notes.md in your own words, then perform a recording test and measure the full presentation duration.

## Useful Commands

```powershell
git status
git log -5 --oneline
git diff
.\.venv\Scripts\python.exe demo_assignment1.py
```

The demo is optional for pre-recording checks; no terminal interaction is required in the presentation video.
