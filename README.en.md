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

Real research projects use the naming pattern `YYYYMM + keyword`, like:

```
202606-digital-transformation-innovation
202608-platform-governance-worker-welfare
202612-minimum-wage-employment-structure
```

### What Goes into the Public Workflow Repository

- Stata pipeline templates (`dofiles/`)
- Agent and skill definitions (`agents/`, `skills/`)
- Reusable templates (`templates/`)
- Quality rules and check scripts (`scripts/`)
- Workflow documentation (`AGENTS.md`, `README.md`, etc.)

> **Note:** The public repository does NOT contain `data/`, `logs/`, or `output/` directories. These are created and used only in private research workspaces.

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
~/research/202606-digital-transformation-innovation/
```

### Step 3: Start Codex inside the Private Workspace

**Option A: Open the private project as workspace (recommended)**

```powershell
cd "~/research/202606-digital-transformation-innovation"
codex
```

**Option B: Use the research root directory as workspace**

Open `~/research/` in VS Code. All sub-projects are visible in one window. Specify the current project in your messages:

```text
Current project: 202606-digital-transformation-innovation
Please read workflow-for-economists/AGENTS.md.
```

> If you prefer the root-directory approach, consider placing a lightweight `AGENTS.md` at `~/research/AGENTS.md` as a workspace entry point for Codex.

Example first prompt (when using a private project as workspace):

```text
Please treat the current directory as a private empirical economics research project.
The public workflow repository is at:
~/research/workflow-for-economists

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
├── agents/                         ← Specialized agent definitions
│   ├── data-analyst/
│   ├── literature-reviewer/
│   ├── theory-auditor/
│   ├── paper-miner/
│   ├── paper-critic/
│   ├── paper-fixer/
│   ├── rebuttal-writer/
│   ├── response-critic/
│   ├── response-fixer/
│   └── artifact-verifier/
│
├── skills/                         ← Reusable skill packages
│   ├── good-question/
│   ├── research-ideation/
│   ├── results-analysis/
│   ├── story-diagnostics/
│   ├── paper-writing/
│   ├── paper-self-review/
│   ├── qa-paper/
│   ├── review-response/
│   ├── qa-response/
│   ├── citation-verification/
│   └── post-acceptance/
│
├── templates/                      ← Template files
│   ├── master-do-template.do
│   ├── did-analysis-template.do
│   ├── ddml-analysis-template.do
│   ├── good-question-card.md
│   ├── requirements-spec.md
│   ├── response-to-referees.md
│   ├── ...
│   └── private-study-skeleton/
│
├── scripts/                        ← Execution, check, and project creation scripts
│   ├── new_private_study.ps1
│   ├── run_pipeline.sh
│   ├── run_stata.sh
│   ├── check_data_safety.py
│   └── quality_score.py
│
├── dofiles/                        ← Stata pipeline templates
│   ├── 00_master.do                ← Main entry point
│   └── README.md
│
├── quality_reports/                ← Quality report templates and references
│   ├── good_questions/
│   ├── specs/
│   ├── decisions/
│   └── passports/
│
├── reports/                        ← Quarto report templates
├── results_memos/                  ← Result interpretation memo templates
└── master_supporting_docs/         ← Supporting documents and images
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

The Codex components in this repository are organized around the complete lifecycle of an empirical economics research project, divided into Skills and Agents, each covering different stages.

### Workflow Overview

```
Ideation ──→ Data Analysis ──→ Interpretation ──→ Writing ──→ QA ──→ R&R ──→ Post-Acceptance
    │              │                │                │           │        │           │
    ▼              ▼                ▼                ▼           ▼        ▼           ▼
 ideation    data-analyst    results-analysis   paper-      qa-paper  review-    post-
 good-       (agent)         story-             writing     qa-       response   acceptance
 question                    diagnostics        paper-      response  rebuttal-
 lit-                                           self-review            writer
 reviewer                                                             response-
 (agent)                                                              critic/fixer
                                                                      artifact-
                                                                      verifier
                                              citation-verification (cross-cutting)
```

### Skills

Skills are organized by workflow stage. Codex automatically loads the appropriate skill during conversations:

