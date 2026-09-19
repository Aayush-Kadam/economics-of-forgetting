# M4.5 Hostile Audit

## MILESTONE

M4.5 — hostile audit of the fixed-memory planner

## STATUS

Complete after prospective correction of a discrete-time deterrence inconsistency. Historical M4 commits and tags were not altered.

## M4 ORIGINAL VERDICT

PASS WITH LIMITATIONS.

## BENCHMARK BOUNDARY RESULT

The benchmark still selects `phi*=0`. The original code mixed a one-period recovery delay at exactly zero with a continuous sub-period delay immediately above zero. M4.5 replaces that inconsistent relaxation with integer recovery time throughout. After correction, the local welfare slope over `[0,.01]` is `-.156`: productive surplus contributes `-.146`, bad-match loss `-.087`, effort-cost relief contributes `+.076`, and misconduct harm is locally flat. Minimal memory therefore survives for economic rather than discontinuity-driven reasons.

## INTERIOR MEMORY CASES

High effort cost (`kappa=3`) yields `phi*=.274` and half-life `.536`. Weak rehabilitation makes some retained screening/deterrence value worth preserving. Interior cases remain in the seeded search, but exact locations are calibration-dependent.

## LONG MEMORY CASES

At `rho=0`, the audited calibration selects approximately `phi=.80` (`H=3.08`). A two-period horizon selects near-permanent memory because initial screening and deterrence dominate the short window. These are regime examples, not monotone comparative-static theorems.

## MULTIPLE LOCAL MAXIMA AUDIT

The headline multiplicity claim is substantially weakened. A representative case shows 57–62 apparent material peaks on an effort grid of 101, 11–20 on 401, but zero to two on 1001 under small cost perturbations. Most peaks are discretized-policy roughness. Robust non-concavity remains possible, but widespread multiple economic maxima are **NOT ESTABLISHED**.

## PREDICTION VS WELFARE AUDIT

Both orderings continue after the timing correction. Persistence, horizon, opportunity curvature, effort cost, and misconduct harm shift the ordering. No stable one-dimensional boundary supports a theorem.

## NAIVE VS BEHAVIOR-AWARE AUDIT

Both directions continue. Self-confirming feedback can make long memory costly, while self-correcting effort can make consequences productive. Screening and deterrence also matter, so the M3 sign region alone is insufficient.

## STATE-SPECIFIC MEMORY MARGINS

The corrected benchmark reveals material lifecycle disagreement. A safe high-quality clean state has positive local memory value and selects approximately `phi=.44` (`H=.84`), while the low-quality favorable-record type and all audited adverse/recovery states select near-zero memory. Local slopes range from positive `.10` to negative `.64`.

## DOES FIXED MEMORY CREATE AN INSTITUTIONAL CONSTRAINT?

Yes. Reachable positive-weight states have different preferred memory directions and distinct optima. A constant rule cannot implement both. This motivates a precommitted lifecycle/state-contingent policy independently of the corrected artifact.

## WHAT SURVIVED

The minimal-memory benchmark, multiple retention regimes, designer-ordering reversals, behavior-aware reversals, and meaningful state-specific disagreement.

## WHAT FAILED

The original zero-boundary deterrence implementation and the strong claim that numerous local maxima are robust economic features.

## SCIENTIFIC RISKS

State margins use singleton continuation welfare; population weights and commitment interactions matter. Integer recovery creates policy kinks. General regime boundaries remain numerical.

## FINAL VERDICT

**M4 SURVIVES WITH REFRAMING — PROCEED TO M5.**
