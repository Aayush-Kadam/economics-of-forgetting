# M3.5 Hostile Audit

## MILESTONE

M3.5 — freeze, review, and hostile audit of institution-produced persistence

## STATUS

Complete.

## M3 ORIGINAL VERDICT

PASS WITH LIMITATIONS.

## HEADLINE RESULT AUDIT

The narrow headline survives: at `rho=0`, public records can create multi-period true-quality differences through repeated record-dependent productive-effort differences. Repeated effort transmission is necessary. A one-time effort gap alone lasts one period.

The audit rejects a stronger interpretation that endogenous quality-to-score feedback is always necessary. When `phi>0`, mechanical carryover of the original record can itself keep effort different across periods. When both endogenous quality updating and record carryover are disabled, the effect ends after the first transition.

## ZERO-RHO AUDIT

- `alpha=0`: all true-quality gaps vanish.
- `e_R=0`: all true-quality gaps vanish at matched current quality.
- endogenous quality update disabled, `phi=0`: only the first-period gap remains.
- endogenous quality update disabled, `phi=.8`: later gaps remain because the original score difference survives mechanically and repeatedly changes effort.
- full updating, `phi=0`: quality affects the next score directly, allowing a pure behavioral feedback chain.

Thus there are two finite-horizon propagation routes: mechanical record carryover into repeated effort, and endogenous `x -> signal -> R -> effort` feedback.

## SELF-CONFIRMING REGION

At matched fundamentals, `Delta x_{t+1}=alpha e_R Delta R_t` locally. For `alpha>0`, `e_R>0` means a lower record reduces effort and is self-confirming. In the interior one-investment logistic problem,

`sign(e_R)=sign(A''(r))`

because the remaining factors and strict-SOC denominator are positive. The self-confirming region is therefore the convex portion of the opportunity curve, subject to interiority.

## SELF-CORRECTING REGION

For `e_R<0`, a lower record raises effort and partially repairs the quality difference. In the interior logistic problem this is the concave portion of the opportunity curve. The numerical smooth-policy scan finds self-confirming states from low records through approximately `R=.35` and self-correcting states from approximately `R=.40` upward in the audited calibration.

## SMOOTH-OPPORTUNITY ROBUSTNESS

Passed with the logistic opportunity map and globally optimized effort grids. Both sign regions occur with efforts strictly between zero and one. The sign boundary is analytical in the one-investment interior subproblem: `A''(r)=0`; for logistic opportunity this is `r=threshold`. Primitive parameters (`phi`, `alpha`, `beta`, `kappa`, horizon, current `R,x`) move the endogenous post-effort score `r` and can move the state across that boundary. Outside the strict interior, clipping and global nonconcavity require numerical classification.

## HORIZON ROBUSTNESS

Nonzero multi-period gaps occur over simulated horizons 2, 4, 6, 8, and 12 under rolling smooth logistic effort. The sign can change with the decision horizon/state path; this reinforces the regional result. Mean absolute gaps range from `.0325` to `.1514` in the reported normalized calibration.

## PLACEBO RESULTS

All decisive placebos pass: `alpha=0`, fixed effort, reputation-independent effort, no carryover plus frozen endogenous record update, and randomized-record information-only prediction. Frozen quality updating alone does not eliminate the effect when `phi>0`; it identifies mechanical record carryover as the alternate channel.

## ECONOMIC MAGNITUDE

The smooth benchmark produces average absolute true-quality gaps of roughly 3–15 percent of the normalized quality unit across horizons. Efforts are interior, so these results are not created by action clipping. Magnitudes remain calibration-specific and are not external policy estimates.

## PREDICTIVENESS CLAIM AUDIT

- Structural future-state effect: **PROVED UNDER CONDITIONS** by the state equation.
- Multi-period outcome persistence: **PROVED BY CONSTRUCTION / REGIONAL** under repeated record-dependent effort.
- Conditional predictive value: **NUMERICALLY SUPPORTED** in randomized-record simulations.
- General statistical channel decomposition: **NOT ESTABLISHED**.

## WHAT IS PROVED

The exact propagation identity; the necessity of repeated effort at `rho=0`; the local sign condition `sign(alpha e_R)`; the interior logistic boundary `A''(r)=0`; and the channel-killing `alpha=0` and `e_R=0` placebos.

## WHAT IS ONLY NUMERICAL

Calibration-specific magnitudes, horizon paths, state-space prevalence of each sign region, and partial-R-squared/MSE values.

## WHAT MUST NOT BE CLAIMED

Bad reputation is always self-fulfilling; endogenous quality feedback is the only multi-period channel; higher `phi` always worsens outcomes; M3 identifies an empirical causal effect; or local Jacobian roots establish an infinite-horizon equilibrium.

## SCIENTIFIC RISKS

The opportunity schedule is exogenous; repeated rolling policies are finite-horizon diagnostics rather than a solved market equilibrium; statistical magnitudes are simulated; region weights require a population model; and score carryover and endogenous feedback interact non-additively.

## FINAL VERDICT

**M3 SURVIVES WITH FURTHER REFRAMING — FREEZE AND PROCEED TO M4.**
