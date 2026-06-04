# Codex Stata for Economists

**A Codex Reproducible Workflow for Empirical Economics and Management Research**

**Last Updated:** 2026-06-04

---

## Positioning

This is a **public workflow repository** that stores reusable research processes, Stata pipelines, Codex configurations, agents, skills, templates, and quality management rules.

Real personal research projects should live in **separate private workspaces** and may be stored as private GitHub repositories.

Two cardinal rules:

- The public repository only stores workflow; real research assets belong in private project repositories.
- No numerical claim should be reported without a supporting log or output table.

---

## Why This Design

Empirical economics projects easily go off the rails: research questions are too broad, data and code are scattered, regression specifications go unrecorded, interpretation drifts away from the identification design, and numbers in the manuscript become untraceable.

This repository's core principles:

| Principle                       | Description                                                                                                   |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Question First**        | Verify that the research question matters, is specific, is falsifiable, and has a feasible pilot              |
| **Private Isolation**     | Each real research project gets its own private workspace and private GitHub repository                       |
| **Reproducible Pipeline** | Stata do-files, logs, tables, figures, and reports follow a fixed directory structure                         |
| **Log Verification**      | All coefficients, standard errors, sample sizes, and descriptive statistics must trace back to logs or tables |
| **Paper Continuity**      | Interpretation, theory diagnostics, paper QA, and R&R responses connect on the same evidence chain            |

---

## Public Workflow and Private Workspaces

Recommended structure: **one public workflow repository + one private repository per research project**.

```
./
├── workflow-for-economists/          ← Public workflow repository
│   ├── AGENTS.md                        ← Primary Codex rules
│   ├── skills/                          ← Reusable skill packages
│   ├── agents/                          ← Specialized agent configurations
│   ├── templates/                       ← Do-file, memo, and private project skeleton templates
│   ├── scripts/                         ← Execution scripts, quality checks, project creation
│   ├── dofiles/                         ← Public template pipeline
│   ├── quality_reports/                 ← Quality report templates
│   ├── reports/                         ← Quarto report templates
│   └── results_memos/                   ← Result interpretation memo templates
│
└── private-research/                    ← Private research workspace (example)
    ├── AGENTS.project.md                ← Project-specific rules
    ├── data/                            ← Raw and derived data
    ├── dofiles/                         ← Project do-files
    ├── logs/                            ← Stata logs
    ├── output/                          ← Output tables and figures
    ├── reports/                         ← Paper drafts and Quarto reports
    ├── quality_reports/                 ← Question cards, specs, decision records
    └── results_memos/                   ← Result interpretation memos
```

Real research projects use the naming pattern `YYYYMM + keyword`:

```
202606-digital-transformation-innovation
202608-platform-governance-worker-welfare
202612-minimum-wage-employment-structure
```

### What Goes into the Public Workflow Repository

- Reusable Stata pipeline code (`dofiles/`)
- Agent and skill definitions (`agents/`, `skills/`)
- Reusable templates (`templates/`)
- Quality rules and check scripts (`scripts/`)
- Workflow documentation free of sensitive information

### What Goes into Private Research Workspaces

- Raw and derived data (`data/`)
- Project do-files (`dofiles/`)
- Stata logs (`logs/`)
- Output tables and figures (`output/`)
- Good Question Cards (`quality_reports/good_questions/`)
- Requirements specs (`quality_reports/specs/`)
- Result interpretation memos (`results_memos/`)
- Paper drafts and referee responses (`reports/`)

> **Note:** If a data license, ethics review, or institutional rule forbids uploading data to GitHub, do not commit the data even to a private repository. Use encrypted storage, institutional servers, Git LFS, DVC, or another compliant system, and document the reproduction path in `data/README.md`.

---

## Quick Start

### Step 1: Obtain the Workflow Repository

```bash
git clone https://github.com/YOUR_USERNAME/workflow-for-economists.git
cd workflow-for-economists
```

### Step 2: Create a Private Research Workspace

Run from the workflow repository root:

```powershell
# Create the project directory
powershell -ExecutionPolicy Bypass -File scripts/new_private_study.ps1 -Keyword "digital-transformation-innovation"

# Create with Git initialization
powershell -ExecutionPolicy Bypass -File scripts/new_private_study.ps1 -Keyword "digital-transformation-innovation" -InitGit
```

This creates:

```
D:\Desktop\科研相关\202606-digital-transformation-innovation/
```

### Step 3: Start Codex inside the Private Workspace

```powershell
cd "D:\Desktop\科研相关\202606-digital-transformation-innovation"
codex
```

