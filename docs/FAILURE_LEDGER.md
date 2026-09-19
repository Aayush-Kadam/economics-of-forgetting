# Failure Ledger

| ID | Date | Stage | Attempt or risk | Evidence | Disposition |
|---|---|---|---|---|---|
| F-M0-001 | 2026-09-19 | M0 | Broad novelty conjecture: reputation memory affects effort and welfare. | Sperisen (2018), Bohren (2024), Board and Meyer-ter-Vehn (2013), Elul and Gottardi (2015), and Gjerde and Slotnick (2004) establish the main components. | **FALSE; framing dropped** |
| F-M0-002 | 2026-09-19 | M0 | “Reputation half-life” as new terminology. | Gjerde and Slotnick (2004) explicitly use the term. | **FALSE; terminology retained only descriptively** |
| F-M0-003 | 2026-09-19 | M0 | Direct Google Scholar forward-citation audit. | Google Scholar was not directly accessible in the research environment. | **OPEN LIMITATION; mandatory author-access check before public novelty claim** |
| F-M0-004 | 2026-09-19 | M0 | Recent fresh-rating paper fully inspected. | Hamilton and Cui (2024) was verified and abstract inspected; full theorem-level access was not obtained in this pass. | **OPEN HIGH-RISK COLLISION** |
| F-M0.5-001 | 2026-09-19 | M0.5 | Separation of record persistence from quality-effort persistence might be new. | Paulson Gjerde and Slotnick (2004) explicitly separate reputation half-life from the persistence of long-term quality efforts. | **FALSE; novelty claim prohibited** |
| F-M0.5-002 | 2026-09-19 | M0.5 | Hamilton–Cui might contain productive rehabilitation. | Author slides specify fixed provider quality and disintermediation; Theorem 1 concerns freshness, Lemma 2 disintermediation, and Theorem 3 revenue approximation. | **FALSE; partial rather than fatal collision** |
| F-M0.5-003 | 2026-09-19 | M0.5 | Broad “reputation causes future quality” feedback might be new. | Bohren; Board and Meyer-ter-Vehn; Hauser; and Paulson Gjerde–Slotnick already contain reputation-dependent real investment. | **FALSE; only retention-sensitive lifecycle joint result survives** |
| F-M0.5-004 | 2026-09-19 | M0.5 | Full appendices for both mandatory sources could be inspected directly. | SSRN automated access challenge blocked the Hamilton–Cui PDF; no lawful full manuscript of Paulson Gjerde–Slotnick was located. Author slides/code and detailed publisher text were used instead. | **ACCESS LIMITATION DISCLOSED** |
| F-M1-001 | 2026-09-19 | M1 | Initial reputation alone creates different effort under a linear opportunity map. | With `A(R)=a+bR`, `A'` is constant, so `R0` changes payoff levels but not the marginal return to effort. | **FALSE IN BASELINE; history divergence needs nonlinearity or another complementarity** |
| F-M1-002 | 2026-09-19 | M1 | Rehabilitation effort always decreases in record persistence under a logistic market response. | Persistence both attenuates new signals and relocates reputation along a nonconstant marginal-return curve; the effects can oppose each other. | **FALSE GENERALLY; CONDITIONALLY TRUE** |
| F-M1-003 | 2026-09-19 | M1 | A hard threshold is required for discouragement. | Closed-form linear opportunity yields `e* proportional to 1-phi^T`, decreasing in persistence. | **FALSE; smooth and linear survival confirmed** |
| F-M1-004 | 2026-09-19 | M1 | Bad reputation always lowers rehabilitation effort relative to good reputation. | Under a logistic response, a worse record can move the agent closer to the steep region and increase effort; sufficiently bad records instead have low marginal returns. | **FALSE GENERALLY; regime-dependent** |
| F-M1-005 | 2026-09-19 | M1 | `rho=0` kills behavioral persistence. | Different reputation histories still induce different effort and hence different next-period quality when `alpha>0`; without repeated effort the gap then disappears. | **FALSE; record memory can create transient state persistence** |
| F-M1-006 | 2026-09-19 | M1 | M1 identifies institution-produced statistical predictiveness. | The model establishes a causal pathway but contains no estimable information/behavior decomposition. | **NOT ESTABLISHED; deferred to M3** |
| F-M1.5-001 | 2026-09-19 | M1.5 | T5 is globally valid across reputation states. | Deterrence saturates for agents with no opportunity left to lose; logistic rehabilitation has positive-derivative regions. | **FALSE GLOBALLY; reframed as regional** |
| F-M1.5-002 | 2026-09-19 | M1.5 | Logistic nonmonotonicity is a numerical artifact. | Independent IFT derivation yields an attenuation term and an opposing curvature-relocation term. | **FALSE; analytical state dependence verified** |
| F-M1.5-003 | 2026-09-19 | M1.5 | Patience near one eliminates all discouragement. | It eliminates pure-delay binary discouragement, but not fixed-horizon attenuation of the score response. | **MODEL-DEPENDENT** |
| F-M1.5-004 | 2026-09-19 | M1.5 | Nearly free or extremely productive rehabilitation preserves smooth comparative statics. | Effort hits bounds or little effort is required, flattening or reversing local responses. | **FALSE AT BOUNDARIES** |
| F-M2-001 | 2026-09-19 | M2 | The canonical baseline can be called a market equilibrium. | Opportunity is an imposed score schedule; no belief or price consistency condition is solved. | **FALSE; labeled dynamic control problem** |
| F-M2-002 | 2026-09-19 | M2 | Smooth-market lifecycle asymmetry is global. | Seeded search finds interior parameter sets with positive `de/dphi`. | **FALSE; regional theorem only** |
| F-M2-003 | 2026-09-19 | M2 | `rho=0` alone produces indefinitely persistent true-quality gaps. | One-time effort creates only a next-period gap; persistence needs repeated record-dependent effort. | **FALSE WITHOUT REPEATED EFFORT** |
| F-M2-004 | 2026-09-19 | M2 | Finite-horizon propositions automatically extend to an infinite horizon. | No contraction/uniqueness and differentiability proof for the infinite-horizon policy was completed. | **UNPROVED; scope restricted** |
| F-M2-005 | 2026-09-19 | M2 | Mean-zero signal noise is innocuous for all results. | Linear expected scores are preserved, but nonlinear opportunity introduces Jensen effects. | **PARTIAL ONLY** |
| F-M3-001 | 2026-09-19 | M3 | Bad reputation is always self-confirming. | Negative local effort response to reputation creates a self-correcting region; bounds create flat regions. | **FALSE GLOBALLY; SIGN-DEPENDENT** |
| F-M3-002 | 2026-09-19 | M3 | Multi-period quality persistence at `rho=0` follows from record persistence alone. | It disappears under fixed effort and `alpha=0`; repeated behavior is essential. | **FALSE WITHOUT THE PRODUCTIVE BEHAVIORAL CHANNEL** |
| F-M3-003 | 2026-09-19 | M3 | Predictive content of reputation is automatically causal. | Informational content and behavior must be separated; only the randomized-record matched-world construction isolates production here. | **FALSE GENERALLY; STRUCTURALLY ISOLATED ONLY** |
| F-M3-004 | 2026-09-19 | M3 | Local Jacobian roots establish an infinite-horizon equilibrium. | The canonical model is finite horizon and the policy schedule is imposed. | **FALSE INTERPRETATION; DIAGNOSTIC ONLY** |
| F-M3.5-001 | 2026-09-19 | M3.5 | Endogenous quality-to-record feedback is necessary for every multi-period zero-`rho` effect. | With `phi>0`, the inherited record mechanically survives and repeatedly changes effort even when quality is removed from future score updates. | **FALSE; ALTERNATE MECHANICAL-CARRYOVER ROUTE** |
| F-M4-001 | 2026-09-19 | M4 | A defensible baseline must have an interior optimal half-life. | Primitive welfare accounting selects `phi=0` in the normalized benchmark. | **FALSE; BOUNDARY RESULT RETAINED** |
| F-M4-002 | 2026-09-19 | M4 | Prediction-focused design always retains history longer than welfare design. | Seeded search finds both longer and shorter prediction optima. | **FALSE GLOBALLY; REGIME-DEPENDENT** |
| F-M4-003 | 2026-09-19 | M4 | Ignoring behavioral feedback always biases retention upward. | Full versus fixed-policy search moves the optimum in both directions. | **FALSE GLOBALLY; REGIME-DEPENDENT** |
| F-M4-004 | 2026-09-19 | M4 | Welfare is unimodal in memory. | Bounded actions and deterrence/recovery kinks generate multiple grid-local maxima. | **FALSE IN GENERAL** |
| F-M4.5-001 | 2026-09-19 | M4.5 | Continuous recovery delay can be used for positive `phi` while assigning one discrete period at `phi=0`. | This creates a spurious boundary discontinuity; integer recovery is required throughout the discrete model. | **IMPLEMENTATION INCONSISTENCY CORRECTED PROSPECTIVELY** |
| F-M4.5-002 | 2026-09-19 | M4.5 | Numerous local maxima are robust economic nonlinearities. | Peak counts collapse from dozens to zero-to-two as the effort grid is refined. | **MOSTLY NUMERICAL ROUGHNESS; STRONG CLAIM WITHDRAWN** |
| F-M5-001 | 2026-09-19 | M5 | Earned forgetting strictly improves on optimal fixed memory. | The restricted earned rule chooses identical `.85` persistence in all lifecycle states. | **FALSE IN BENCHMARK** |
| F-M5-002 | 2026-09-19 | M5 | Optimal adaptive memory necessarily forgets rehabilitated agents faster. | Benchmark has `phi_rehab=phi_adverse=.85`. | **FALSE IN BENCHMARK** |
| F-M5-003 | 2026-09-19 | M5 | M5 establishes commitment/time inconsistency. | No discretionary planner is solved. | **NOT ESTABLISHED** |
| F-M5.5-001 | 2026-09-19 | M5.5 | The benchmark is a meaningful three-state earned-forgetting rule. | `phi_adverse=phi_rehab`; welfare is exactly flat in `m`. | **FALSE; COLLAPSES TO TWO-STATE MEMORY ACTIVATION** |
| F-M5.5-002 | 2026-09-19 | M5.5 | The benchmark flexibility gain is economically large. | Gain is only 0.64% of the feasible policy-welfare range. | **FALSE; SMALL BUT NUMERICALLY STABLE** |
| F-M6-001 | 2026-09-19 | M6 | Memory-conflict dispersion is a sufficient statistic for adaptive value. | Design correlation is approximately `-.09`. | **FAILED; INDEX NOT RETAINED AS ORGANIZING RESULT** |
| F-M6-002 | 2026-09-19 | M6 | Restricted earned relief can be placed above P2 in a nested complexity ladder. | It is not a superset of P2. | **CLASSIFICATION ERROR CORRECTED; EARNED FAMILY REPORTED SEPARATELY** |
## M7 failures and unresolved tests

- F-M7.1: the result is not uniquely a memory result; the state variable is an adverse lifecycle punishment flag.
- F-M7.2: alternative within-period timing was not solved.
- F-M7.3: false positives and non-deterministic signal families were not solved.
- F-M7.4: rolling windows, hard expiration, and bounded-history averages were not solved.
- F-M7.5: continuous global optimization of the full memory policy was not certified.
- F-M7.6: current-state observability and endogenous opportunity were not solved.
