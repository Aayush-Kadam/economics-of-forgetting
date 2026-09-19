# M3 Phase Report

## MILESTONE

M3 — institution-produced outcome persistence and endogenous predictiveness

## STATUS / VERDICT

**COMPLETE — PASS WITH LIMITATIONS**

## CANONICAL MODEL VERSION

The unchanged M2 finite-horizon, score-based dynamic control problem, augmented with repeated policy paths and matched structural counterfactuals. It is not a Bayesian or competitive equilibrium.

## PRIMARY M3 QUESTION

Holding current true fundamentals and future primitive shocks fixed, can public reputation change future true quality through opportunity-sensitive productive effort, and can that channel create conditional predictive content?

## COUNTERFACTUAL WORLDS

Full; information-only/fixed effort; `alpha=0`; `rho=0`; `phi=0`; randomized record; and self-correcting policy region. Common future shocks are used.

## PERSISTENCE AND PREDICTIVENESS DEFINITIONS

Intrinsic persistence is the `rho^h Delta x_t` term. Record persistence is mechanical score carryover through `phi`. Behavioral persistence is the distributed lag of effort gaps. Conditional predictiveness is the incremental linear forecast contribution of `R_t` after controlling for `x_t`, summarized by its coefficient, MSE gain, and partial R-squared.

## PROPOSITION STATUS

1. **PROVED:** matched records that induce different effort create one-period true-quality divergence.
2. **PROVED:** the exact multi-period propagation identity holds under common shocks.
3. **PROVED BY CONSTRUCTION:** repeated record-dependent effort creates multi-period true-quality gaps at `rho=0`.
4. **PROVED LOCALLY:** the policy-dependent `(x,R)` Jacobian characterizes finite-horizon local propagation.
5. **VERIFIED STRUCTURALLY:** randomized reputation produces conditional predictiveness in the full channel and not the information-only placebo.
6. **PROVED CONDITIONALLY:** self-confirming and self-correcting regions are separated by the sign of the local effort response to reputation.

## ZERO-RHO RESULT / MULTI-PERIOD PROPAGATION

At `rho=0`, the benchmark full path has quality gaps `0, .1470, .1248, .1060, .0900, .0764, .0648`. Every nonzero term is behavioral. Repeated effort differences may be sustained either by mechanical record carryover or by endogenous quality-to-score feedback. The exact general identity is

`Delta x_{t+h}=rho^h Delta x_t + alpha sum rho^{h-1-j} Delta e_{t+j}`.

## EFFECTIVE PERSISTENCE

The local Jacobian contains direct quality persistence, policy feedback, and score carryover. For the full zero-`rho` benchmark it is `[[0,.245],[0,.849]]`. The `.849` root is a path diagnostic, not a claim about an infinite-horizon equilibrium.

## INFORMATIONAL VS BEHAVIORAL COMPONENT

Randomized records contain no information about current fundamentals. Yet the full channel yields a reputation coefficient `.4996`, MSE improvement `.2482`, and partial R-squared `.7974`. The matched information-only placebo yields approximately zero on all incremental measures. Thus predictive content is institution-produced in this construction.

## SELF-CONFIRMING / SELF-CORRECTING REGIONS

Both exist. Positive local `e_R` makes worse records self-confirming; negative `e_R` makes them self-correcting. Effort bounds create flat regions. M3 therefore rejects a global self-fulfilling-stigma theorem.

## FALSE-RECORD EXPERIMENT

Passed using randomized record assignment independent of current quality. The initially false label changes later true quality only when it changes productive effort.

## MEMORY COMPARATIVE STATICS

In the reported benchmark, `phi=0` sharply reduces propagation relative to `phi=.8`, but does not erase the first behavioral response to the initially assigned record. No global monotonicity in `phi` is claimed because M2 already established policy relocation and boundary counterexamples.

## COUNTEREXAMPLES / PLACEBO RESULTS

Negative `e_R` reverses the direction; `e_R=0` or effort clipping flattens it. The `alpha=0` and fixed-effort worlds have zero true-quality gap even while score gaps persist. All specified core placebos pass.

## PROOF AUDIT / COMPUTATIONAL VALIDATION

The induction identity and Jacobian are analytical. Six new regression tests cover the identity, zero-`rho` repetition, placebos, both sign regions, the Jacobian, and randomized-record predictiveness. Reproduction command: `python scripts/run_m3_counterfactuals.py`.

## WHAT SURVIVED / WHAT FAILED

Survived: exact pathwise decomposition, causal matched-world divergence, multi-period zero-`rho` feedback, local effective persistence, and conditional institution-produced predictiveness. Failed as global claims: bad reputation always lowers effort; persistence always amplifies the gap; or statistical predictiveness is wholly causal.

## SCIENTIFIC RISKS

The opportunity schedule remains exogenous; the repeated affine policy is a transparent local policy diagnostic rather than a newly solved market equilibrium; statistical magnitudes are calibration-specific; nonlinear channel interactions are not additively identified; empirical external validity is not claimed.

## KEY FILES CREATED

`src/economics_of_forgetting/m3.py`; `tests/test_m3_persistence.py`; `scripts/run_m3_counterfactuals.py`; the M3 decomposition, counterfactual, proof-audit, recovery, and phase reports; and machine-readable experiment output.

## TEST STATUS

`28 passed` after the M3.5 frozen-update placebo.

## REPOSITORY STATE / CURRENT COMMIT / CURRENT TAG

Branch `recovery/m3-interrupted-session`; M3 changes are uncommitted over `8d1966ee59612759760a2b12b5fa996ee5c62de1`; current latest tag remains `m2-theory-core`. No M3 tag is created before review/commit.

## DECISION / NEXT MILESTONE

**PASS WITH LIMITATIONS.** M3 is closed at the structural-mechanism level. M4 is not started in this recovery session.