| Stage                     | Skill                     | Description                                                                                                                                                                                                                         |
| ------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ideation**        | `research-ideation`     | Problem framing → literature map → identification strategy → data feasibility. Produces `literature-review.md` and `identification-map.md` before any code is written                                                        |
|                           | `good-question`         | Transforms vague ideas into falsifiable scientific questions. Generates Good Question Cards evaluating importance, rival explanations, falsifiability, and two-week pilots                                                          |
| **Data Analysis**   | `results-analysis`      | Complete Stata-first analysis: raw data audit → cleaning → sample construction → variable definition → main regression → robustness → heterogeneity/mechanisms → theory audit → output → replication check                 |
|                           | `story-diagnostics`     | Diagnoses when empirical results are unstable or don't support the expected story. Returns STORY_READY / CREDIBLE_NULL / ITERATE / NEW_DATA_REQUIRED                                                                                |
| **Writing**         | `paper-writing`         | Drafts standard empirical economics paper structure: Introduction → Institutional Background → Data → Empirical Strategy → Main Results → Mechanisms/Heterogeneity. Every numerical claim tied to a specific table or figure   |
|                           | `paper-self-review`     | Pre-submission or pre-advisor quality gate. Checks: question-design alignment, sample traceability, variable definition consistency, fixed effects and clustering choices                                                           |
| **QA**              | `qa-paper`              | Rigorous paper QA cycle: critic → fixer → verifier. Checks identification credibility, table-number consistency, citation fidelity, and replication readiness. Used for pre-submission go/no-go decisions                         |
|                           | `qa-response`           | Response letter QA cycle. Checks comment coverage, change traceability, and tone. Ensures every reviewer comment has a corresponding response                                                                                       |
| **R&R**             | `review-response`       | Complete R&R workflow: classify referee comments (identification, robustness, mechanisms, external validity, literature positioning), draft response letter, map each comment to manuscript changes or reasoned non-changes         |
| **Post-Acceptance** | `post-acceptance`       | Post-acceptance tasks: replication package cleanup, appendix finalization, data/code availability statements, journal-format figure checklists, seminar slides, policy briefs                                                       |
| **Cross-Cutting**   | `citation-verification` | Citation verification: distinguishes working papers from published versions, checks journal metadata and DOIs, prevents fabricated citations. Source priority: publisher page > top journal site > NBER/RePEc/SSRN > Google Scholar |

### Agents

Agents are organized by role, invoked as sub-agents via the `Task` tool, ideal for tasks requiring independent context and repeated iterations:

| Stage                    | Agent                   | Role & Responsibilities                                                                                                                                                                                                                                                                              |
| ------------------------ | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ideation**       | `literature-reviewer` | Literature review specialist. Groups papers by research question, identification strategy, data source, and findings. Identifies disagreements, credibility gaps, and open empirical opportunities. Uses Zotero as default citation backbone                                                         |
| **Data Analysis**  | `data-analyst`        | Stata-first empirical analysis expert. Translates identification designs into executable analysis plans, builds regression specification matrices, robustness plans, and table frameworks. Triggers or recommends `theory-auditor`                                                                 |
| **Interpretation** | `theory-auditor`      | Theory-facing interpretation auditor. Tests whether current interpretations are consistent with economic theory and whether rival mechanisms remain alive. Produces structured memo: result summary → theory fit → rival mechanisms → interpretation risks → next empirical steps                |
| **Writing**        | `paper-miner`         | Writing pattern miner. Extracts reusable patterns from published papers and review materials (introduction frameworks, institutional context descriptions, data descriptions, empirical strategy language), updating reference files used by writing skills                                          |
| **QA**             | `paper-critic`        | Read-only critic performing adversarial paper review. Review dimensions: argument structure, identification credibility, econometric specification, literature positioning, writing/presentation norms, replication readiness. Assumes manuscript is below submission standard until hard gates pass |
|                          | `paper-fixer`         | Executor that fixes issues identified by `paper-critic` in CRITICAL → MAJOR → MINOR order without expanding scope                                                                                                                                                                                |
|                          | `artifact-verifier`   | Final verifier. Checks hard gates, scores against rubric, declares APPROVED or CONTINUE. Approves only when hard gates pass and score ≥ 90                                                                                                                                                          |
| **R&R**            | `rebuttal-writer`     | Journal revision specialist. Classifies referee comments, selects appropriate response stance, drafts professional response letters, maintains comment-change-response traceability                                                                                                                  |
|                          | `response-critic`     | Read-only critic for adversarial review of response letters. Checks comment coverage, stance quality, change traceability, evidence sufficiency, and tone                                                                                                                                            |
|                          | `response-fixer`      | Executor that fixes issues identified by `response-critic` in CRITICAL → MAJOR → MINOR order while preserving traceability                                                                                                                                                                       |

### Templates

The `templates/` directory provides ready-to-use skeleton files:

- **Stata do-file templates**: `master-do-template.do` (standard header, logging, stage organization), `did-analysis-template.do` (TWFE DID / Callaway-Sant'Anna), `ddml-analysis-template.do` (DDML double machine learning)
- **Memo templates**: `good-question-card.md`, `requirements-spec.md`, `decision-record.md`, `session-log.md`, `passport-template.yaml`
- **Paper templates**: `response-to-referees.md` (review response), `preregistration-template.md`
- **Private project skeleton**: `private-study-skeleton/` (complete directory structure and `AGENTS.project.md` template)

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

This workflow draws on the following excellent projects:

- [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) — Claude Code workflow management and project organization paradigms
- [maxwell2732/codex-stata-for-economists](https://github.com/maxwell2732/codex-stata-for-economists) — Reproducible Stata research workflow for economics and management with Codex
- [Rimagination/good-question](https://github.com/Rimagination/good-question) — Good Question Card methodology for research question sharpening

It has progressively integrated Codex-first operation, Claude Code compatibility, economics paper QA, research question sharpening, and private research workspace management.

---

## License

MIT
