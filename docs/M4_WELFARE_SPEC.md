# M4 Welfare Specification

## Canonical planner

The planner chooses one constant `phi` on the numerical domain `[0,.999]` for a finite horizon. Agents face the existing exogenous opportunity schedule and adverse-record agents choose productive effort separately for every candidate `phi`.

| Component | Symbol | Definition | Economic meaning / recipient | Transfer? | Counted? |
|---|---|---|---|---|---|
| Productive surplus | `S_t` | `output_value*A(R_t)*x_t` | Real output from allocated opportunity | No | Yes |
| Bad-match loss | `M_t` | `bad_match_cost*A(R_t)*(1-x_t)` | Real consumer/platform loss from allocating to low quality | No | Yes, negatively |
| Effort cost | `C_t` | `kappa*e_t^2/2` | Real rehabilitation disutility/resource cost | No | Yes, negatively |
| Misconduct harm | `L*d(phi)` | harm times clean-agent misconduct rate | Real harm imposed by misconduct | No | Yes, negatively |
| Opportunity payments/wages | — | omitted | Payment between sides | Yes | No |

The welfare function is

`W(phi)=sum_t beta^t E[S_t-M_t-C_t] - clean_share*L*d(phi)`.

No term rewards interiority and no direct administrative cost of memory is inserted. Consequently a boundary optimum is allowed.

## Population

The normalized benchmark has four equally weighted types: high-quality/accurate clean record, high-quality adverse record, low-quality adverse record, and low-quality favorable record. This deliberately contains correct and noisy histories without assigning group-specific welfare weights.

## Benchmarks

- `W_full`: policies are re-solved at every candidate `phi`.
- `W_fixed`: effort schedules are frozen at reference `phi=.5`.
- `W_no_rehab`: `alpha=0` and effort is disabled.
- `W_no_deterrence`: misconduct harm/channel removed.

`W_full-W_fixed` is a behavioral benchmark, not a uniquely additive causal decomposition because states and allocation interact.

## Half-life

For `0<phi<1`, `H=log(.5)/log(phi)`. At `phi=0`, memory is minimal and the reported half-life is zero periods. As `phi` approaches one, half-life diverges.
