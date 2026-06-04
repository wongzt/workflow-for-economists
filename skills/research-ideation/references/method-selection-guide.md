# Method Selection Guide

Select the empirical method that matches the variation, data, and policy question.

## If Policy Timing Drives Variation

Consider:

- `DID`
- event study
- stacked designs if treatment timing is staggered

## If Treatment Is Endogenous

Consider:

- `IV`
- control-function approaches
- design changes that sharpen exogeneity

## If Assignment Uses A Threshold

Consider:

- sharp or fuzzy `RDD`
- local randomization checks

## If Observables Drive Selection

Consider:

- matching
- reweighting
- careful balance diagnostics

## Selection Rule

Pick the design that:

- matches the real source of variation
- has diagnosable assumptions
- can be explained clearly in the paper
