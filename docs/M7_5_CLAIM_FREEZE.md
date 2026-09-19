# M7.5 claim freeze

The classifications below are final ceilings for M8. `CORE` does not mean globally novel; it means necessary to the paper's argument.

## C1 — lifecycle asymmetry — CORE

- **Formal claim:** On a nonempty open set satisfying an interior clean-state misconduct threshold and the linear or regional smooth-opportunity effort condition, increasing common score persistence weakly lowers misconduct and strictly lowers productive post-event effort.
- **Plain English:** The same persistent record can strengthen discipline before an adverse event while weakening rehabilitation incentives afterward.
- **Model/version:** M2 finite-horizon score control problem.
- **Theorem/result ID:** M2-P5, supported by M2-P3 and M2-P4.
- **Assumptions:** reachable recovery; positive detection; unsaturated punishment; productive effort; interior strict optimum; linear opportunity or the stated local smooth inequality.
- **Status:** proved as regional existence; audited with counterexamples to globality.
- **Robustness:** analytical for linear access, regional for smooth access; not invariant to every timing convention.
- **Closest literature:** Bhaskar-Thomas; Elul-Gottardi; Board-Meyer-ter-Vehn.
- **Allowed wording:** “There exists a nonempty region in which persistence improves ex ante discipline while reducing post-event productive effort.”
- **Prohibited wording:** “Long memory always deters misconduct and suppresses rehabilitation.”
- **Main-text status:** central theorem and first contribution.

## C2 — regional rehabilitation comparative static — SECONDARY

- **Formal claim:** At a strict interior optimum, the sign of de*/dphi equals the sign of attenuation plus curvature relocation in M2-P3.
- **Plain English:** With nonlinear opportunity, longer memory may raise or lower rehabilitation effort depending on the state.
- **Model/version:** M1.5/M2 one-investment subproblem.
- **Theorem/result ID:** M2-P3.
- **Assumptions:** twice differentiable increasing opportunity, strict SOC, interior effort.
- **Status:** proved formula; both signs verified numerically.
- **Robustness:** boundaries and nonconcavity require global numerical checks.
- **Closest literature:** Board-Meyer-ter-Vehn; Bohren.
- **Allowed wording:** “The comparative static is regional and decomposes into attenuation and relocation.”
- **Prohibited wording:** “Persistence reduces rehabilitation under logistic opportunity.”
- **Main-text status:** mechanism supporting C1.

## C3 — zero-rho future-quality divergence — CORE

- **Formal claim:** If rho=0, alpha>0, and two records induce different effort, then their next-period quality gap is alpha times the effort gap.
- **Plain English:** Records can create differences in future fundamentals even when fundamentals have no intrinsic carryover.
- **Model/version:** M2/M3.
- **Theorem/result ID:** M2-P6, M3-P1.
- **Assumptions:** matched current fundamentals and shocks; productive, record-dependent effort.
- **Status:** proved identity.
- **Robustness:** vanishes at alpha=0 or equal effort; one-period unless effort differences recur.
- **Closest literature:** Board-Meyer-ter-Vehn; Bohren.
- **Allowed wording:** “The mechanism can operate at zero intrinsic persistence.”
- **Prohibited wording:** “Reputation creates permanent quality persistence from nothing.”
- **Main-text status:** second contribution.

## C4 — multi-period institutional feedback — SECONDARY

- **Formal claim:** The finite-horizon gap equals intrinsic carryover plus the distributed lag of effort gaps; at rho=0 repeated record-dependent effort can keep gaps nonzero.
- **Plain English:** Repeated responses to a public record can propagate a real quality difference over several periods.
- **Model/version:** M3.
- **Theorem/result ID:** M3-P2, M3-P3.
- **Assumptions:** linear quality law, common shocks, repeated score-dependent effort.
- **Status:** identity proved; persistence construction numerical/regional.
- **Robustness:** mechanical score carryover and endogenous score feedback are nonadditive routes.
- **Closest literature:** Bohren; Board-Meyer-ter-Vehn.
- **Allowed wording:** “Repeated effort differences can sustain finite-horizon gaps.”
- **Prohibited wording:** “The institution creates an infinite-horizon stationary persistence process.”
- **Main-text status:** extension of C3.

## C5 — self-confirming region — SECONDARY

