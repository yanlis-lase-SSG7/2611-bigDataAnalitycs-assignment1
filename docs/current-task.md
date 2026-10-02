# Current Task

Last updated: 2026-10-02

## Current Objective

Prepare and visually polish the Assignment I PowerPoint and one-video recording guide against the revised Word report and freshly rerun notebooks.

## Current Status

Ready for review

## Completed

- The three notebooks ran locally without cell errors. Their source cells are unchanged from HEAD; saved ingestion, model and graph numbers agree with the revised report.
- The Word report and matching 24-page PDF include measured EDA and the enterprise data-lake proposal. A governance-table sentence was corrected to match ephemeral salted seller tokens in the EDA script. The student-owned AI declaration was left untouched.
- Updated the existing 11-slide PPT. Slide 4 distinguishes all order statuses from delivered orders with valid delay labels; slide 6 shows tested local ingestion versus proposed enterprise storage/cluster; slide 8 shows measured null profiles and controls; slide 10 separates customer-state delay from seller-to-customer routes.
- Updated all 11 speaker notes from docs/presentation-notes.md and revised docs/presentation-video.md for a single-slide-show recording without a VS Code switch.
- Restyled all 11 slides with a consistent navy–teal editorial design. The cover and closing slide use a dark background, ingestion/model results emphasize the measured numbers, and stakeholder/technology tables remain editable. All speaker notes and key metrics were preserved. The user-renamed PPT path was retained and documentation links corrected.

## Remaining Work

- Student rehearses and records the video, checks the final duration is below 10 minutes, and verifies that speaker notes are not captured. The 9:30 timeline is an estimate, not a measured recording.
- Student reviews the AI Use Declaration, which still contains older statements about AI text/script use and tools. No AI percentage was selected or changed by Codex.
- The revised Word manuscript remains local and ignored by Git at the user's request. The updated PDF, renamed PPT, notebooks, EDA code, small aggregate reports, figures and documentation form the repository checkpoint. The superseded tracked report filenames are removed.

## Technical Decisions

- Keep 11 slides to protect the video time limit. The displayed demo results are checks performed earlier, not an execution inside the recording. Use a flat typographic layout with a dark cover/closing pair rather than adding decorative panels.
- Spark local[4], Parquet and the measured EDA are implemented locally. S3/HDFS, multi-node Spark, database servers and enterprise controls remain proposals pending benchmark and implementation.
- Slide 4 uses different denominators: 99,441 all-status orders versus 96,470 delivered orders with valid actual/estimated timestamps. Slide 10 distinguishes customer-state rates from primary-seller-to-customer routes.
- Four 300-DPI EDA PNGs and the architecture diagram are embedded presentation snapshots. If source data or figures change, refresh the PPT before making a new video.

## Files Changed

- presentations/Big Data Analytics - Laporan 2702751284.pptx and Big Data Analytics - Laporan 2702751284.pdf.
- eda_assignment1.py, make_eda_figures.py, figures/ and small EDA aggregate outputs.
- Saved outputs in notebooks 01–03 and ingestion_summary_report.csv.
- .gitignore, README.md, notebooks/README.md, docs/presentation-notes.md, docs/presentation-video.md and this file.

## Known Issues / Risks

- Narration is about 1,260 words after the latest clarification; the 9:30 estimate requires practice and a natural speaking rate near 140 words per minute when pauses are included. Trim examples if the rehearsal exceeds 10 minutes.
- No revised video was created after the PPT update because the student must record their own voice/presentation. Earlier SharePoint/video contents have not been independently verified.
- Existing report AI declaration is unchanged and needs student review before submission.

## Validation

### Build

PASS — PowerPoint opened the style candidate and exported 11 slides to PDF. All 11 slides were visually inspected at full size, and the final PPT is byte-identical to the validated candidate.

### Tests

PASS — four runtime safety tests and the read-only demo check. The three user-rerun notebooks saved error-free outputs that agree with report figures. PPT checks found 11 slides, notes unchanged on all 11, retained native tables and four EDA image slides, and preserved key metrics. No analytic pipeline was rerun during the style edit.

### Lint / Static Analysis

PASS — both new Python scripts compile; presentation package integrity had zero findings; layout geometry reported zero findings and warnings. Git whitespace and secret-pattern checks passed. EDA CSV headers contain aggregates only.

## Environment Notes

- Windows, Microsoft PowerPoint for render verification, Python 3.11 in .venv for PPT editing and validation. QA source and PDF renders are ignored under .report_review/.
- Root: D:\Private Project\bda\BDA_Olist_Project. Raw data, Parquet, runtime and .venv remain local.

## Recommended Next Step

Open the final PPT, rehearse with Presenter View or a separate notes device, make a 20-second test recording, then record and check one complete video under 10 minutes. Review the AI declaration before submitting the report.

## Useful Commands

```powershell
.\.venv\Scripts\python.exe demo_assignment1.py
```
