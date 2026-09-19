# M4 Phase Report

## MILESTONE

M4 — optimal constant reputation memory / social planner

## STATUS

Complete.

## VERDICT

**PASS WITH LIMITATIONS**

## M3.5 AUDIT VERDICT

M3 SURVIVES WITH FURTHER REFRAMING — FREEZE AND PROCEED TO M4.

## CANONICAL PLANNER MODEL

A finite-horizon planner chooses one constant `phi` for the M2/M3 score-based control environment. Policies are re-solved at each candidate memory rule. The model remains a reduced-form dynamic control problem, not a Bayesian or competitive equilibrium.

## WELFARE FUNCTION

`W(phi)=sum beta^t E[productive surplus - bad-match loss - effort cost] - misconduct harm`.

## WELFARE COMPONENTS

Real allocated output, real loss from low-quality allocation, rehabilitation effort disutility/resource cost, and external misconduct harm. Wages/opportunity payments are excluded as transfers. No ad hoc memory penalty is used.

## OPTIMAL MEMORY RESULT

The normalized benchmark chooses `phi*=0` with welfare `.60545`: minimal fixed memory is a genuine boundary solution.

## OPTIMAL HALF-LIFE

Benchmark `H*=0` periods. Sensitivity cases range from zero to `H*=114.4` near the upper numerical boundary; these are calibration outcomes, not policy recommendations.

## BOUNDARY VS INTERIOR CLASSIFICATION

All regimes occur. The benchmark is short/boundary; `kappa=3` yields an intermediate optimum; `rho=0` and `beta=.75` yield long memory; horizon two yields near-permanent memory. The seeded search also finds interior and upper-boundary cases.

## SCREENING MARGIN

Memory preserves informative ordering but also stale erroneous records. Productive output and real bad-match loss capture the two sides jointly.

## DETERRENCE MARGIN

Longer recovery delay weakly reduces misconduct in unsaturated regions and therefore favors memory locally. It does not globally move the optimizer monotonically once other margins and probability bounds interact.

## REHABILITATION MARGIN

Memory changes effort returns. The effect can suppress or stimulate effort depending on the M3 region, so rehabilitation productivity has no established global optimizer sign.

## BEHAVIORAL FEEDBACK MARGIN

The full-versus-fixed benchmark changes welfare components but not the default boundary choice. Across the seeded search it changes optimal retention substantially in both directions.

## PREDICTION-OPTIMAL MEMORY

Benchmark `phi_pred*=0` for the multi-period score-as-forecast MSE objective. Other defensible parameterizations select much longer prediction memory.

## WELFARE-OPTIMAL MEMORY

Benchmark `phi_welfare*=0`. The broader search contains interior and near-permanent welfare optima.

## NAIVE VS BEHAVIOR-AWARE PLANNER

Benchmark choices coincide at zero. Counterexamples show `phi_full<phi_naive` and `phi_full>phi_naive`; no universal bias direction survives.

## COMPARATIVE STATICS

Mostly regional and numerical. Low `rho`, high `kappa`, low `beta`, and short horizons can move the optimum sharply toward longer memory. Baseline alpha and misconduct-harm sweeps remain at zero. Global monotonicity is rejected.

## REGIME MAP

The benchmark `rho x alpha` map contains 24 short-memory cells and one intermediate cell. The wider seeded search supplies long and near-permanent regimes. M4.5 finds that most apparent local maxima vanish with action-grid refinement, so robust multiplicity is not established.

## DISTRIBUTIONAL EFFECTS

Rapid updating benefits the two adverse-record benchmark types through rehabilitation. The low-quality favorable-record type has the lowest modeled incidence. This is descriptive model incidence, not a fairness theorem.

## COUNTEREXAMPLES

Both prediction/welfare orderings and both naive/full orderings occur. Welfare can be multi-peaked. Neither higher intrinsic persistence nor greater rehabilitation productivity has a protected global sign.

## PROOF AUDIT

Planner existence is proved on compact subdomains under continuous primitives and a unique continuous policy. All stronger optimizer/comparative-static results are honestly classified as numerical or false globally.

## COMPUTATIONAL VALIDATION

Global grids plus local refinement; policy re-solution at every `phi`; linear/logistic opportunity; horizons 2–10; zero/positive `rho`; parameter sweeps; phase map; 100 seeded counterexample draws; and regression tests.

## WHAT SURVIVED

A coherent non-ad-hoc planner, boundary/interior regime classification, economically interpretable margins, meaningful behavioral designer differences, and prediction-versus-welfare divergence in both directions.

## WHAT FAILED

The benchmark interior optimum, a universal prediction-too-long result, a universal naive-too-long result, unimodality, and monotone global comparative statics.

## SCIENTIFIC RISKS

Reduced-form opportunity, rolling finite-horizon policies, calibration-dependent magnitudes, coarse population support, no full stochastic filtering model, and numerical kinks near action/deterrence bounds.

## KEY FILES CREATED

`m4.py`; M4 planner/counterexample scripts; welfare, planner, proof, counterexample, and phase documents; generated JSON/CSV tables and four figures; and M4 tests.

## TEST STATUS

`34 passed` after the M4.5 discrete-time deterrence correction and boundary regression test.

## REPOSITORY STATE

M3 and M4 are frozen on `recovery/m3-interrupted-session`; the working tree is clean at the freeze.

## CURRENT COMMIT

M3 freeze: `dce26a642bf731dda27b0a16bbecfb26ed1ab1ff`. M4 scientific freeze: `2c0657a2c8a74315f3f9c41a4f9be75f09f05433`.

## CURRENT TAG

M3: `m3-regional-feedback`. M4: `m4-boundary-memory`.

## DECISION

**PASS WITH LIMITATIONS.** The fixed-memory planner is scientifically coherent, but its chief result is regime dependence rather than a universal interior half-life or designer ordering.

## NEXT MILESTONE

Stop. M5 earned/history-dependent forgetting is not started.
