# Example Analysis Report

## Project

Tuition-free vocational-school expansion and youth employment

## Data Pipeline Summary

- administrative school-opening records matched to county-year labor outcomes
- county panel from 2010 to 2022
- estimation sample excludes counties with missing pre-policy labor outcomes

## Main Specification

- outcome: youth employment rate
- treatment: county exposed to tuition-free vocational-school expansion
- fixed effects: county and year
- controls: baseline demographics interacted with year where relevant
- clustered standard errors: county level

## Main Findings

1. The baseline estimate is positive and economically meaningful.
2. Event-time coefficients are flat before treatment and rise gradually after implementation.
3. The result is larger in counties with weak pre-policy secondary-school capacity.

## Immediate Interpretation Risks

- school expansion timing may coincide with broader county education spending
- employment effects may partly reflect migration rather than local placement

## Next Table Sequence

1. baseline event study
2. robustness to alternative cohorts and controls
3. heterogeneity by pre-policy school scarcity
4. mechanism table on local firm hiring or training participation

## Memo Trigger

Because the mechanism interpretation remains uncertain, pass the current result package to `theory-auditor` and save the memo in `results_memos/theory_audits/`.
