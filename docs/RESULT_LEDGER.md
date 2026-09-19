# Result Ledger

| ID | Claim | Model/version | Type | Location / command | Status | Robustness |
|---|---|---|---|---|---|---|
| R-M2-01 | Continuous deterministic recovery time strictly rises with record persistence. | M2 deterministic score benchmark | Analytical | `paper/appendix.tex`; `pytest tests/test_theorem_regressions.py` | VERIFIED | Reachable threshold only |
| R-M2-02 | Binary rehabilitation has a unique state-dependent memory threshold for an interior cost range. | M2 binary rehabilitation | Analytical | Appendix; theorem tests | VERIFIED | Fails at extreme costs and patient pure-delay limit |
| R-M2-03 | Linear-opportunity productive effort falls with `phi`. | M2 one-decision subproblem | Analytical | Appendix; 1,000 seeded draws | VERIFIED | Bounds create weak rather than strict effects |
| R-M2-04 | Smooth nonlinear effort response is governed by attenuation plus curvature relocation. | M1.5/M2 logistic subproblem | Analytical + numerical | `M1_5_HOSTILE_AUDIT.md`; sign map | VERIFIED UNDER CONDITIONS | Both signs occur |
| R-M2-05 | Clean-state misconduct weakly falls with `phi` under unsaturated punishment. | M2 clean lifecycle state | Analytical | Appendix; 1,000 seeded draws | VERIFIED | Not global over already-stigmatized states |
| R-M2-06 | A nonempty state/parameter region exhibits lifecycle asymmetry. | M2 common-memory model | Analytical existence | Appendix, Proposition 5 | VERIFIED UNDER CONDITIONS | Regional, not global |
| R-M2-07 | At `rho=0`, history-dependent effort can create a next-period quality gap. | M2 state transition | Analytical + test | Appendix; regression test | VERIFIED | Long duration needs repeated effort |
| R-M2-08 | Institution-produced conditional predictiveness is isolated by matched/randomized-record counterfactuals. | M3 structural simulation | Structural | `M3_DECOMPOSITION.md`; M3 experiment | VERIFIED WITH LIMITATIONS | Not an empirical causal estimate |
| R-M3-01 | Exact intrinsic-plus-behavioral propagation identity. | M3 finite horizon | Analytical | `m3.py`; M3 proof audit | VERIFIED | Common primitive shocks |
| R-M3-02 | Repeated effort sustains true-quality gaps with `rho=0`. | M3 matched paths | Constructive | M3 experiment; tests | VERIFIED | Policy-dependent, not universal |
| R-M3-03 | `alpha=0` and fixed-effort placebos eliminate true-quality divergence. | M3 counterfactuals | Falsification | M3 experiment; tests | VERIFIED | Score gaps may remain |
| R-M3-04 | Both self-confirming and self-correcting regions exist. | M3 local policy analysis | Analytical + constructive | M3 proof audit; tests | VERIFIED UNDER CONDITIONS | Flat at bounds |
| R-M4-01 | The benchmark welfare-optimal fixed memory is the minimal boundary `phi=0`. | M4 normalized planner | Numerical global optimization | M4 benchmark table | VERIFIED FOR CALIBRATION | Not universal |
| R-M4-02 | Interior, long, and near-permanent regimes exist in sensitivity/search cases. | M4 planner | Numerical | Comparative statics; phase/counterexample outputs | VERIFIED BY CONSTRUCTION | Calibration-specific |
| R-M4-03 | Prediction and welfare objectives can choose different memory. | M4 designer comparison | Numerical | Counterexample output | VERIFIED BY CONSTRUCTION | Either ordering occurs |
| R-M4-04 | Internalizing behavior can move chosen memory in either direction. | Full versus fixed behavior | Numerical | Counterexample output | VERIFIED BY CONSTRUCTION | No global bias sign |
| R-M5-01 | Optimal lifecycle memory improves benchmark welfare by `.015895`. | M5 repeated-event model | Numerical enumeration | M5 results | VERIFIED FOR CALIBRATION | Modest, regional gain |
| R-M5-02 | Restricted earned forgetting collapses to constant memory. | M5 earned family | Negative numerical result | M5 results | VERIFIED FOR CALIBRATION | No accelerated relief result |
| R-M5-03 | Lifecycle memory improves benchmark prediction MSE and welfare together. | M5 model | Numerical | M5 results | VERIFIED FOR CALIBRATION | Not a universal frontier result |
| R-M5.5-01 | Two-state memory activation has stable positive value through horizons 3–20 and effort grids 101–1001. | M5.5 audit | Numerical convergence | M5.5 experiment | VERIFIED FOR AUDITED GRIDS | Gain is modest |
| R-M6-01 | Two-state adaptive value is positive at 33 of 36 predeclared design points. | M6 atlas | Deterministic enumeration | M6 atlas table | VERIFIED FOR DESIGN | Frequency is not probability |
| R-M6-02 | P0–P3 nested ordering holds at every design point. | M6 policy ladder | Numerical validation | M6 atlas flags/tests | VERIFIED 36/36 | Coarse common grid |
| R-M6-03 | Prediction memory has both orderings relative to welfare memory. | M6 atlas | Numerical | Regime table | VERIFIED FOR DESIGN | 11 longer, 4 shorter, 21 same-grid |
## M7 results

- R-M7.1: all 61 implemented cases preserve two-state-over-constant nesting; all gains are nonnegative and positive above `1e-8`.
- R-M7.2: magnitude is fragile: linear access yields 0.000270 and logistic slope 3 yields 0.003686.
- R-M7.3: gains remain positive at T=3,6,12,20,30,50, with changing optimal adverse persistence.
- R-M7.4: 12 recurrence stresses remain positive, but only six exceed 0.01.
- R-M7.5: costless direct punishment can dominate baseline two-state memory, yet state contingency adds value conditional on the penalty.
- R-M7.6: representative continuous effort differs from a 501-point grid by at most 0.000972.
