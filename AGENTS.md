# AGENTS.md - Codex Operating Guide

This repository is a Stata empirical-research workflow template. Codex should preserve the existing Stata pipeline behavior while using this file as the primary project instruction source.

## Project Purpose

- Maintain a reproducible Stata workflow for empirical economics research.
- Keep `dofiles/00_master.do` as the single end-to-end pipeline entry point.
- Keep raw data out of version control.
- Produce audit-friendly tables, figures, logs, and Quarto reports.
- Preserve the existing Claude Code assets under `.claude/` as reference material; do not remove them unless the user explicitly asks.

## Repository Map

- `dofiles/00_master.do`: canonical pipeline orchestrator.
- `dofiles/01_clean/`: raw data to cleaned data.
- `dofiles/02_construct/`: variable construction and samples.
- `dofiles/03_analysis/`: estimation, robustness, event studies, IV, DiD, etc.
- `dofiles/04_output/`: table and figure assembly.
- `dofiles/_utils/`: reusable Stata helpers.
- `data/raw/`: raw datasets, gitignored.
- `data/derived/`: intermediate datasets, gitignored.
- `logs/`: Stata logs, gitignored.
- `output/tables/`: committed publication/audit tables.
- `output/figures/`: committed figures.
- `reports/`: Quarto reports.
- `scripts/`: wrappers and quality tooling.
- `templates/`: reusable project templates.
- `templates/private-study-skeleton/`: template for real private research projects outside this public workflow repository.
- `agents/`: economics-paper specialist agent prompts for literature review, theory audit, QA, and response drafting.
- `skills/`: economics research workflow skills for ideation, results interpretation, writing, QA, and post-acceptance work.
- `results_memos/`: interpretation memos such as theory audits and story diagnostics.
- `quality_reports/specs/`: project requirement specs and task briefs.
- `quality_reports/good_questions/`: Good Question Cards for early research-question screening.
- `quality_reports/checkpoints/`: structured session handoff snapshots for long projects.
- `quality_reports/decisions/`: architectural or research decision records.
- `quality_reports/preregistrations/`: preregistration drafts and review artifacts.
- `quality_reports/passports/`: numeric-claim provenance passports for manuscript verification.
- `.claude/`: legacy Claude Code agents, skills, rules, and hooks. Treat as reference.

## Economics Workflow Overlay

This repository now includes a paper-workflow overlay in addition to the Stata pipeline.

- Keep the Stata workflow as the execution backbone.
- Use `dofiles/` to generate artifacts first.
- Use the migrated `skills/` and `agents/` to interpret, write up, QA, and revise based on those artifacts.
- Treat `agents/` and `skills/` as repository-local reference assets for Codex-style economics workflows.
- Treat this repository as a public workflow repository. Real private research projects should live in separate private workspaces under `D:\Desktop\科研相关\`.

## Public Workflow And Private Project Boundary

This repository should contain public workflow assets:

- reusable Stata pipeline code
- templates
- scripts
- agents and skills
- teaching demos
- non-sensitive simulations
- documentation

Real research projects should be created as separate folders under `D:\Desktop\科研相关\` using the naming pattern:

```text
YYYYMM关键词
```

Example:

```text
D:\Desktop\科研相关\202606数字化转型与企业创新
```

Each private project should keep its own data, logs, tables, figures, memos, drafts, and project-specific do-files. Use `templates/private-study-skeleton/` or `scripts/new_private_study.ps1` to create the workspace.

Default command:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/new_private_study.ps1 -Keyword "数字化转型与企业创新"
```

