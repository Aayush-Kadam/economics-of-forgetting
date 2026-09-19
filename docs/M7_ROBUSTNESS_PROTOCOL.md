# M7 robustness protocol

Status: preregistered before running `scripts/run_m7_robustness.py`.

## Estimand and benchmark

The primary estimand is the welfare of the best universal two-state rule minus the welfare of the best universal constant-memory rule. Every tested environment re-optimizes both classes on the same declared memory mesh. Positive signs alone do not constitute a pass: magnitudes, boundary hits, recurrence, and whether a direct instrument renders memory redundant are reported.

## Search and numerical rules

- Primary memory mesh: `{0, .25, .50, .75, .90, .99}`; constant policies are the diagonal subset of exactly the same mesh.
- Selected high-resolution checks: local mesh at 0.03 spacing around optima, effort grids 101 and 501, and bounded continuous effort optimization at representative policies.
- Tie tolerance: `1e-8`; material gain: at least `0.01` welfare units and at least `0.1%` of the tested constant-policy welfare range.
- A family passes regionally when at least half its defensible specifications have nonnegative gain and at least one has material gain. A universal claim requires all defensible specifications; no such claim is anticipated.
- Any nesting violation, nonfinite output, or material effort-grid reversal is a numerical failure.

## Preregistered matrix

| Family | Specifications / range | Expected tests | Reason |
|---|---|---:|---|
| Opportunity | logistic slopes 3, 6, 10; linear | 4 | Relocate curvature identified in M1.5 |
| Effort cost | `kappa` .6, 1.2, 2.5 | 3 | Test response-cost sensitivity |
| State dynamics | `rho` 0, .45, .9; `alpha` .3, .55, .8 | 9 | Persistence and rehabilitation mechanism |
| Signals/detection | detection .25, .65, .95 | 3 | False-negative proxy; model has no stochastic false-positive engine |
| Score normalization | threshold .35, .5, .65 with bad/good records shifted coherently | 3 | Test scale dependence |
| Initial distribution | baseline, high quality, low quality, high adverse share, low adverse share, bimodal | 6 | Composition sensitivity |
| Heterogeneity | one common policy under mixtures in `alpha` and `rho`; observable-type upper bound | 4 | Universal versus personalized policy |
| Repeat misconduct | benefit .75, 1.5, 3; detection .25, .65; horizons 12, 20 | 12 | Dedicated gaming stress |
| Horizon | 3, 6, 12, 20, 30, 50 | 6 | Terminal effects and persistence |
| Discounting | beta .7, .85, .95, .99 | 4 | Patience sensitivity |
| Harm/benefit | harm .3, 1.2, 3 and benefit .75, 1.5, 3 | 6 | Separate social and private stakes |
| Action bounds / solver | effort grids 101, 501 plus representative continuous solver comparison | 3 | Mandatory grid-artifact check |
| Timing | current-score opportunity and one-period-lagged opportunity | 2 | Detect sequencing dependence |
| State definition | lifecycle flag, current-score threshold, recent adverse event, absorbing flag | 4 | Test whether “two state” is definition-specific |
| Punishment flag | adverse-state access penalty without memory differentiation | 3 penalties | Test lifecycle-punishment equivalence |
| Direct punishment | constant memory plus post-misconduct penalty, penalty grid 0–2 | 9 | Determine second-best status |
| Current-state observability | reputation/current-quality blend 0, .5, 1 | 3 | Separate information from incentives |

## Explicitly unsupported families

Gaussian, fat-tailed, and heteroskedastic signal processes; rolling-window and bounded-history score objects; fully nonlinear state laws; fixed rehabilitation costs; endogenous opportunity investment; strategic multi-agent gaming; and a stationary infinite-horizon solution require new state spaces rather than parameter variations. They will be documented as untested rather than represented by cosmetic proxies. This is a deliberate scope boundary, and it prevents M7 from claiming the exhaustive robustness requested by the ideal matrix.

## Decision rule

- **PASS WITH LIMITATIONS** only if the primary sign survives a meaningful subset of opportunity, persistence, horizon, heterogeneity, recurrence, timing, and numerical checks, while failures are sharply delimited.
- **PIVOT REQUIRED** if alternative timing or continuous effort reverses the benchmark, heterogeneity broadly eliminates common-rule value, or direct punishment dominates and memory has no distinct constrained role.
- **FAIL** only if both the established M2/M3 theory and the M5/M6 computational design fail; M7 does not retest every theorem mechanically.
