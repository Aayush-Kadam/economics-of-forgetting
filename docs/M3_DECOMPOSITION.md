# M3 Structural Decomposition

## Canonical timing and exact identity

The M2 law of motion remains

`x_{t+1}=rho*x_t+alpha*e_t+epsilon_{t+1}`.

For two matched worlds with common future primitive shocks,

`Delta x_{t+h}=rho^h Delta x_t + alpha sum_{j=0}^{h-1} rho^{h-1-j} Delta e_{t+j}`.

This follows by induction and is implemented both recursively and in closed form in `m3.py`. It is an exact state-equation decomposition, not a statistical or Shapley allocation. When `Delta x_t=0`, every later true-quality difference is behaviorally produced inside the model.

## Persistence objects

- Intrinsic persistence: propagation through `rho^h Delta x_t`.
- Record persistence: mechanical propagation through the score update and `phi`.
- Behaviorally produced persistence: the distributed lag of endogenous effort gaps.

These terms are not collapsed. The score gap can survive while the quality gap is zero, as the `alpha=0` and fixed-effort placebos show.

## Local dynamics

For state ordering `(x,R)` and a differentiable policy `e_t=e_t(x,R)`, the zero-shock local transition Jacobian is

```
J_t = [[rho + alpha*e_x,                  alpha*e_R],
       [(1-phi)*(rho + alpha*e_x), phi+(1-phi)*alpha*e_R]].
```

Its powers are finite-horizon propagation diagnostics only. No stationary equilibrium or infinite-horizon stability claim is made.

## Conditional predictiveness

M3 measures the incremental linear predictive content of current `R` for future `x`, after controlling for current `x`, using the reputation coefficient, forecast-MSE improvement, and partial R-squared. A randomized-record construction isolates consequences from information. This is a structural simulation estimand, not an empirical causal estimate.