Example first prompt:

```text
Please treat the current directory as a private empirical economics research project.
The public workflow repository is at:
D:\Desktop\科研相关\workflow-for-economists

Please read this project's AGENTS.project.md and the workflow repository's AGENTS.md.
My research direction is digital transformation and firm innovation.
I do not yet have a sharp research question.

Please first use the good-question workflow to generate 2-3 Good Question Cards.
Compare each question's importance, feasibility, rival explanations, falsifiability, and two-week pilot.
Do not start writing Stata code yet. Help me decide which question is worth pursuing.
```

---

## Complete Research Workflow

This workflow moves an empirical economics project from a "vague idea" to a "reproducible, auditable, paper-ready" state:

```
Good Question → Private Research Workspace → Requirements Spec → Data Audit
    → Stata Cleaning and Analysis → Log Verification → Result Interpretation and Theory Diagnostics
    → Paper Writing / QA / Referee Response
```

---

### Stage 1: Sharpen the Research Question

**When to use:** You have only a broad direction, a literature gap, a proposal abstract, or several ideas all seeming viable.

**Output location:** `quality_reports/good_questions/`

**Basic prompt:**

```text
Please use the good-question workflow.
My rough idea is: [write your idea]

Please generate a Good Question Card and check:
1. Why the question matters
2. What default assumption it challenges
3. At least two rival explanations
4. What evidence can distinguish those explanations
5. What result would falsify or weaken it
6. What a feasible two-week pilot looks like
7. Whether it is worth entering the Stata empirical stage
```

**Literature gap scenario:**

```text
Please use good-question to evaluate whether this literature gap is worth pursuing:
[gap description]

Do not accept my gap at face value.
Separate source-backed evidence, reasonable inference, and unknowns.
If a source audit is needed, list the papers and claims that must be checked.
```

**Proposal stress test:**

```text
Please use good-question as a strict reviewer to stress-test this proposal abstract:
[proposal abstract]

Please output:
1. The most likely reason for desk rejection
2. The strongest reviewer objection
3. What needs theoretical rewriting
4. What needs data or identification strategy reinforcement
5. A repaired core research question
```

---

### Stage 2: Define the Task Boundary

**When to use:** The task scope is unclear. Write a requirements spec before writing code.

**Output location:** `quality_reports/specs/`

```text
Please do not write code yet.
Based on my research question and data situation, generate a requirements spec under quality_reports/specs/.

Separate into:
MUST: required in this round
SHOULD: preferred
MAY: optional if time permits
BLOCKED: questions that require my confirmation
```

---

### Stage 3: Audit Data and Variables

**When to use:** You have data but need to understand variable quality, sample structure, missingness, and feasible specifications.

```text
The data are in data/raw/.
Please run a data audit first; do not jump to regression.

Please:
1. Identify data format and variable list
2. Check sample size, time span, and panel or cross-sectional structure
3. Check core variable missingness and outliers
4. Identify category-coded variables that should not be treated as continuous
5. Generate data-audit.md and an initial variable dictionary
6. Recommend next steps for cleaning and construction
```

---

### Stage 4: Stata Cleaning, Construction, and Analysis

Formal do-files follow this structure:

```
dofiles/01_clean/      ← Raw data cleaning
dofiles/02_construct/  ← Variable construction and sample filtering
dofiles/03_analysis/   ← Descriptive statistics, baseline regression, robustness
dofiles/04_output/     ← Table and figure assembly
```

**Basic analysis prompt:**

```text
Please write the first Stata analysis workflow based on data-audit.md and the requirements spec.

Requirements:
1. Create or update do-files under dofiles/
2. Use Chinese comments
3. Use relative paths
4. Open and close logs in each runnable do-file
5. Output descriptive statistics tables, key figures, and baseline regression tables
6. Export figures as both png and pdf
7. Save tables to output/tables/
8. Save logs to logs/
9. Inspect the log after execution; do not report numbers without log support
```

**DID / Event Study scenario:**

```text
Please design a DID / event study analysis.

First confirm:
1. What is the unit dimension
2. What is the time dimension
3. How treatment is defined
4. Whether adoption is staggered
5. At which level to cluster standard errors
6. How to run pre-trend and placebo checks

Then write the Stata do-file and export the event study table and figure.
```

**IV scenario:**

```text
Please design an IV regression.

First write down:
1. The endogenous variable
2. The instrument
3. The economic reasoning for the exclusion restriction
4. How to report the first stage
5. How to check weak-instrument risk
6. How to organize the table into panels

Only after confirmation, write the Stata do-file.
```

---

