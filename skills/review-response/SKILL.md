---
name: review-response
description: Use when the user asks to respond to referee comments, draft an economics journal revision memo, prepare an R&R response letter, map comments to manuscript changes, or analyze reviewer concerns about identification, robustness, mechanism, exposition, or data construction.
version: 0.3.1
---

# Review Response for Economics Journals

Treat this workflow as a journal `referee response / R&R` process by default.

If the user asks for a strict final check, wants an adversarial review loop, or needs a score-based readiness decision before sending the response, route to `../qa-response/SKILL.md`.

## Default Outputs

- `response-letter.md`
- `comment-to-change-map.md`

## Core Workflow

```text
Parse referee comments -> Classify issue type -> Decide response stance -> Map each comment to manuscript changes -> Draft response letter -> Check tone and consistency
```

## Comment Categories

- identification
- robustness
- mechanism
- external validity
- data construction
- exposition
- literature positioning
- formatting or minor edits

## Response Stances

- `accept and revise`
- `clarify existing logic`
- `partially accommodate`
- `decline with justification`

## Required Structure For Each Comment

1. short acknowledgement
2. substantive reply
3. manuscript action taken
4. location of the change
5. appendix or robustness addition when relevant

## Economics Defaults

- prioritize credibility and transparency over flourish
- explain new robustness checks in relation to the identifying assumption
- if a request cannot be met because of data limits, say what was attempted and what remains infeasible
- if a comment reflects misunderstanding, improve the paper text rather than only defending it in the letter

## References To Load On Demand

- `references/referee-response-patterns.md`
- `references/review-classification.md`
- `references/response-strategies.md`
- `references/tone-guidelines.md`

## Escalation Rule

Escalate to `qa-response` when:

- the draft is near-final and the user wants a go/no-go judgment
- there are many referee comments and traceability is hard to track manually
- the user wants critic/fixer iteration instead of a one-pass edit
- the task requires hard gates, scores, or remaining-blocker reporting
