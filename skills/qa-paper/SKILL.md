---
name: qa-paper
description: Use when the user wants a strict, adversarial QA loop for an empirical economics paper draft, a submission-readiness decision, score-based quality gates, or iterative critic/fixer review before advisor sharing, journal submission, or R&R resubmission.
version: 0.1.0
---

# QA Paper

Run a Codex-native critic/fixer/verifier loop for empirical economics manuscripts.

## When To Use

Use this skill when the user wants:

- a harsh pre-submission review
- a go/no-go decision
- a numeric score
- multiple review-fix rounds
- hard-gate enforcement for identification, tables, citations, and replication

## Loop

```text
Pre-flight -> paper-critic round 1 -> paper-fixer round 1 -> artifact-verifier -> repeat if needed -> stop at APPROVED or 5 rounds
```

## Pre-flight

Before the loop starts, identify:

- manuscript source files
- tables/figures/appendices referenced in the draft
- replication materials or README
- whether citations can be checked from available artifacts

If the draft is too incomplete for adversarial QA, say so and produce a scoped pre-flight note instead of pretending the loop ran cleanly.

## Hard Gates

Fail the loop immediately if any of these remain unresolved:

- identification logic error
- text/table mismatch on a headline result
- unverifiable or distorted citation
- missing replication note for a claim that depends on code/data workflow

## Scoring Rubric

Score each category from `0-100`:

- identification
- econometrics
- data transparency
- literature accuracy
- writing clarity
- appendix/replication readiness

Thresholds:

- `80` = commit-ready
- `90` = submission-ready
- `95` = excellence

## Report Locations

- critic reports: `quality_reports/papers/*_critic_roundN.md`
- fixer reports: `quality_reports/papers/*_fixer_roundN.md`
- verifier reports: `quality_reports/verifier/*_paper_verifier_roundN.md`

Use the templates in `quality_reports/templates/` when creating a new report.

## Expected Round Logic

1. `paper-critic` produces issue list and provisional score
2. `paper-fixer` addresses issues conservatively
3. `artifact-verifier` decides:
   - `APPROVED`
   - `CONTINUE`
   - `STOP_MAX_ROUNDS`

If `CONTINUE`, run another critic round focused on unresolved items.

## Final Output

Always provide:

- current verdict
- overall score
- hard-gate status
- top remaining blockers
- whether the draft is `commit-ready`, `submission-ready`, or below threshold