Use `-InitGit` when the user wants to initialize a private Git repository immediately:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/new_private_study.ps1 -Keyword "数字化转型与企业创新" -InitGit
```

Do not put confidential research assets, private data, unpublished paper drafts, or project-specific generated outputs into this public workflow repository unless the user explicitly says the material is public-safe.

Preferred skills for economics sessions:

- `research-ideation`
- `good-question`
- `results-analysis`
- `story-diagnostics`
- `paper-writing`
- `paper-self-review`
- `review-response`
- `qa-paper`
- `qa-response`
- `citation-verification`
- `post-acceptance`

Preferred agents for economics sessions:

- `literature-reviewer`
- `data-analyst`
- `theory-auditor`
- `paper-miner`
- `paper-critic`
- `paper-fixer`
- `rebuttal-writer`
- `response-critic`
- `response-fixer`
- `artifact-verifier`

Default memo and QA outputs:

- `results_memos/theory_audits/`
- `results_memos/story_diagnostics/`
- `quality_reports/papers/`
- `quality_reports/responses/`
- `quality_reports/verifier/`
- `quality_reports/specs/`
- `quality_reports/good_questions/`
- `quality_reports/checkpoints/`
- `quality_reports/decisions/`
- `quality_reports/preregistrations/`
- `quality_reports/passports/`

Useful governance templates now available under `templates/`:

- `requirements-spec.md`
- `good-question-card.md`
- `decision-record.md`
- `session-log.md`
- `passport-template.yaml`
- `preregistration-template.md`
- `response-to-referees.md`

## Sandbox and Pilot Workflow

- New methods, one-off simulations, and diagnostic tests should start in a private workspace under `D:\Desktop\科研相关\` rather than inside this public workflow repository.
- Public-safe teaching examples and simulations may be placed in dedicated repositories or subdirectories, but keep them outside the production `dofiles/` pipeline.
- Keep sandbox logs inside the corresponding workspace. Do not leave Stata console logs or run logs in the repository root.
- Promote a pilot to production only after it is stable, documented, quality-checked, and intentionally wired into `dofiles/00_master.do`.
- Cox proportional hazards / hazard-ratio examples use `stset`, `stcox, hr`, `estat phtest`, and graph export.

## Good Question Workflow

Use the repository-local `skills/good-question/` workflow before empirical execution when the user starts from a broad direction, literature gap, proposal sketch, or several possible ideas.

Good research questions should pass these checks:

- The answer would matter for theory, method, policy, practice, or next-step research.
- The question is specific enough for evidence to touch.
- Plausible rival explanations exist.
- Some result could weaken, revise, or falsify the idea.
- A credible pilot can start under the user's real constraints.
- A negative result would still teach a boundary, mechanism, or method lesson.
- If current field context matters, source-backed claims are separated from inference and unknowns.

Default output is a Good Question Card saved under `quality_reports/good_questions/` using `templates/good-question-card.md`.

When a user asks to evaluate a literature gap, proposal, or current field trend, first check whether a source audit or compact domain brief is needed. Do not state that a gap, consensus, or latest trend exists unless the claim is backed by sources or clearly marked as inference.

## Non-Negotiable Rules

- No numerical research claim without a source in `logs/*.log` or `output/tables/*`.
- Do not fabricate or infer coefficients, standard errors, p-values, sample sizes, or summary statistics.
- Do not commit or expose raw or derived datasets from `data/raw/` or `data/derived/`.
- Do not weaken `.gitignore` data-protection rules without explicit user confirmation.
- Use relative paths in Stata code. Avoid hardcoded machine-specific paths.
- Every substantive `.do` file should have `version`, `set more off`, `set varabbrev off`, logging, and a clear header.
- Write new or modified Stata do-file comments in Chinese unless the user requests another language.
- Keep reports downstream of pipeline outputs. Reports should consume `output/`, not become the primary analysis source.
- Do not edit protected files casually: `dofiles/00_master.do`, `.gitignore`, and bibliography files if added later.
- Do not put wildcard paths such as `output/tables/*` inside Stata block comments or header comments. Stata reads `/*` as the start of a block comment even when it appears inside a path, which can silently comment out the rest of a do-file. Prefer `output/tables/` in `.do` file headers.

## Commands

Run a single do-file:

```bash
bash scripts/run_stata.sh dofiles/03_analysis/main_regression.do
```

Run the full pipeline:

```bash
bash scripts/run_pipeline.sh
```

Render the report:

```bash
quarto render reports/analysis_report.qmd
```

Score an artifact:

```bash
python scripts/quality_score.py dofiles/03_analysis/main_regression.do
python scripts/quality_score.py reports/analysis_report.qmd
python scripts/quality_score.py scripts/check_data_safety.py
```

Check staged files for data leaks:

```bash
python scripts/check_data_safety.py --staged $(git diff --cached --name-only)
```

## Stata Conventions

- Local Stata is Stata 18: `D:\Program Files\Stata18\StataMP-64.exe`.
- Pin Stata do-files to `version 18` unless the user explicitly changes the project standard.
- Pin the Stata version at the top of each `.do` file.
- Use one project-wide seed unless a task has a documented reason to do otherwise.
- Open and close logs inside runnable do-files.
- For teaching, exploration, or user-facing do-files, prefer explicit commands over Stata macro indirection. Avoid unnecessary `` `local' `` macro use, especially in regression specifications. If a command must be easy to run line-by-line in the Do-file Editor, write the full control-variable list directly in the command rather than relying on a prior `local controls ...` line.
- Use local macros sparingly for stable paths or repeated filenames only when they materially improve readability. Do not hide key model choices, sample restrictions, or variable lists inside macros if that makes partial reruns fragile.
- Store estimation results with `estimates store` or `est store` when table assembly depends on them.
- Export figures with native Stata `graph export` as both `.pdf` and `.png`; do not keep `.gph` as a committed artifact.
- When generating a figure, always create both PDF and PNG outputs unless Stata itself cannot run.
- Use a muted Stata-style graph design by default: white or very light gray background, subtle horizontal gridlines only, solid blue marks or bars using RGB `"49 145 255"` / HEX `#3191FF`, no glossy or gradient-like effects, no strong contrast edges, Arial or default Stata Sans fonts, normal-weight dark blue-gray titles, modest axis/tick label sizes, and Stata-default-like proportions with enough whitespace.
- For survival curves, use the same graph style: white background, subtle horizontal gridlines, treatment or focal series in RGB `"49 145 255"` / HEX `#3191FF`, comparison series in muted blue-gray, restrained titles, and PDF plus PNG export. In Stata 15, `stcurve` has limited line-style options; use `sts graph, by(...)` when reliable per-line styling is needed.
- Prefer `esttab` outputs as `.tex` plus `.csv` for auditability.
- Cluster standard errors at the most defensible aggregate level and document the choice.
- For large CSV workflows, do not assume Stata can reliably import only selected columns across versions. If the source is too wide or slow, use a small reproducible Miniconda Python helper to stream selected columns into `data/derived/`, then have Stata read the narrow extract.
- For user replication convenience, produce an analysis-ready `.dta` in `data/derived/` when the workflow requires substantial merging or cleaning. Keep the `.dta` gitignored and document the command to regenerate it.
- Do not rely on Stata `shell` calls inside batch-mode do-files for required preprocessing. Run Python/R preprocessing explicitly before Stata, or fail with a clear message telling the user which helper command to run.
- When using variables with encoded categories, verify from the codebook whether values are true quantities or category codes. Do not treat education, occupation, or survey response codes as continuous measures unless the codebook confirms they are measured on a numeric scale.
- If a do-file includes numerical interpretation in comments, cite the generated log or output table in the comment and keep the numbers synchronized by rerunning the script after model changes.

## Local Environment

- Python is Anaconda, not the Microsoft Store Python.
- Miniconda root: `D:\ProgramFiles\anaconda3`.
- Conda executable: `D:\ProgramFiles\anaconda3\Scripts\conda.exe`.
- Python executable: `D:\ProgramFiles\anaconda3\python.exe`.
- Stata executable: `D:\Program Files\Stata18\StataMP-64.exe`.
- Prefer explicit executable paths if `python`, `conda`, or `stata` are not found on `PATH`.

## Log Verification

Before stating a numerical result:

1. Find the current log or output table.
2. Verify the value appears in that artifact.
3. Cite the artifact path and, when practical, the surrounding context or line.
4. If no current artifact exists, say that the do-file must be run first.

Use this response pattern when blocked:

```text
I cannot state that result because no fresh log or output table backs it. I need to run the relevant do-file first, or remove the numerical claim.
```

## Data Protection

Never add these to version control:

- `data/raw/**`, except `.gitkeep` and documentation.
- `data/derived/**`, except `.gitkeep` and documentation.
- Stata logs under `logs/`.
- Stata binary graphs `*.gph`.
- Data files such as `*.dta`, `*.sav`, `*.por`, `*.parquet`, `*.feather`, `*.csv`, `*.json`, and `*.jsonl`, except narrow whitelisted output/example paths.
- Raw-data-style spreadsheets such as `*.xls` and `*.xlsx`, except narrow whitelisted output/example paths.

Allowed committed outputs:

- `output/tables/*.csv`, `*.tex`, and other small non-PII summary tables.
- `output/figures/*.pdf`, `*.png`.
- Template/example fixtures only when intentionally whitelisted.

## Quality Gates

- `80/100`: acceptable for commit.
- `90/100`: PR-ready.
- `95/100`: excellence target.

Run `python scripts/quality_score.py <file>` before finalizing substantive edits to `.do`, `.qmd`, or user-facing Python scripts.

For sandbox and teaching analyses in private workspaces, the quality bar is relaxed, but they still need to be runnable and honest about limitations.

## Codex Workflow

- Inspect relevant files before editing.
- Prefer small, targeted patches.
- Preserve user changes and do not revert unrelated edits.
- Keep this repository usable by both Codex and Claude Code.
- If changing workflow rules, update `AGENTS.md` and any affected README section together.
- If changing Stata behavior, run the relevant wrapper when Stata is available; otherwise state exactly what was not verified.
- After running Stata batch jobs, check for root-level console transcripts and move them into the corresponding project's `logs/` folder with a `_console.log` suffix.
- When a user reports a mismatch between their Stata output and reported results, first check whether macros, partial do-file execution, sample filters, or stale derived files changed the actual specification.
- For a new project, default to this sequence unless the user asks otherwise: `research-ideation` or literature mapping, private workspace setup, Stata analysis, `results-analysis`, optional `theory-auditor`, then paper writing or QA.
- If the user's starting point is a rough topic, literature gap, or proposal idea, run the Good Question workflow before creating an exploration folder.
- If the user starts a real research project, create or use a private workspace under `D:\Desktop\科研相关\YYYYMM关键词` before writing project-specific inputs or outputs.
- For long or ambiguous tasks, write a short requirements spec first and save it under `quality_reports/specs/`.
- For major design choices such as sample definitions, core treatment coding, or identification changes, record an ADR-style note under `quality_reports/decisions/`.
- For manuscript projects with many numerical claims, maintain a passport file under `quality_reports/passports/` so tables and prose can be traced back to code and outputs.

## Legacy Claude Code Material

The `.claude/` directory contains richer rule, agent, and skill documentation. Codex should consult it when deeper guidance is needed, especially:

- `.claude/rules/log-verification-protocol.md`
- `.claude/rules/data-protection.md`
- `.claude/rules/quality-gates.md`
- `.claude/rules/stata-coding-conventions.md`
- `.claude/rules/stata-reproducibility-protocol.md`
- `.claude/skills/stata/SKILL.md`

Do not assume Claude-only commands such as `/run-stata` exist in Codex. Use the shell commands documented above.
