# M7 horizon robustness

Re-optimized gains are positive at T = 3, 6, 12, 20, 30, and 50, ranging from 0.0193 to 0.1365. The preferred adverse-state memory declines from 0.99 at short horizons to 0.50 at T=50, while clean-state memory remains zero in these cases. For computational tractability, T=30 and T=50 suppress repeat offenses after the first; they are horizon checks, not recurrence checks.

The non-monotone gain and changing policy reject a stationary or horizon-invariant interpretation. No infinite-horizon Bellman solution was attempted. Terminal effects therefore remain a live limitation.