- **Formal claim:** At matched fundamentals, a lower record reduces next quality locally when alpha e_R>0.
- **Plain English:** In some states a bad record depresses investment and helps validate itself.
- **Model/version:** M3/M3.5.
- **Theorem/result ID:** M3-P6.
- **Assumptions:** differentiable interior policy, strict SOC.
- **Status:** proved under restrictions and mapped numerically.
- **Robustness:** regional only.
- **Closest literature:** Board-Meyer-ter-Vehn; Bohren.
- **Allowed wording:** “A self-confirming region exists.”
- **Prohibited wording:** “Bad reputation is self-fulfilling.”
- **Main-text status:** mechanism result, not independent contribution.

## C6 — self-correcting region — SECONDARY

- **Formal claim:** At matched fundamentals, a lower record raises next quality locally when alpha e_R<0.
- **Plain English:** In other states a bad record induces compensating effort.
- **Model/version:** M3/M3.5.
- **Theorem/result ID:** M3-P6.
- **Assumptions/status/robustness/literature:** as in C5.
- **Allowed wording:** “Self-correcting regions coexist with self-confirming regions.”
- **Prohibited wording:** “Adverse reputation always causes recovery effort.”
- **Main-text status:** paired with C5.

## C7 — fixed-memory regime heterogeneity — APPENDIX

- **Formal claim:** Calibrated finite-horizon examples yield minimal, intermediate, long, and near-permanent fixed-memory optima.
- **Plain English:** The model has no universal optimal half-life.
- **Model/version:** M4/M6.
- **Theorem/result ID:** M4-T2.
- **Assumptions:** normalized population, finite horizon, reduced-form opportunity, tested grids.
- **Status:** numerical examples.
- **Robustness:** regional; classifications depend on thresholds.
- **Closest literature:** Sperisen; Elul-Gottardi; Gjerde-Slotnick.
- **Allowed wording:** “Different parameterizations select different retention regimes.”
- **Prohibited wording:** “The optimal half-life is interior.”
- **Main-text status:** appendix/counterexample.

## C8 — two-state contingent-memory value — APPENDIX

- **Formal claim:** In tested finite designs, an optimized clean/nonclean persistence pair weakly dominates the same-grid constant rule and is strictly better in many cases.
- **Plain English:** A simple lifecycle rule sometimes improves on one constant rate.
- **Model/version:** M5-M7.
- **Theorem/result ID:** M5-P1-P3, M6-A1.
- **Assumptions:** commitment, lifecycle flag, finite horizon, deterministic signals, reduced-form opportunity.
- **Status:** nesting proved; gains numerical and regional.
- **Robustness:** positive across implemented M7 families but can be negligible; timing and false-positive tests unresolved.
- **Closest literature:** Bhaskar-Thomas; Pei; Hamilton-Cui.
- **Allowed wording:** “The numerical exercise provides a secondary design illustration.”
- **Prohibited wording:** “State-contingent memory is generally optimal” or “earned forgetting.”
- **Main-text status:** appendix only.

## C9 — memory versus direct punishment — ROBUSTNESS

- **Formal claim:** In the M7 transfer benchmark, a strong direct penalty plus constant memory beats baseline two-state memory without a penalty, while contingency adds value conditional on the penalty.
- **Plain English:** Direct sanctions can substitute for memory; the computed instruments can also complement each other.
- **Model/version:** M7.
- **Theorem/result ID:** R-M7.5.
- **Assumptions:** costless enforceable transfer, no legal/liquidity constraint.
- **Status:** numerical.
- **Robustness:** instrument-grid specific.
- **Closest literature:** Jovanovic.
- **Allowed wording:** “The memory result is second-best and instrument-constrained.”
- **Prohibited wording:** “Memory dominates direct punishment.”
- **Main-text status:** limitation/appendix.

## C10 — prediction/welfare ordering ambiguity — APPENDIX

- **Formal claim:** Both orderings occur in numerical counterexamples; refined equality is uncommon.
- **Plain English:** Predictive accuracy does not determine welfare-optimal retention.
- **Model/version:** M4-M6.5.
- **Theorem/result ID:** M4-T5.
- **Assumptions:** model-specific numerical designs.
- **Status:** counterexamples, not a general characterization.
- **Robustness:** ordering remains bidirectional.
- **Closest literature:** information-retention and rating-design literatures.
- **Allowed wording:** “No fixed ordering appears in the model.”
- **Prohibited wording:** “Prediction-focused institutions remember too long.”
- **Main-text status:** appendix.

## Frozen architecture

M8 has two core contributions, not three: C1 and C3. C2 and C4-C6 supply the mechanism and regional qualification. C7-C10 are appendix or robustness material. All earned-forgetting, universal-half-life, global-stigma, universal designer-ordering, and memory-conflict claims are DROP.
