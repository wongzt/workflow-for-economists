---
name: story-diagnostics
description: Use when empirical results do not yet support a credible economics story, when theory and estimates do not line up cleanly, or when the user wants a disciplined memo on what to run next and when to stop.
version: 0.1.0
---

# Story Diagnostics for Empirical Economics

Use this skill as an explicit opt-in workflow when the current evidence is real but the interpretation is unsettled.

## When To Use

Use this skill when the user says things like:

- "I do not have a story yet."
- "These estimates do not line up with theory."
- "What should I run next?"
- "Tell me whether this is a credible null or just unfinished work."

## Inputs

- baseline regression tables
- identification notes
- variable-construction notes
- mechanism or heterogeneity results, if any
- relevant institutional background

## Outputs

- `results_memos/story_diagnostics/*_roundN.md`

Each memo should end with one of four outcomes:

- `STORY_READY`
- `CREDIBLE_NULL`
- `ITERATE_WITH_CURRENT_DATA`
- `NEW_DATA_REQUIRED`

## Strict Loop

```text
diagnose current evidence -> theory audit -> bounded next-step slate -> rerun only defensible checks -> memo verdict
```

## Round Rules

- default maximum is `3` rounds unless the user explicitly overrides it
- each round must propose a bounded next-step slate, not an open-ended fishing list
- every proposed step must tie to theory, design, measurement, or sample definition
- stop early if only opportunistic specification searches remain
- a credible null or theory-challenging result is an acceptable endpoint

## Required Memo Sections

1. `Current Result State`
2. `Why The Story Is Not Yet Locked`
3. `Most Credible Explanations`
4. `Next Defensible Checks`
5. `What Not To Run`
6. `What New Data Would Change The Assessment`
7. `Verdict`

## Default Escalation Path

1. use `results-analysis` to recover the specification and sample logic
2. use `theory-auditor` to test interpretation against economics theory
3. write a memo under `results_memos/story_diagnostics/`

## Stop Conditions

Stop with:

- `STORY_READY` when the design, estimates, and interpretation fit together cleanly
- `CREDIBLE_NULL` when the best reading is that the effect is absent, too small, or theoretically unpersuasive
- `ITERATE_WITH_CURRENT_DATA` when one more bounded round is justified
- `NEW_DATA_REQUIRED` when stronger interpretation depends on variables, institutional detail, or outcomes not currently observed
