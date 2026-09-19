# M4 Planner Analysis

## Baseline solution

The benchmark selects `phi*=0`, so the fixed-memory optimum is the minimal-memory boundary. This is not forced: the objective contains no penalty centered at zero or interior target. The refined welfare is `.60545` normalized units.

The fixed-behavior, no-rehabilitation, no-deterrence, and prediction objectives also choose `phi=0` in the benchmark. Their welfare levels and components differ materially, so equality of the chosen boundary does not imply identical mechanisms.

## Regime variation

The comparative-static grid produces short, intermediate, long, and near-permanent optima. Examples include `rho=0` with `phi*=.795` (`H*=3.02`), high effort cost `kappa=3` with `phi*=.287` (`H*=.56`), low patience `beta=.75` with `phi*=.899` (`H*=6.54`), and horizon two with `phi*=.994` (`H*=114.4`). The default `rho x alpha` map is mostly short-memory, with one intermediate cell.

## Welfare margins

- Screening: longer memory can preserve useful initial sorting but also preserves erroneous histories; the allocation-output and bad-match terms jointly measure this.
- Deterrence: longer recovery delay can reduce misconduct, pushing toward longer retention, but clipping and the recovery formula create flat regions.
- Rehabilitation: memory changes the return to productive effort; its sign is state-dependent under logistic opportunity.
- Behavioral feedback: effort changes quality and future scores. Because M3 contains both sign regions, this margin can move the planner in either direction.

The margins are reported as welfare components and benchmark differences. They are not asserted to form a unique additive causal decomposition.

## Designer comparison

In the benchmark, prediction and welfare both choose minimal memory. Across 100 seeded, non-cherry-picked parameter draws, however, the search finds prediction-optimal memory both longer and shorter than welfare-optimal memory. It likewise finds the behavior-aware planner both shorter and longer than the fixed-behavior planner. Thus `phi_pred > phi_welfare` and `phi_naive > phi_full` are both false globally.

## Global search and non-concavity

Every reported optimum comes from a global coarse grid plus dense local refinement. Multiple local maxima appear in the seeded search, largely because bounded actions and the deterrence/recovery threshold create kinks. No unimodality assumption is used.

## Distributional incidence

At the baseline optimum, adverse-record types gain from rapid updating and productive rehabilitation, while clean types bear the separately allocated misconduct harm in the type-level accounting. The noisy favorable low-quality type has the lowest welfare. These are model-incidence results, not fairness conclusions.
