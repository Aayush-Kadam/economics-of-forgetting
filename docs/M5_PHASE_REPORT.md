# M5 Phase Report

## MILESTONE

M5 — history-dependent and earned forgetting

## STATUS

Complete at the parsimonious policy-class level.

## VERDICT

**PASS WITH LIMITATIONS**

## M4.5 AUDIT VERDICT

M4 SURVIVES WITH REFRAMING — PROCEED TO M5.

## WHY STATE-CONTINGENT MEMORY IS OR IS NOT JUSTIFIED

It is justified: positive-weight clean and adverse states have different local memory demands, and a lifecycle rule strictly improves welfare. Earned post-rehabilitation acceleration itself is not justified by the benchmark.

## CANONICAL M5 MODEL

The M4 finite-horizon population model extended with lifecycle, favorable-signal streak, offense count, probabilistic misconduct branching, recovery, and repeated offending.

## COMMITMENT ASSUMPTION

The institution publicly commits at `t=0`; agents face the announced rule. Discretion is not solved.

## FIXED-MEMORY BENCHMARK

Within the repeated-event M5 model, the optimal constant policy is `phi=.85`, `m=1`, welfare `-.28110`.

## ADAPTIVE POLICY CLASS

Three persistence parameters—clean, adverse, and rehabilitation—plus one favorable-streak threshold. Constant policies are nested exactly.

## EARNED-FORGETTING RULE

The restricted monotone-relief rule collapses to the constant optimum and adds zero welfare in the benchmark.

## OPTIMAL STATE-CONTINGENT POLICY

`(phi_clean,phi_adverse,phi_rehab,m)=(0,.85,.85,1)`.

## VALUE OF ADAPTIVE MEMORY

`.015895` normalized welfare units over the globally searched constant rule in the same repeated-event model. Because benchmark welfare is negative, no misleading percentage normalization is reported.

## STRICT-DOMINANCE REGION

Positive in 11 of 16 reported `alpha x misconduct-harm` cells, ranging up to `.437`; zero in five cells. Tiny gains below `.004` occur in several cells.

## LIFECYCLE MEMORY RESULT

Lifecycle conditionality survives, but the ordering is low clean memory and high adverse memory in the benchmark—not rapid relief after rehabilitation.

## GOOD-BEHAVIOR RELIEF RESULT

Fails in the benchmark: `phi_rehab=phi_adverse`.

## DETERRENCE EFFECT

High adverse persistence reduces expected misconduct. Flexibility retains this while permitting different clean-state updating.

## REHABILITATION EFFECT

Effort and quality are unchanged between the optimal fixed and lifecycle rules in the benchmark; the gain comes from allocation/record updating. Other robustness cells use different rehabilitation memory.

## GAMING / CYCLING RESULT

Repeat misconduct is implemented but zero under the benchmark optimum within six periods. This is not a general gaming-proof result.

## TIME-CONSISTENCY RESULT

Not established.

## COMMITMENT VS DISCRETION

Only commitment is solved; no comparison is claimed.

## PREDICTION EFFECT

Prediction MSE improves from `.06764` to `.06167` under lifecycle memory.

## WELFARE EFFECT

Welfare improves from `-.28110` to `-.26521`, mainly through lower bad-match loss despite slightly lower productive surplus.

## SIMPLE RULE VS FULL POLICY

The three-regime rule is the solved policy ceiling. A general dynamic policy was intentionally not used, so efficiency relative to a full-policy ceiling is unavailable.

## PLACEBO RESULTS

Removing effort eliminates rehabilitation effort; removing misconduct eliminates the deterrence channel; `alpha=0` can still leave lifecycle value through deterrence/screening; no-repeat and baseline recurrence are reported separately.

## COUNTEREXAMPLES

Earned relief can add zero value; contingency can collapse to constant; adverse memory can exceed clean memory; flexibility value is nonmonotone in `alpha`; welfare and prediction can improve together.

## LITERATURE COLLISION CHECK

Ali and Miller (2016) already establish that forgiveness can improve ostracism; forgiving strategies and reputation repair are also established in repeated games and online trust systems. M5 therefore makes no broad novelty claim about forgiveness. Its narrower object is score-memory selection with productive quality, lifecycle-specific retention, and welfare/prediction accounting.

## THEOREMS / RESULTS STATUS

Nesting: proved. Strict finite-state contingency value: proved under differing unique state optima. Lifecycle gain: numerical. Earned relief: failed in benchmark. Gaming: partial. Time inconsistency: not established.

## PROOF AUDIT

Completed in `M5_PROOF_AUDIT.md`, including counterexamples and deterministic regression tests.

## COMPUTATIONAL VALIDATION

Global enumeration of parsimonious rules, optimized constant benchmark, 16-cell dominance map, five placebos, repeated-event probability tree, three generated figures, and deterministic tests.

## WHAT SURVIVED

Strict regional value of lifecycle contingency; separation of clean and adverse memory; simultaneous welfare and prediction improvement in the benchmark.

## WHAT FAILED

Universal earned forgetting, accelerated rehabilitation relief, a time-inconsistency theorem, a full dynamic-policy result, and general gaming claims.

## SCIENTIFIC RISKS

Rolling effort response rather than fully forward-looking policy anticipation; coarse memory grid; deterministic quality signals; short horizon; exogenous opportunity; no empirical calibration; literature overlap with forgiveness mechanisms.

## KEY FILES CREATED

M5 source/tests, policy/earned/commitment/gaming/proof/counterexample reports, phase report, reproducibility script, JSON results, three tables, and three figures.

## TEST STATUS

`42 passed in 2.64s` in the final pre-freeze validation.

## REPOSITORY STATE

M4.5 and M5 are committed; the working tree is clean at the final freeze.

## CURRENT COMMIT

M4.5: `0fdebcb54beeb7e932fd1c09d516036fd21f57e6`. M5 scientific freeze: `3c6f58e259dede7e729700e8009c5a6a1c4695ef`.

## CURRENT TAG

`m5-state-contingent-memory` (M4 historical tag remains `m4-boundary-memory`).

## DECISION

**PASS WITH LIMITATIONS.** The surviving object is lifecycle/state-contingent memory, not earned forgetting.

## NEXT MILESTONE

Stop. Do not begin M6.
