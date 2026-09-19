# M2 Phase Report

## MILESTONE

M2 — formal dynamic theory, equilibrium consistency, and proof auditing

## STATUS

COMPLETE

## VERDICT

PASS WITH LIMITATIONS

## M1.5 AUDIT VERDICT

M1 SURVIVES WITH REFRAMING — PROCEED TO M2.

## FINAL CANONICAL MODEL

A finite-horizon score-based dynamic control problem with public score `R`, true quality `x`, clean/adverse lifecycle state `z`, record persistence `phi`, intrinsic persistence `rho`, productive effort `e`, and effort productivity `alpha`.

## EQUILIBRIUM CONCEPT

Dynamic control problem against an exogenous opportunity schedule. It is not labeled a market or Bayesian equilibrium.

## TIMING

State observation; opportunity assignment; lifecycle-specific action; flow payoff; quality transition; signal generation; score update; continuation.

## CORE EQUATIONS

`x'=rho x+alpha e+epsilon`; `y'=x'+eta`; `R'=phi R+(1-phi)y'`; adverse-state Bellman equation `V=max_e{vA(R)-kappa e^2/2+beta E[V']}`.

## PROPOSITION 1 STATUS

PROVED, global on the reachable deterministic-recovery domain.

## PROPOSITION 2 STATUS

PROVED, parameter-dependent binary rehabilitation threshold.

## PROPOSITION 3 STATUS

PROVED globally for linear opportunity and regionally for smooth increasing opportunity under a strict interior optimum.

## PROPOSITION 4 STATUS

PROVED for clean agents with positive, unsaturated continuation loss; not global across reputation histories.

## PROPOSITION 5 STATUS

PROVED as existence of a nonempty open lifecycle-asymmetry region.

## PROPOSITION 6 STATUS

PROVED for a next-period quality gap at `rho=0`; indefinite persistence is not proved.

## PROPOSITION 7 STATUS

PROVED: absent later effort differences, an induced state gap decays geometrically at `rho`.

## LIFECYCLE ASYMMETRY

Survives as a regional theorem under one common memory parameter, not as global monotonicity.

## LOGISTIC / SMOOTH-MARKET RESULT

The local sign is determined by signal attenuation plus curvature relocation. Both signs occur in admissible parameter regions; a machine-readable counterexample set is retained.

## RECORD MEMORY VS STATE MEMORY

`phi` controls institutional score inheritance; `rho` controls actual quality carryover; `alpha` maps effort into quality. They are separate in equations and tests.

## BEHAVIORAL PERSISTENCE RESULT

Different records can change actual next-period quality even at `rho=0`. Persistence beyond one period then requires repeated record-dependent effort.

## COUNTEREXAMPLES

Positive logistic memory effects, worse-record/higher-effort cases, and boundary-flat cases are stored in `experiments/m2_theorems/counterexamples/logistic_counterexamples.json`.

## PROOF AUDIT

All seven propositions are verified under stated conditions. Global logistic, infinite-horizon, and equilibrium interpretations were rejected.

## THEOREM REGRESSION TESTS

Seed `20260919`; 1,000 draws for each main monotonicity theorem, plus finite-difference IFT checks at regular interior points.

## WHAT SURVIVED

Recovery, binary threshold, global linear attenuation, regional smooth discouragement, clean-state deterrence, regional lifecycle asymmetry, and history-induced true-quality divergence.

## WHAT FAILED

Global logistic discouragement, universal deterrence, infinite persistence at `rho=0`, full Bayesian/market equilibrium consistency, and any statistical predictiveness theorem.

## SCIENTIFIC RISKS

The regional theorem may be viewed as assembling known mechanisms; the opportunity schedule is exogenous; infinite-horizon policy properties and quantitative importance remain unknown.

## KEY FILES CREATED

Formal appendix, dynamic transition module, proof audit, theorem-regression tests, counterexample engine and data, updated ledgers, and this report.

## TEST STATUS

21 tests passed. The theorem-regression module used seed `20260919`, 1,000 admissible draws for each main monotonicity result, finite-difference checks of the implicit derivative at regular interior solutions, and the required `rho=0` history-gap test.

## REPOSITORY STATE

Formal documents, source, appendix, tests, and machine-readable counterexamples reproduce cleanly; pending milestone commit.

## CURRENT COMMIT

To be recorded by Git.

## CURRENT TAG

`m2-theory-core` only after all tests and counterexample generation pass.

## DECISION

Proceed to M3 only with the regional theorem and score-based interpretation. M3 must build, not assume, a formal predictiveness decomposition.

## NEXT MILESTONE

M3 — endogenous feedback and institution-produced outcome persistence.
