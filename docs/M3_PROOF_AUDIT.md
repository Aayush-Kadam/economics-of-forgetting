# M3 Proof Audit

| Target | Status | Scope and audit finding |
|---|---|---|
| M3-P1 one-period divergence | **PROVED** | `Delta x_{t+1}=alpha Delta e_t` when current quality and shocks match. Requires `alpha>0` and a policy gap. |
| M3-P2 multi-period propagation | **PROVED** | Exact finite-horizon induction identity; numerically regression-tested. |
| M3-P3 zero-`rho` produced persistence | **PROVED BY CONSTRUCTION** | At `rho=0`, every period's gap equals `alpha Delta e`; repeated record-dependent effort sustains multiple nonzero gaps. Not guaranteed under every policy. |
| M3-P4 local effective persistence | **PROVED LOCALLY** | Exact Jacobian for a differentiable policy; eigenvalues are diagnostics, not infinite-horizon equilibrium objects. |
| M3-P5 conditional produced predictiveness | **VERIFIED STRUCTURALLY** | Randomized record has predictive content only when the record changes productive effort. Statistical result is simulation-specific, not an empirical identification theorem. |
| M3-P6 self-confirming/self-correcting regions | **PROVED CONDITIONALLY** | Sign is `sign(alpha*e_R)` at matched fundamentals. Both policy-slope regions exist; global monotonicity is false. |

M3.5 sharpens P6 for the strict-interior one-investment problem: `sign(e_R)=sign(A''(r))`; the logistic boundary is the opportunity midpoint. It also shows that endogenous quality-to-score updating is sufficient but not necessary for repeated effort gaps when `phi>0`, because mechanical score carryover is an alternate route.

## Placebo audit

- `alpha=0`: passed; true-quality effects vanish.
- reputation-independent/fixed effort: passed; true-quality effects vanish while mechanical score persistence remains.
- `rho=0`: passed; repeated behavioral feedback alone sustains multi-period gaps.
- minimal memory: passed; the initial treatment still has a one-step effect, but propagation is sharply weaker in the benchmark.
- randomized reputation: passed; consequences create conditional predictiveness in the full world.
- perfect/current-state information: represented by conditioning directly on current `x`; the randomized record adds no predictive content in the information-only world.

## Boundaries

Clipping can make `e_R=0`, so effects become flat at effort bounds. A negative policy response reverses rather than merely weakens the result. Common-shock identities do not allocate nonlinear statistical interactions, and the benchmark does not establish a general Shapley decomposition. These are retained limitations rather than hidden assumptions.
