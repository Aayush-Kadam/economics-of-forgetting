# MILESTONE
M7 adversarial robustness gate.

# STATUS
Complete within the preregistered bounded implementation; several ideal-matrix families remain explicitly unsupported.

# VERDICT
**PASS WITH LIMITATIONS.**

# M6.5 AUDIT VERDICT
M6 survives with reframing and proceeds to M7.

# PRIMARY SURVIVING CONTRIBUTION
A simple universal clean/adverse lifecycle-contingent persistence rule can outperform the best universal constant persistence rule over meaningful regions of the finite-horizon model.

# SECONDARY SURVIVING CONTRIBUTIONS
The sign survives several opportunity shapes, horizons, limited latent heterogeneity, and repeated-offense stresses; magnitude depends strongly on curvature and population composition.

# OPPORTUNITY-FUNCTION ROBUSTNESS
Positive in five implemented cases; tiny under linear access and large under a hard threshold.

# EFFORT-COST ROBUSTNESS
Positive for quadratic-cost curvature kappa 0.6, 1.2, and 2.5. Alternative cost families remain untested.

# STATE-DYNAMICS ROBUSTNESS
Positive for rho 0, .45, .9 and alpha .3, .55, .8. Nonlinear transition laws remain untested.

# SIGNAL ROBUSTNESS
Detection variations are positive. False positives and stochastic signal distributions remain unimplemented.

# SCORE-RULE ROBUSTNESS
Only exponential updating is solved. Rolling windows, expiration, and bounded-history rules remain open.

# INITIAL-DISTRIBUTION ROBUSTNESS
Positive for six populations, but two gains are below 0.01 and one is below 0.001.

# HETEROGENEITY ROBUSTNESS
Positive under two common-policy mixtures; broad and joint heterogeneity remain open.

# FALSE-POSITIVE ROBUSTNESS
Not solved; this is a material limitation.

# FALSE-NEGATIVE ROBUSTNESS
Detection probability 0.25–0.95 preserves the sign, with gains 0.0066–0.3863.

# REPEAT-MISCONDUCT ROBUSTNESS
All 12 stresses are positive; only six are material at the 0.01 threshold.

# HORIZON ROBUSTNESS
Positive at T=3,6,12,20,30,50; the optimal adverse persistence changes materially with horizon.

# CONTINUOUS-OPTIMIZATION ROBUSTNESS
Continuous versus 501-point effort solutions differ by at most 0.000972 in 12 representative checks. Continuous memory optimization is not certified.

# TIMING ROBUSTNESS
Not solved beyond the corrected canonical timing; no invariance claim is permitted.

# STATE-DEFINITION ROBUSTNESS
The computed state is a lifecycle flag. Alternative score/recent-event/absorbing definitions remain open.

# DIRECT-PUNISHMENT COMPARISON
Constant memory plus a strong costless-transfer penalty beats baseline two-state memory; adding state contingency still raises welfare further. Memory is second-best but not redundant in this benchmark.

# CURRENT-STATE OBSERVABILITY
Not solved. Informational and incentive channels are not separately identified.

# OPPORTUNITY-ENDOGENEITY CHECK
Not solved.

# ZERO-RHO RESULT
Positive in the central rho=0 M7 case, but M6.5 supplies exact zero-value counterexamples at low alpha and long horizon.

# SELF-CONFIRMING VS SELF-CORRECTING RESULT
The prior descriptive masses do not explain gains and are not promoted as a result.

# TWO-STATE ADAPTIVE-MEMORY RESULT
Survives regionally, best interpreted as lifecycle-contingent persistence rather than earned forgetting.

# POLICY COMPLEXITY CEILING
M6 higher classes can add value, but lifecycle timing confounds parameter-count comparisons. No universal ceiling is claimed.

# WELFARE / PREDICTION QUADRANTS
Exact alignment fails under refinement; prediction and welfare remain separate objectives.

# ECONOMIC MAGNITUDE
Ranges from effectively zero to large. Sign counts are not enough; linear access and some populations yield negligible gains.

# NOVELTY RE-CHECK
Bounded-memory enforcement and endogenous-record reputation are close literatures. The narrow contribution, if retained, must be the constrained comparison of constant versus lifecycle-contingent decay with endogenous rehabilitation—not generic temporary punishment.

# COUNTEREXAMPLES
Exact zero value at M6.5 indices 1 and 3; negligible linear-opportunity value; direct punishment dominates the no-penalty adaptive baseline.

# NEGATIVE RESULTS
No earned-forgetting result, no universal half-life, no explanatory memory-conflict index, no exact prediction/welfare equality, and no exhaustive robustness.

# THEOREM SURVIVAL
The finite-state strict-contingency inequality remains valid. M7 does not invalidate the M2/M3 analytical results.

# REFEREE VERDICT
Major revision; retain only a theory-first, constrained lifecycle-state paper.

# PAPER ARCHITECTURE
Lead with the strict-contingency theory, then mechanism decomposition, counterexamples, regional computations, and direct-instrument comparison.

# KEY FIGURES
No new figure is elevated; the raw robustness table is more informative than a decorative plot.

# KEY TABLES
`m6_5_audit.csv`, `m7_robustness.csv`, and `m7_effort_solver.csv`.

# TEST STATUS
52 passed.

# RUNTIME / REPRODUCIBILITY
Deterministic; no seed except the fixed global-solver seed. M7 battery runtime 67.7 seconds; full reproduction includes the separate 80.2-second M6 atlas and 70.5-second M6.5 audit.

# WHAT SURVIVED
Regional two-state value, nesting, selected horizon/curvature/heterogeneity/recurrence robustness, and local continuous-effort validation.

# WHAT FAILED
Strong magnitude labels, exact predictive alignment, and the interpretation of the result as uniquely about memory rather than an adverse lifecycle punishment state.

# SCIENTIFIC RISKS
Alternative timing, false positives, score-rule alternatives, direct-penalty constraints, current-state observability, and continuous memory globality remain unresolved.

# REPOSITORY STATE
M7 artifacts, source, tests, and ledgers are committed on the recovery branch; historical tags are untouched.

# CURRENT COMMIT
Recorded after the M7 commit.

# CURRENT TAG
`m7-design-limited` after final validation.

# DECISION
Retain the project but narrow to lifecycle-contingent persistence under constrained instruments.

# NEXT MILESTONE
Stop. Design M8 separately around the narrowed theory-first architecture.
