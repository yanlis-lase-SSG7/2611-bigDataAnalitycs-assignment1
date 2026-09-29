# Current Task

Last updated: 2026-09-29

## Current Objective

Synchronize and publish all remaining report deliverables, preserving the clarified 11-slide narration and recording guidance.

## Current Status

Ready for review

## Completed

- Updated speaker notes in the existing 11-slide PPT through native PowerPoint; visible slide text, tables and layouts preserved.
- Made explanations more concrete: timestamp delay/baseline, aggregate-before-join with repeated values, technology roles, train/validation/test, threshold, precision/recall and false positives, state graph and the meaning of PASS.
- Narration has 1,238 words in short paragraphs, with references/timing separate. Reading target changed to 9:30 (approximately 130 words/minute); actual recording must be measured.
- Updated the exact narration copy and recording timing guide. Added three private comprehension prompts to the Markdown narration for rehearsal, outside spoken text.
- Exported all 11 slides and verified their pixels are identical to the previously reviewed renders. Package and note/source/timing checks pass.
- Reviewed remaining user-saved Word/PDF files. Word paragraph text is unchanged from the previous committed report; the remaining change is in the document package/formatting. PDF has 19 readable pages and matching substantive long paragraphs/key metrics; TOC/index/header extraction differs.
- Added the report PDF link in README. The previously observed untracked PPT copy is no longer present; no copy file is pending publication.

## Remaining Work

- User rehearses the 1,238-word narration with a stopwatch and records the video, maximum 10 minutes. 9:30 is a target, not measured recording duration; a slower pace requires shortening the explanation.
- Confirm final recording shows the slides, with notes/Presenter View only on the private display, and verify audio/readability.
- Student reviews/completes AI declaration before submission. A PDF export is available; regenerate it if subsequent Word edits occur.

## Technical Decisions

- Prior user approval permits local PowerPoint COM authoring instead of the unavailable artifact-tool runtime. No new project dependencies added.
- Same canonical PPT filename updated as requested. Native text/tables remain editable; slide advance is manual.
- Results explicitly represent earlier read-only checks of saved reports, not live ingestion/training in the recording. demo_assignment1.py remains optional for separate verification/Q&A.
- Spark runs local[4] on one machine. pandas remains suitable for this dataset size. Warehouse is conceptual; NoSQL/physical graph database/dashboard are proposed.
- Baseline: 96,470 labels / 7,826 delayed, reviews 4.2943 versus 2.5665, storage savings 54.93%. Model: unweighted RF, threshold 0.099536, validation F1 0.2168, test recall 45.41%, precision 14.47%, 4,186 FP. Graph: 27 nodes / 409 routes, SP–RJ 8,158 orders / 15.49% delay.
- Review associations do not establish causation; state graph does not show transit or physical hub locations. External surveys provide context distinct from Olist data.
- User explicitly authorized commit and push of all remaining appropriate changes, including the Word report and PDF export. Determine publication state from actual HEAD, origin/main and working tree.

## Files Changed

- Laporan Big Data Analytics - 2702751284.docx: user-saved document update, paragraph text unchanged from Git.
- Laporan Big Data Analytics - 2702751284.pdf: new 19-page report export.
- README.md: report PDF link and regeneration guidance.
- docs/current-task.md: report publication scope and validation; narration/recording guidance already committed.

## Known Issues / Risks

- Actual video duration, recording setup and audio are not yet verified. Rehearsal is required.
- Low model precision, temporal validation and intervention cost evaluation remain future work; operational impact and cluster scalability are not demonstrated.
- Student fills AI declaration; do not choose the percentage.
- Git excludes datasets/runtime/generated QA. Another computer needs local prerequisites separately to run notebooks.

## Validation

### Build

PASS — prior PowerPoint notes build remains unchanged. Existing report PDF opened/read successfully; no document generation or analytic build needed for this publication.

### Tests

PASS — Word ZIP/text review, PDF page/text/key-metric checks and credential-pattern scan. Report body text unchanged; PDF extraction differences are TOC/index entries and the declaration form header. Prior narration/570-second target verification remains valid. Full analytics pipeline NOT RUN because code/results did not change.

### Lint / Static Analysis

PASS — report sizes are 400,122 bytes (Word) and 658,698 bytes (PDF). No credential patterns or embedded Word files found. Publication content reviewed; whitespace checks pass. Runtime, datasets and generated QA remain ignored. PDF checks establish readability/content, not a new full visual layout review.

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
