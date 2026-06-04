# Identification Strategy Guide

Choose the design that matches the available variation, not the one that sounds most prestigious.

## Common Designs

- `DID` and event study for staggered policy or exposure timing
- `IV` when treatment is endogenous but a credible source of exogenous variation exists
- `RDD` when institutional thresholds create quasi-random assignment
- panel fixed effects when within-unit changes are informative
- matching or reweighting when selection on observables is the best available design

## Questions To Ask

- what variation identifies the estimate
- what assumptions make that variation credible
- what threats are first order
- what diagnostics speak directly to those threats
- what parameter is being estimated and for whom

## Warning

Never treat robustness checks as a substitute for identification logic.
