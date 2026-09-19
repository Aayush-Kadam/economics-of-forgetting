# MILESTONE

M6.5 hostile audit of the deterministic regime atlas.

# STATUS

Complete. The audit is deterministic and was run from tagged commit `32103c7`.

# M6 ORIGINAL VERDICT

M6 was a **PASS WITH LIMITATIONS**: two-state value was positive at 33/36 coarse-grid points, but magnitude labels and policy coincidences were not yet resolution-robust.

# ATLAS REPLICATION

All 47 pre-existing tests passed. The full 36-point atlas reproduced every substantive count: fixed regimes 6 minimal, 2 intermediate, 21 long, and 7 near-permanent; adaptive bins 3 negligible, 5 small, 15 moderate, and 13 large; prediction order 11 longer, 4 shorter, and 21 same; repeat misconduct positive at 7 points; nesting passed 36/36. Runtime was 80.2 seconds versus approximately 76 seconds previously. The difference is wall-clock drift, not output drift.

# 33/36 RESULT AUDIT

The audit records all 36 parameter vectors and outcomes in `outputs/tables/m6_5_audit.csv`. Re-optimization with a 301-point effort grid and local memory meshes produces 34 positive gains, rather than invalidating the original 33/36 statement. The extra positive case is index 0 and is economically tiny (`6.997e-5`). The useful distinction is economic, not sign-based: low persistence, low rehabilitation productivity, and low harm make clean and adverse states want nearly the same memory; higher harm makes adverse-state persistence valuable for deterrence while low clean-state persistence limits stale-score losses.

# LARGE-GAIN POINTS

All 13 originally LARGE points remain positive under the 301-point effort grid and denser local memory search. Several magnitudes shrink sharply: for example indices 9 and 11 fall from about 0.95 and 1.08 to 0.19 and 0.21, and indices 19, 22, and 23 fall to roughly 0.030, 0.069, and 0.099. Thus “large” was partly a coarse constant-policy-grid artifact. Boundary solutions remain common: the clean-memory optimum is frequently zero and the adverse-memory optimum often approaches 0.99. These are economically interpretable but make extrapolation beyond the allowed domain unsafe. The audit does not claim a global continuous optimum; it rejects only the hypothesis that the positive gains vanish under materially finer local searches.

# NEGLIGIBLE POINTS

Indices 1 and 3 remain exactly negligible. Index 0 becomes positive only at `6.997e-5`. All three have `rho=0`, `alpha=0.3`, and a constant-memory optimum at zero. With weak rehabilitation and no intrinsic persistence, additional adverse-state memory creates little productive response; at the longer horizon the clean/nonclean optima coincide exactly. They are mechanism counterexamples, not numerical failures.

# REGIME-THRESHOLD AUDIT

The fixed-memory and adaptive-value labels are descriptive bins. They are discontinuous at declared thresholds and should not bear inferential weight. The raw phi values, absolute gains, and normalized gains are therefore reported beside every label. M7 should discuss regions and magnitudes, not the count in an arbitrary bin.

# PREDICTION VS WELFARE GRID AUDIT

Of the 21 coarse “same grid point” cases, only 6 remain exactly equal on the local refined mesh. Three additional cases are within 0.03, while 12 differ by more than 0.03. Several differences are economically visible, around 0.05–0.09. The M6 claim must therefore be restated: coarse alignment is common, but exact prediction/welfare equality is not established.

# REPEAT-MISCONDUCT AUDIT

All seven positive-recurrence points retain a positive two-state gain when their audited policies are evaluated at twice the original horizon. The fixed-policy longer-horizon gains range from about 0.007 to 0.149. Recurrence is often high, including discounted expected repeats above one, so the result is not evidence that the policy eliminates reoffending. It only says the welfare comparison remains positive in these stress cases under the tested extension.

# NUMERICAL RISKS

The objective is non-smooth because recovery time, lifecycle transitions, clipping, and misconduct deterrence change discretely. Local meshes do not prove global optimality. Policy-bound hits are frequent. Normalization by an endogenous welfare range can change labels materially. Longer-horizon checks hold the audited policies fixed rather than re-optimizing them. These limits motivate continuous/action-solver and global-search checks in M7.

# WHAT SURVIVED

The sign of the two-state gain survives at all 13 suspicious large-gain points, nesting survives everywhere, two of three negligible cases remain exact counterexamples, and all seven recurrence stress cases retain positive longer-horizon fixed-policy comparisons.

# WHAT FAILED

The literal interpretation of 21 prediction/welfare coincidences fails under refinement. Several LARGE magnitudes shrink substantially. The bin counts are not structurally meaningful, and the audit does not certify global continuous optima.

# FINAL VERDICT

**M6 SURVIVES WITH REFRAMING — PROCEED TO M7.**

The defensible claim is regional and comparative: a simple two-state rule can outperform a globally searched constant rule in this model, but coarse-grid magnitude labels and exact prediction/welfare alignment should not be promoted as findings.
