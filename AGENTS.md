# Project instructions

## Session Start

At every session start, and on `resume`, `continue`, `lanjut`, or `lanjutkan`:
1. Read this file and `docs/current-task.md`.
2. Run `git status` and review recent commits.
3. Inspect the relevant source files before editing.
4. Treat the repository as more authoritative than old chat context; continue from its actual state.

## Handoff

On `handoff`, `prepare handoff`, `switch device`, `saya mau lanjut di rumah`, or `saya mau lanjut di kantor`:
1. Inspect `git status`, `git diff`, and changed files.
2. Update `docs/current-task.md`; update other documentation only when implementation changes made it outdated.
3. Run appropriate validation; report remaining work and suggest a commit message.
4. Do not automatically commit or push without explicit authorization.

## Documentation Principle

Persist important context in source, tests where relevant, README, project documentation, and `docs/current-task.md`. Chat history must not be necessary to continue development.

## Git Safety

Never automatically run `git reset --hard`, `git clean -fd`, or force push. Never discard local work without explicit permission. Never commit credentials, datasets, runtime binaries, caches, or large generated outputs. Review the staged diff before committing. Preserve existing remote history.

## Project conventions

- Python 3.11, PySpark 4.0.4, Java 17, pandas, NetworkX; local Windows prototype.
- Execute notebooks 01 → 02 → 03. Keep raw data unchanged. Keep all inputs, computation staging and outputs within the local project directory; do not use Colab/Google Drive.
- Use `BDA_PROJECT_DIR` to select the project on another computer. It defaults to the repository root when opened from the root or `notebooks/`.
- Model/label defaults, aggregate-before-join rules, split and threshold choices are documented in `notebooks/README.md`. Do not change them silently.
- Distinguish observed results from proposed architecture. Warehouse is conceptual; NetworkX is not a graph database; reviews text/JSON audit is not a document store; local Spark is not evidence of cluster scalability.
- The student's AI declaration is for the student to fill; do not choose a contribution percentage or rewrite it without instruction.
- Validate notebook structure, Python cell syntax and saved outputs for documentation/configuration changes. Run the pipeline when analytic logic changes and local datasets/runtime are available; record what was actually run.
- Avoid rerunning legacy maintenance scripts: they can overwrite notebook revisions or the current report. They are deliberately excluded from Git.
