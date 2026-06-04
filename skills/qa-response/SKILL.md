---
name: qa-response
description: Use when the user wants a strict, adversarial QA loop for an economics referee response or R&R letter, including comment-coverage checks, traceability review, score-based quality gates, and iterative critic/fixer review before sending the response.
version: 0.1.0
---

# QA Response

Run a Codex-native critic/fixer/verifier loop for economics `response-letter.md` workflows.

## When To Use

Use this skill when the user wants:

- a final `R&R` response audit
- a coverage check for many referee comments
- a score or pass/fail verdict
- iterative critic/fixer review before sending the response

## Loop

```text
Pre-flight -> response-critic round 1 -> response-fixer round 1 -> artifact-verifier -> repeat if needed -> stop at APPROVED or 5 rounds
```

## Pre-flight

Before the loop starts, identify:

- referee comments
- current `response-letter.md`
- `comment-to-change-map.md`
- manuscript locations cited in the response

If comment-to-change traceability does not exist yet, create the minimal tracking structure before claiming QA coverage.

## Hard Gates

Fail the loop immediately if any of these remain unresolved:

- a key referee point is unanswered
- the response promises a manuscript change that is not traceable
- the letter and revision map disagree
- the tone is evasive or materially misleading

## Scoring Rubric

Score each category from `0-100`:

- completeness
- alignment to comments
- evidence and traceability
- tone
- revision mapping
- unresolved blockers

Thresholds:

- `80` = commit-ready
- `90` = submission-ready
- `95` = excellence

## Report Locations

- critic reports: `quality_reports/responses/*_critic_roundN.md`
- fixer reports: `quality_reports/responses/*_fixer_roundN.md`
- verifier reports: `quality_reports/verifier/*_response_verifier_roundN.md`

Use the templates in `quality_reports/templates/` when creating a new report.

## Expected Round Logic

1. `response-critic` produces issue list and provisional score
2. `response-fixer` updates the response and change map conservatively
3. `artifact-verifier` decides:
   - `APPROVED`
   - `CONTINUE`
   - `STOP_MAX_ROUNDS`

If `CONTINUE`, run another critic round focused on unresolved coverage or traceability failures.

## Final Output

Always provide:

- current verdict
- overall score
- hard-gate status
- top remaining blockers
- whether the response is `commit-ready`, `submission-ready`, or below threshold
