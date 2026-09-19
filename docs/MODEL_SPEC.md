# M1 Model Specification

## Purpose

M1 asks whether one public-memory parameter can discourage misconduct before a bad record yet reduce productive rehabilitation afterward. It is deliberately not a full equilibrium or planner model.

## Players

1. A long-lived agent who may commit misconduct and, after an adverse record, invest in rehabilitation.
2. A competitive or reduced-form market that maps public reputation into opportunity value.
3. A future planner who may choose record persistence; the planner is not active in M1.

## Three distinct persistence objects

- `phi`: persistence of the public record.
- `rho`: intrinsic persistence of actual quality.
- `alpha`: productivity of current rehabilitation effort in raising future quality.

They never share a parameter.

## Timeline

```text
t=-1                 t=0                         t=1,...,T
private misconduct   adverse signal/record       record updates from outcomes
d in {0,1}     --->  R0 observed          --->   market opportunity A(R)
   |                     |                         |
   | detection p         rehabilitation e         future underlying quality x
   +--------------------> x1=rho*x0+alpha*e ------+
```

## Model 0: deterministic recovery

For constant favorable behavior `y_G > R_bar` after an adverse record `R_0 < R_bar`,

`R_{t+1}=phi R_t+(1-phi)y_G`,

so

`R_t=y_G+phi^t(R_0-y_G)`.

Let `q=(y_G-R_bar)/(y_G-R_0)` in `(0,1)`. The continuous crossing time is

`n(phi)=log(q)/log(phi)`

and the first integer crossing time is `N(phi)=ceil(n(phi))`. For `0<phi<1`,

`dn/dphi=-log(q)/[phi(log phi)^2] > 0`.

At `phi=0`, the integer recovery time is one update; as `phi` approaches one, recovery time diverges.

## Model 1: binary rehabilitation

The agent pays `C` to generate the favorable recovery path and receives opportunity value `V` upon recovery. Rehabilitation is chosen iff

`beta^{n(phi)} V >= C`.

Because `n(phi)` is strictly increasing and `0<beta<1`, the left side is strictly decreasing. An interior critical persistence exists when the cost lies between the endpoint values. The exact continuous threshold solves

`n(phi_bar)=log(C/V)/log(beta)`.

This model proves delay-induced rehabilitation collapse but does not yet prove a productive-state effect.

## Model 2: productive continuous rehabilitation

The adverse-history agent chooses `e in [0,1]` at cost `kappa e^2/2`. Actual quality becomes

`x_1=rho x_0+alpha e`.

Holding that post-investment quality signal fixed through horizon `T`, public reputation is

`R_T=phi^T R_0+(1-phi^T)x_1`.

The reduced-form objective is

`U(e)=beta^T V A(R_T)-kappa e^2/2`.

For an interior solution,

`kappa e=beta^T V A'(R_T)(1-phi^T)alpha`.

For an unclipped linear mapping `A(R)=a+bR`,

`e*(phi)=beta^T V b alpha(1-phi^T)/kappa`, clipped to `[0,1]`,

which weakly decreases in `phi` and is strictly decreasing when interior. Thus a discontinuous access threshold is not necessary for the basic discouragement result.

For a logistic mapping, the sign is generally ambiguous because `phi` changes both the weight on new quality and the location at which `A'` is evaluated. Numerical global optimization is used only to map those regimes.

For a strict interior optimum define `m=phi^T`, `x_1=rho x+alpha e`, and `r=mR+(1-m)x_1`. Implicit differentiation gives

`e_phi = beta^T V alpha T phi^{T-1}[-A'(r)+(1-m)A''(r)(R-x_1)] / D`,

where `D=kappa-beta^T V[alpha(1-m)]^2A''(r)>0` is the second-order-condition denominator. The first term is signal-weight attenuation; the second is curvature-driven relocation along the opportunity schedule.

## Market opportunity functions

- Hard: `A(R)=1{R>=R_bar}`.
- Logistic: `A(R)=1/[1+exp(-k(R-R_bar))]`.
- Linear: `A(R)=clip(a+bR,0,1)`.
- Placebo: constant opportunity.
- Perfect-observation placebo: the market applies the logistic map to `x_1`, not `R_T`.

## Model 3: pre-event misconduct

Misconduct yields private benefit `b` and is detected with probability `p`. Detection produces `R_bad`. The reduced-form penalty from waiting rather than obtaining immediate access is

`P(phi)=V[1-beta^{n(phi)}]`.

An agent commits misconduct iff `b >= pP(phi)`. With `b` uniform on `[0,b_max]`,

`Pr(d=1)=clip(1-pP(phi)/b_max,0,1)`,

