---
name: results-analysis
description: Use when the user asks to analyze empirical economics results, inspect Stata outputs, design regressions, build robustness checks, interpret regression tables, or connect data artifacts to paper writing.
version: 0.3.0
---

# Results Analysis for Empirical Economics

Use this skill for empirical analysis after the research design is in place. Default to `Stata`-first workflows and economics-paper outputs.

## Core Workflow

```text
Raw data audit -> Cleaning and merge -> Sample construction -> Variable definitions -> Main regression -> Robustness -> Heterogeneity or mechanisms -> Theory audit -> Table and figure export -> Replication check
```

## Required Outputs

- `analysis-plan.md`
- `regression-spec-matrix.md`
- `table-shells.md`
- `replication-checklist.md`

Use `theory-auditor` when new core results require a disciplined interpretation memo.

## Working Rules

- establish the sample and variable logic before telling a story about coefficients
- map each table to its exact specification
- keep robustness checks tied to identification threats
- separate main effects from mechanism exercises
- if interpretation is unsettled, save a memo under `results_memos/theory_audits/`

## References To Load On Demand

- `references/stata-workflow.md`
- `references/empirical-checklist.md`
- `references/regression-table-conventions.md`
- `references/robustness-patterns.md`
- `references/results-writing-guide.md`
- `references/common-pitfalls.md`