### Stage 5: Log Verification and Result Interpretation

All numerical interpretation must be based solely on `logs/` and `output/tables/`.

**Result interpretation prompt:**

```text
Please run results-analysis using the latest logs/ and output/tables/.

Requirements:
1. Recover each regression specification column by column
2. Explain sample, controls, fixed effects, and clustering level
3. Interpret only numbers that can be found in logs or tables
4. Flag potential identification threats
5. Propose a next-step checklist for robustness, heterogeneity, and mechanisms
6. Generate a result interpretation memo under results_memos/
```

**Diagnostic prompt for unstable results:**

```text
The current results are unstable.
Please use story-diagnostics to judge whether:
1. The theoretical story is unsupported
2. Measurement or variable construction is the problem
3. The sample or identification strategy is the problem
4. The current data are insufficient

Please return one of: STORY_READY, CREDIBLE_NULL, ITERATE_WITH_CURRENT_DATA, or NEW_DATA_REQUIRED.
```

---

### Stage 6: Paper Writing and QA

Move into writing only after tables and logs are stable.

**Writing prompt:**

```text
Please use the paper-writing workflow.
Based on output/tables/, output/figures/, and results_memos/, draft the Main Results section.

Requirements:
1. Tie every numerical claim to a corresponding table or figure
2. Do not overstate mechanism evidence
3. Separate main effects, robustness, heterogeneity, and mechanisms
4. Flag points that cannot yet be stated definitively
```

**Pre-submission QA prompt:**

```text
Please use the qa-paper workflow to run a pre-submission check on the current manuscript draft.

Focus on:
1. Whether the research question is clear
2. Whether the identification strategy is coherent
3. Whether manuscript numbers match tables
4. Whether figure and table notes are complete
5. Whether data and code availability statements are sufficient
6. Which issues would cause a hard gate failure
```

**R&R response prompt:**

```text
Please use the review-response workflow.
I will provide referee comments and revised results.

Please generate:
1. A comment-to-change map
2. A draft response letter
3. The manuscript location for each change
4. Items that are not actually completed and should not be promised
```

---

## Repository Structure

```
./
├── AGENTS.md                       ← Primary Codex rules
├── CLAUDE.md                       ← Claude Code compatibility notes
├── MEMORY.md                       ← Repository-level memory and context
├── config.codex-econ.example.toml  ← Codex configuration example
│
├── agents/                         ← Specialized agent definitions (paper critic, data audit, rebuttal, etc.)
│   ├── data-analyst/               ← Data analysis agent
│   ├── paper-critic/               ← Paper review agent
│   ├── rebuttal-writer/            ← Rebuttal writing agent
│   ├── theory-auditor/             ← Theory audit agent
│   └── ...
│
├── skills/                         ← Reusable skill packages (good-question, results-analysis, etc.)
│
├── templates/                      ← Template files
│   ├── master-do-template.do        ← Do-file template
│   ├── did-analysis-template.do     ← DID analysis template
│   ├── ddml-analysis-template.do    ← DDML analysis template
│   ├── good-question-card.md        ← Good Question Card template
│   ├── requirements-spec.md         ← Requirements Spec template
│   ├── response-to-referees.md      ← Referee response template
│   ├── ...                          ← More templates
│   └── private-study-skeleton/      ← Private project skeleton template
│
├── scripts/                        ← Execution, check, and project creation scripts
│   ├── new_private_study.ps1       ← Create a private research project
│   ├── run_pipeline.sh             ← Run the full Stata pipeline
│   ├── run_stata.sh                ← Run a single do-file
│   ├── check_data_safety.py        ← Data safety check
│   └── quality_score.py            ← Quality scoring
│
├── dofiles/                        ← Public template Stata pipeline
│   ├── 00_master.do                ← Main entry point
│   ├── 01_clean/                   ← Data cleaning
│   ├── 02_construct/               ← Variable construction
│   ├── 03_analysis/                ← Analysis and estimation
│   └── 04_output/                  ← Output assembly
│
├── quality_reports/                ← Quality report templates and references
│   ├── good_questions/             ← Good Question Card templates
│   ├── specs/                      ← Requirements spec templates
│   ├── decisions/                  ← Research decision records
│   └── passports/                  ← Numerical claim traceability passports
│
├── reports/                        ← Quarto report templates
├── results_memos/                  ← Result interpretation memo templates
├── master_supporting_docs/         ← Supporting documents and images
│
├── data/                           ← Public demo entry point (real data should not live here)
├── logs/                           ← Public demo logs (real logs should not live here)
└── output/                         ← Public demo outputs
```