which weakly decreases in `phi` and is strictly decreasing in the interior because `n'(phi)>0`.

## Equilibrium concept

M1 uses optimal individual decisions against a specified opportunity mapping and aggregation rule. It is a partial-equilibrium mechanism test, not a rational-expectations market equilibrium. Belief consistency and planner optimization are deferred.

## Eventual planner object

Later milestones may choose `phi` or a history-contingent rule to balance screening, misconduct, productive rehabilitation, exclusion, and effort costs. No optimal-memory claim is made in M1.

## M2 canonical dynamic model

M2 embeds the benchmarks in a finite-horizon score-based dynamic control problem. The public state is `s_t=(R_t,x_t,z_t)`, where `z_t` is clean or adverse. The institutional score is not asserted to be a Bayesian posterior.

Within a period: the state is observed; opportunity `A(R_t)` is assigned; a clean agent may choose misconduct while an adverse agent chooses productive effort; flow payoffs occur; quality evolves as `x_{t+1}=rho x_t+alpha e_t+epsilon`; signal `y_{t+1}=x_{t+1}+eta` is generated; and the score updates as `R_{t+1}=phi R_t+(1-phi)y_{t+1}`.

The adverse-state Bellman equation is

`V_t^A(R,x)=max_e {v A(R)-kappa e^2/2 + beta E[V_{t+1}^A(R',x')]}`.

The clean-state misconduct threshold compares private benefit with the detection-weighted continuation loss from entering the adverse state. Because the market schedule is imposed rather than derived from beliefs, the baseline is a dynamic control problem, not a competitive or Bayesian equilibrium.

### Four-stage causal decomposition

1. Direct memory: `phi` changes the inherited weight in `R'` holding behavior and signals fixed.
2. Behavioral response: `phi` changes optimal effort.
3. State effect: changed effort changes `x'` through `alpha` and subsequently through `rho`.
4. Feedback: changed `x'` changes later signals and therefore later scores.

M2 proves building blocks for this sequence but does not estimate a statistical predictiveness decomposition.

## M3 institution-produced persistence layer

M3 keeps the M2 timing and compares paired worlds with the same current quality and future primitive shocks but different public scores. Iterating the quality law gives

`Delta x_{t+h}=rho^h Delta x_t+alpha sum_{j=0}^{h-1} rho^{h-1-j} Delta e_{t+j}`.

Thus, when `Delta x_t=0`, future divergence is entirely behaviorally produced. At `rho=0`, multi-period divergence is possible only if score-dependent effort differences recur. Information-only/fixed-effort and `alpha=0` worlds preserve possible score gaps but eliminate true-quality gaps.

For a differentiable policy `e_t(x,R)`, M3 uses the local `(x,R)` transition Jacobian only as a finite-horizon propagation diagnostic. Predictiveness is measured conditionally on current `x`; randomized record assignment distinguishes consequences of the score from its informational content. Full definitions and limitations are in `M3_DECOMPOSITION.md`.

## M4 constant-memory planner

M4 chooses one `phi` on `[0,.999]` and re-solves finite-horizon adverse-agent policies for every candidate. Social welfare counts real allocated output, real low-quality allocation loss, productive effort cost, and misconduct harm. Opportunity payments are transfers and are omitted. The normalized population includes accurate and erroneous clean/adverse records.

The fixed-behavior, `alpha=0`, no-deterrence, and prediction-MSE designers are evaluated on the same state system. The optimizer uses a global grid and local refinement without assuming concavity. Full accounting is in `M4_WELFARE_SPEC.md`.

## M5 lifecycle memory

M5 replaces constant `phi` with a precommitted tuple `(phi_clean,phi_adverse,phi_rehab,m)`, where `m` is a favorable-signal streak threshold. The state adds lifecycle, streak, and offense count. Adverse events reset the streak; score recovery after credible signals returns the agent to clean status; repeated misconduct is permitted. Constant memory is nested by equality of all persistence parameters.

## M6 computational model family

M6 freezes P0 constant, P1 clean/nonclean, P2 clean/adverse/rehab, and P3 threshold lifecycle policies. The atlas uses exact finite-horizon probability trees and a predeclared parameter design. P0–P3 are nested; restricted earned relief is reported separately. Frequencies are computational-design frequencies, not probabilities.
## M7 extension

M7 permits `opportunity = hard` in addition to logistic and linear access. It also introduces a nonnegative `direct_penalty` that enters the detected-misconduct deterrence threshold and is treated as a transfer, so it is excluded from social welfare. Defaults are unchanged. The extension is a robustness benchmark, not a new canonical model.
