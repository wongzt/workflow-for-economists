---
name: paper-self-review
description: Use when the user asks for a pre-submission review of an empirical economics paper, wants to check identification logic, regression tables, appendix consistency, data/code reproducibility, or asks for a systematic self-review before journal submission or R&R resubmission.
version: 0.3.0
---

# Paper Self-Review for Empirical Economics

Use this skill as a quality gate before submission, advisor review, or R&R resubmission.

If the user asks for a strict audit, adversarial review, submission-readiness judgment, score-based decision, or explicitly wants a multi-round review/fix loop, route to `../qa-paper/SKILL.md` instead of doing only a static checklist.

## Core Checklist

```text
Empirical Economics Self-Review
- [ ] Research question and identification strategy match
- [ ] Sample selection is traceable from raw data to estimation sample
- [ ] Treatment, outcome, and control variables are defined consistently
- [ ] Fixed effects and standard error choices are justified
- [ ] Main tables, appendix tables, and text use the same sample and variable definitions
- [ ] Mechanism and heterogeneity claims do not outrun the evidence
- [ ] Citations are verified and literature positioning is accurate
- [ ] Data/code/README are sufficient for replication or restrictions are clearly disclosed
```

## What to Review

### 1. Identification Logic

Check whether:

- the paper states the identifying variation clearly
- threats to identification are acknowledged
- robustness checks actually target those threats
- the interpretation matches the design

### 2. Data and Sample Transparency

Check whether:

- sample restrictions are explicit
- merge logic and attrition are documented
- descriptive statistics match the stated sample
- appendix notes explain unusual coding decisions

### 3. Regression and Table Integrity

Check whether:

- tables use consistent coefficient labels
- clustering and FE choices are stable and justified
- significance stars, notes, and units are consistent
- text descriptions match the sign, magnitude, and precision in tables

### 4. Writing Discipline

Check whether:

- the introduction promises only what the design can support
- the results section interprets economic magnitudes correctly
- mechanism evidence is not overstated
- the appendix absorbs supporting material without hiding critical design details

### 5. Reproducibility

Check whether:

- do-files run in a documented order
- intermediate outputs are named consistently
- logs exist for major steps
- README explains dependencies, restricted data, and expected outputs

## Review Output

Prefer a structured review with:

- major risks
- moderate issues
- quick fixes
- a short submit / do-not-submit recommendation

If the paper is not ready, say exactly what blocks submission.

## Escalation Rule

Escalate to `qa-paper` when any of these are true:

- the user asks whether the draft is submission-ready
- the paper has multiple tables/appendices and consistency risk is material
- the user wants iterative critic/fixer review
- the task requires a score or pass/fail quality gate