---

## Common Commands

### Project Creation

```powershell
powershell -ExecutionPolicy Bypass -File scripts/new_private_study.ps1 -Keyword "keyword" -InitGit
```

### Stata Execution

```bash
# Run a single do-file
bash scripts/run_stata.sh dofiles/03_analysis/main_regression.do

# Run the full pipeline
bash scripts/run_pipeline.sh
```

### Report Rendering

```bash
quarto render reports/analysis_report.qmd
```

### Quality Checks

```bash
# Data safety check
python scripts/check_data_safety.py --staged $(git diff --cached --name-only)

# Artifact quality scoring
python scripts/quality_score.py dofiles/03_analysis/main_regression.do
python scripts/quality_score.py reports/analysis_report.qmd
```

---

## Stata Conventions

- Pin `version` at the top of each do-file
- Use `set more off`
- Use `set varabbrev off`
- Use relative paths
- Open logs in every runnable do-file
- Set a unified seed for random procedures
- Use `estimates store` or `est store` before table assembly
- Export figures as both `.pdf` and `.png`
- Prefer `.tex` and `.csv` for table output
- Write new or modified Stata comments in Chinese by default
- Cluster standard errors at the most defensible level and document the reasoning in table notes or memos

---

## Available Workspace Resources

Components that Codex can directly invoke within this repository are organized into three layers:

### Layer 1: Skills

Skills are task-specific, encapsulated capabilities. Codex automatically loads the full instructions of a skill during a conversation. Core skills include:

| Skill                     | Purpose                                         |
| ------------------------- | ----------------------------------------------- |
| `good-question`         | Generate and evaluate research question cards   |
| `research-ideation`     | Research ideation and empirical strategy design |
| `results-analysis`      | Interpret results based on logs and tables      |
| `story-diagnostics`     | Diagnose causes of unstable results             |
| `paper-writing`         | Draft paper sections from templates             |
| `paper-self-review`     | Self-review and consistency check               |
| `qa-paper`              | Pre-submission quality audit                    |
| `review-response`       | R&R referee response                            |
| `qa-response`           | Response letter QA                              |
| `citation-verification` | Citation and reference verification             |
| `post-acceptance`       | Post-acceptance tasks                           |

### Layer 2: Agents

Agents are role-specific proxies invoked as sub-agents via the `Task` tool, ideal for tasks requiring independent context and repeated iterations:

| Agent                   | Role                                                       |
| ----------------------- | ---------------------------------------------------------- |
| `data-analyst`        | Data cleaning, auditing, and variable construction         |
| `literature-reviewer` | Literature search and gap analysis                         |
| `theory-auditor`      | Audit theoretical frameworks and identification strategies |
| `paper-miner`         | Extract writing patterns from papers                       |
| `paper-critic`        | Internal paper review and stress testing                   |
| `paper-fixer`         | Revise papers based on critical feedback                   |
| `rebuttal-writer`     | Draft referee response letters                             |
| `response-critic`     | Review response letters                                    |
| `response-fixer`      | Fix issues identified in response reviews                  |
| `artifact-verifier`   | Final artifact verification and gate checks                |

### Layer 3: Templates

The `templates/` directory provides ready-to-use skeleton files:

- Stata do-file templates (standard header, log setup, section organization)
- Memo templates (data audit memo, result interpretation memo)
- Private project skeleton (complete directory structure and `AGENTS.project.md` template)

---

## Data and Privacy Rules

### Public Workflow Repository — Never Commit

```
data/raw/**        data/derived/**        logs/**
*.log              *.smcl                 *.gph
*.dta              *.sav                  *.parquet
*.csv              *.json                 *.xls
*.xlsx
```

### Private Research Repository — Cautions

- Exclude secrets and tokens
- Exclude personal account configuration
- Exclude temporary caches
- Exclude restricted data that cannot be uploaded to GitHub
- For large data, consider Git LFS or DVC, and document the reproduction procedure in `data/README.md`

---

## Local Environment

The current project guide records the following local environment:

```
Python: D:\ProgramFiles\anaconda3\python.exe
Conda:  D:\ProgramFiles\anaconda3\Scripts\conda.exe
Stata:  D:\Program Files\Stata18\StataMP-64.exe
```

If your machine uses different paths, update local configuration or project notes accordingly, but do-files should still use relative paths.

---

## Acknowledgments

This repository began as a reproducible Stata workflow for economics and management education and empirical research. It has progressively integrated Codex-first operation, Claude Code compatibility, economics paper QA, Good Question research-question sharpening, and private research workspace management.

---

## License

MIT
