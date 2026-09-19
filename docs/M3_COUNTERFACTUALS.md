# M3 Counterfactual Worlds and Falsification Tests

All paired paths use the same current true quality and common future primitive shocks. The reported benchmark uses `phi=0.8`, `rho=0`, `alpha=0.7`, six transitions, and a transparent interior affine policy diagnostic.

| World | Intervention | Result |
|---|---|---|
| Full | Record affects repeated effort and effort affects quality | Quality gap: `0, .1470, .1248, .1060, .0900, .0764, .0648` |
| Information-only / fixed effort | Remove record dependence from effort | True-quality gap is zero; score gap remains |
| No productive effect | Set `alpha=0` | True-quality gap is zero; effort and score gaps may remain |
| Zero intrinsic persistence | Set `rho=0` | Multi-period quality gaps survive through repeated effort differences |
| Minimal memory | Set `phi=0` | Gap persists behaviorally but decays much faster in the benchmark |
| Random record | Draw `R` independently of current `x` | Full channel has reputation coefficient `.4996`; information-only placebo is approximately zero |

The full randomized-record world improves forecast MSE by `.2482` and has partial R-squared `.7974`; the information-only placebo improves MSE by only `1.5e-7` with partial R-squared `2.4e-6`.

## Self-confirming and self-correcting regions

With local `e_R>0`, a better record raises effort and future quality; equivalently, a worse record becomes self-confirming. With `e_R<0`, a worse record raises effort and is self-correcting. Both signs are executable and consistent with the M2 finding that nonlinear optimal effort can have either record/history sign. No global sign theorem is claimed.

## False-record experiment

The randomized-record experiment is the clean theoretical false-record design: current fundamentals are independent of the assigned record. Consequences alone create future predictive content in the full world and do not in the fixed-effort/information-only world.

Machine-readable results are in `experiments/m3_endogenous_persistence/counterfactual_results.json` and are regenerated with `python scripts/run_m3_counterfactuals.py`.

The M3.5 hostile audit adds a frozen endogenous-quality update. With `phi=0`, later gaps disappear after the first transition. With `phi=.8`, they survive through mechanical carryover of the original score. This separates the full feedback loop from a distinct inherited-record route; neither works without repeated record-dependent effort.
