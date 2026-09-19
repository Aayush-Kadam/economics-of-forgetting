# M2 Independent Proof Audit

## Audit protocol

Analytical differentiation was checked against alternative algebra, boundary cases, deterministic random regression tests, and a seeded counterexample search. Numerical tests are bug detectors, not proofs.

## Proposition 1 — recovery dynamics

- **Statement:** under a constant favorable signal with `R<R_bar<y_G`, continuous recovery time is strictly increasing in `phi`.
- **Proof location:** `paper/appendix.tex`, Proposition 1.
- **Independent method:** direct recursion plus implicit threshold differentiation; 1,000 random admissible draws.
- **Counterexamples searched:** unreachable threshold, `phi` endpoints, already-recovered records.
- **Boundary cases:** integer recovery is stepwise; `phi=0` crosses in one update; `phi=1` never crosses.
- **Audit verdict:** **VERIFIED UNDER STATED CONDITIONS**.

## Proposition 2 — binary rehabilitation threshold

- **Statement:** an interior state-dependent memory threshold exists when rehabilitation cost lies between endpoint returns.
- **Proof location:** appendix, Proposition 2.
- **Independent method:** monotonic composition of `beta^n` and random order tests.
- **Counterexamples searched:** `beta=1`, costs outside the interior range, unreachable recovery.
- **Boundary cases:** thresholds disappear at low/high costs.
- **Audit verdict:** **VERIFIED UNDER STATED CONDITIONS**.

## Proposition 3 — continuous rehabilitation

- **Statement:** linear opportunity gives a global weak decrease in effort; a smooth nonlinear map gives a regional sign condition.
- **Proof location:** appendix, Proposition 3.
- **Independent method:** IFT derivation, symbolic term decomposition, finite differences at at least 20 regular interior draws, and 25,000-draw counterexample search.
- **Counterexamples searched:** positive logistic `de/dphi`, corners, nonconcavity, varying slopes.
- **Boundary cases:** effort bounds flatten comparative statics.
- **Audit verdict:** **VERIFIED UNDER STATED CONDITIONS**; global logistic version is false.

## Proposition 4 — clean-state deterrence

- **Statement:** record persistence weakly reduces misconduct for clean agents when the adverse continuation loss grows with recovery delay.
- **Proof location:** appendix, Proposition 4.
- **Independent method:** threshold derivation and 1,000 random order tests.
- **Counterexamples searched:** zero detection, saturated punishment, no access left to lose.
- **Boundary cases:** derivative is zero at aggregate probability bounds.
- **Audit verdict:** **VERIFIED UNDER STATED CONDITIONS**.

## Proposition 5 — lifecycle asymmetry

- **Statement:** a nonempty region exists where the common `phi` reduces both misconduct and productive rehabilitation.
- **Proof location:** appendix, Proposition 5.
- **Independent method:** intersection of Proposition 4's clean-state interior with Proposition 3's linear interior or smooth regional inequality.
- **Counterexamples searched:** positive logistic effort effects and punishment saturation.
- **Boundary cases:** not global across lifecycle states.
- **Audit verdict:** **VERIFIED UNDER STATED CONDITIONS**.

## Proposition 6 — record versus state memory

- **Statement:** even at `rho=0`, different records can generate different next-period quality through different productive effort.
- **Proof location:** appendix, Proposition 6.
- **Independent method:** substitution into `x'=alpha e(R)` and deterministic test.
- **Counterexamples searched:** linear opportunity, `alpha=0`, perfect observation.
- **Boundary cases:** without repeated effort, the gap need not persist beyond one period.
- **Audit verdict:** **VERIFIED UNDER STATED CONDITIONS**.

## Proposition 7 — minimal behavioral persistence

- **Statement:** history-induced effort differences generate a future state gap; without further effort the gap decays geometrically at rate `rho`.
- **Proof location:** appendix, Proposition 7.
- **Independent method:** difference equation and numerical path comparison.
- **Counterexamples searched:** equal marginal incentives and `rho=0` after the first period.
- **Boundary cases:** a persistent gap with `rho=0` requires repeated record-dependent effort.
- **Audit verdict:** **VERIFIED UNDER STATED CONDITIONS**.

