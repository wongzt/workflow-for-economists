# Example Research Proposal

## Working Title

Broadband Expansion and Labor-Market Adjustment in Rural China

## Question

Does rural broadband rollout improve local labor-market outcomes by expanding job search and market access, or do the gains mainly reflect migration and compositional change?

## Motivation

Digital infrastructure is often justified as a tool for reducing spatial inequality. The policy relevance is clear, but the mechanism is not. A rise in local earnings may reflect better local matching, better outside options, selective migration, or measurement changes in recorded activity.

## Contribution

This project aims to contribute by:

1. estimating the average effect of broadband rollout on employment, earnings, and firm entry
2. testing whether the timing and heterogeneity fit a labor-market access channel
3. distinguishing local adjustment from migration-based composition

## Identification Strategy

Preferred design:

- county-by-year panel
- event-study around broadband rollout
- county and year fixed effects
- province-by-year controls where needed

Diagnostics:

- pre-trend test
- timing robustness
- alternative clustering levels
- placebo outcomes that should not move immediately

Fallback design:

- instrument rollout with engineering-cost or backbone-distance measures if rollout timing appears too endogenous

## Data Plan

- broadband rollout dates from administrative or provider records
- county labor outcomes from statistical yearbooks or labor-market administrative data
- firm entry from business registration data
- migration or hukou-adjustment proxy if available

## Main Risks

- rollout timing may respond to expected local growth
- measured coverage may not equal actual household access
- labor-market outcomes may shift through migration rather than local adjustment

## First Table Sequence

1. institutional timeline and descriptive rollout table
2. baseline event-study estimates
3. robustness to sample, controls, and clustering
4. heterogeneity by pre-rollout market access
5. mechanism table on firm entry or job-search proxies
