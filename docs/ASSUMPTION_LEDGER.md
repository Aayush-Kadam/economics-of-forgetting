# Assumption Ledger — M1

| Assumption | Economic interpretation | Mathematical role | Essential? | What breaks without it? | Planned robustness |
|---|---|---|---:|---|---|
| `0 <= phi <= 1` | Public records retain a fraction of prior reputation | Defines memory recursion | Yes | No ordered memory comparison | Alternative finite windows and Bayesian records in M7 |
| `0 <= rho <= 1` | True quality naturally persists | Separates natural from institutional persistence | No for M1 asymmetry; essential for longer-lived state effects | With `rho=0`, effort still changes next-period quality but the gap decays absent repeated effort | Repeated effort and shocks in M3 |
| `alpha > 0` | Rehabilitation is productive | Creates record-to-incentive-to-quality channel | Yes for institution-produced quality | At `alpha=0`, reputation may affect access but not future quality through effort | Placebo implemented |
| `0 < beta < 1` | Delayed opportunity is less valuable | Makes recovery delay economically costly | Essential for binary delay result | At `beta=1`, a pure delay with no flow loss does not reduce value | Add foregone flows and finite horizons |
| Convex cost `kappa e^2/2` | Increasing marginal rehabilitation cost | Gives interior continuous effort | Not essential for binary threshold; useful for smooth response | Linear costs generate corners | Alternative powers in M7 |
| Reputation-dependent opportunity | Employers/customers/lenders condition value on the public score | Links record to effort return | Essential | Constant opportunity yields zero reputation-induced effort | Placebo implemented |
| Opportunity is nonlinear for history divergence | Marginal returns vary across the reputation distribution | Allows identical fundamentals with different histories to choose different effort | Essential for the M1 history-gap example, not for `de*/dphi<0` | With an unclipped linear mapping, initial reputation shifts levels but not marginal effort | Hard, logistic, linear all tested |
| Constant favorable signal in Model 0 | Isolates score mechanics | Gives closed-form recovery time | Benchmark only | Endogenous signals require a control problem | Relaxed in Models 1–2 |
| One productive rehabilitation investment | Minimal post-event decision | Keeps M1 transparent | No | Repeated investment and option value are omitted | Dynamic program in M2/M3 |
| Uniform misconduct benefit | Heterogeneity smooths a binary decision into a probability | Produces differentiable aggregate misconduct | No | Homogeneous agents switch discretely at a threshold | Other distributions in M4/M7 |
| Detection probability is exogenous | Monitoring is not jointly designed in M1 | Isolates memory policy | No | Endogenous detection may substitute for persistence | Planner extension |
| Current quality imperfectly summarized by reputation | Market cannot fully bypass the record | Gives records economic force | Essential for history effects | Perfect observation removes public-history dependence | Placebo implemented |
| Strict local optimum for IFT results | The chosen effort is locally stable and interior | Makes the denominator in comparative statics positive | Essential for derivative formula | Corners and nonconcavity require global comparison | State map marks boundary/non-SOC cells |
| Unsaturated clean-state punishment | A clean agent has future opportunity to lose | Gives strict deterrence response | Essential for strict sign | Already-stigmatized agents may show zero deterrence | M2 lifecycle-state formulation |
| Institutional-score baseline | `R` is a published weighted score, not necessarily a posterior mean | Avoids false belief-consistency claims | Yes for M2 interpretation | A Bayesian model requires an additional filtering equation | Bayesian extension deferred |
| Exogenous opportunity schedule | Market maps score to opportunity without strategic feedback | Defines a control problem | Yes for current proofs | No equilibrium price consistency is established | Endogenize in later extension |
| Finite horizon for canonical proof | Dynamic problem ends after a specified number of periods | Makes existence and backward induction immediate | No conceptually; yes for current theorem scope | Infinite-horizon fixed-point claims remain unproved | M2 limitation; future contraction proof |
| Mean-zero shocks where invoked | Signals and states are unbiased conditional on actions | Preserves expected linear transitions | No for deterministic propositions | Nonlinear opportunity creates Jensen effects | Noise robustness remains partial |
| Common shocks in paired M3 worlds | Holds primitive uncertainty fixed | Makes the pathwise quality-gap identity causal inside the model | Yes for matched-world interpretation | Shock gaps enter as an additional term | Statistical simulation reported separately |
| Differentiable local effort policy in M3 | Summarizes the control response near a state | Defines `e_x`, `e_R`, and the Jacobian | Only for local results | Kinks/bounds require one-sided or global analysis | Bounds retained as flat counterexamples |
| Random record assignment | Removes informational correlation with current quality | Isolates consequences in the predictive experiment | Yes for clean falsification | Observational prediction mixes channels | Theoretical experiment only |
| Constant `phi` in M4 | One retention rule applies to all histories | Defines the fixed-memory planner | Yes for M4 | History-dependent rules may dominate | Deferred to M5 |
| Normalized four-type population | Transparent mix of accurate and erroneous records | Integrates regional feedback and screening | Yes for reported calibration | Optima can depend on type weights | Seeded parameter search and incidence table |
| Real-resource welfare accounting | Output, bad matches, effort, and misconduct are social objects | Avoids transfer double counting | Yes | Adding arbitrary penalties could manufacture interiority | Component table and exact-sum test |
| Numerical upper bound `.999` | Approximates near-permanent memory while retaining finite half-life | Makes search compact | Yes computationally | Exact `phi=1` remains a limiting case | Classified as near-permanent |
| Ex ante policy commitment in M5 | Institution announces lifecycle rule before behavior | Preserves deterrence promises | Yes for reported M5 | Discretion may create time inconsistency | Discretion not yet solved |
| Deterministic favorable signal for streak | Quality above threshold counts as favorable | Keeps earned rule transparent | No | Noise creates mistaken relief and gaming | Major M5 limitation |
| Finite lifecycle policy grid | Three persistence parameters and streak threshold | Avoids uninterpretable overfitting | Computationally | May miss continuous optima | Constant benchmark refined separately |
| M6 predeclared finite design | 36 structured parameter points | Makes coverage reproducible and interpretable | Yes for atlas frequencies | Does not represent a real-world distribution | Frequencies labeled as design fractions |
| Common coarse memory grid | `{0,.45,.85,.99}` for P0–P3 | Guarantees numerical nesting | Yes for M6 solver audit | Can miss continuous optima | M5.5 profiles and future refinement |
## M7 additions

- Direct penalties are perfectly enforced transfers with no collection or legal cost.
- M7 population heterogeneity is limited to two-point latent mixtures.
- T=30 and T=50 horizon checks disable repeat misconduct after the first offense for tractability.
- Continuous validation covers effort choices, not the full memory-policy surface.
- Unsupported stochastic signals, score rules, timing variants, and endogenous opportunity are not proxied.
