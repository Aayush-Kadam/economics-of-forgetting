# M4 Proof Audit

## M4-T1 — planner existence

**PROVED UNDER RESTRICTIONS.** On a compact domain `[0,bar_phi]`, `bar_phi<1`, continuous primitives and a unique continuous policy imply continuous welfare, so Weierstrass gives an optimum. The implemented finite grid also always has a maximizer. With nonunique policy ties or the open domain `[0,1)`, existence requires these restrictions and is not stated globally.

## M4-T2 — boundary versus interior memory

**NUMERICALLY CLASSIFIED.** The global search finds minimal, interior, and near-permanent regimes. No universal closed-form boundary condition survives the nonlinear, finite-horizon model.

## M4-T3 — deterrence comparative static

**PARTIAL / AMBIGUOUS.** Deterrence mechanically weakly favors memory within an unsaturated region, but changing misconduct harm does not move the baseline boundary optimum. Interactions with screening and rehabilitation prevent a global optimizer comparative static.

## M4-T4 — rehabilitation productivity

**FALSE AS A GLOBAL MONOTONIC CLAIM.** The benchmark alpha sweep remains at the short boundary, while the broader phase/counterexample search contains differing regimes. Higher productivity can make rehabilitation more valuable or make recovery easier; no global sign is established.

## M4-T5 — prediction versus welfare memory

**NUMERICALLY SUPPORTED DIVERGENCE; GLOBAL ORDERING FALSE.** Seeded cases exhibit both `phi_pred>phi_welfare` and `phi_pred<phi_welfare`.

## M4-T6 — endogenous behavior and retention

**NUMERICALLY SUPPORTED DIVERGENCE; GLOBAL ORDERING FALSE.** Behavior-aware memory is sometimes shorter and sometimes longer than fixed-behavior memory.

## Boundary and numerical audit

The solver includes both `phi=0` and values through `.999`, uses a coarse global grid, refines around the global candidate, and records grid-local maxima. M4.5 shows most apparent multiplicity disappears as the effort grid is refined, so those peaks are not treated as established economic maxima. Linear and logistic opportunity, horizons 2–10, `rho=0` and positive `rho`, multiple `alpha`, `kappa`, `beta`, misconduct-harm values, and a normalized four-type population are tested. All welfare components sum exactly in regression tests.

## Limitations

The policy is a finite-horizon reduced-form rolling optimization rather than a market equilibrium; signal-noise aggregation is represented through heterogeneous initial record errors rather than a full stochastic filter; comparative statics are numerical unless stated; and near-one optima are classified as near-permanent, not exact `phi=1` solutions.
