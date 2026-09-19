# M5.5 Hostile Audit

## MILESTONE

M5.5 — hostile identification audit of state-contingent memory

## STATUS

Complete.

## M5 ORIGINAL VERDICT

PASS WITH LIMITATIONS.

## POLICY TIMING AUDIT

In a clean state, `phi_clean` updates the clean score after quality realization. If misconduct occurs, the next score is reset to `R_bad` and the adverse regime begins; `phi_clean` does not determine punishment. In an adverse state, effort precedes quality, the applicable nonclean persistence updates the score, the favorable streak updates, and recovery may return the agent to clean status.

## ROLE OF φ_clean

It governs smoothing/adaptation of clean positive records and therefore allocation and forecast error. It does not weaken the adverse punishment triggered by misconduct. The optimum at zero is genuine but shallow: its one-dimensional welfare profile spans only about `.02` across the entire parameter range.

## ROLE OF φ_adverse

It governs adverse-score persistence, effort returns, recovery, and the reduced-form misconduct penalty. It is sharply identified near `.83-.85`; its profile spans about `2.73` welfare units.

## ROLE OF φ_rehab

It applies only after the streak threshold while the agent remains nonclean. Its profile has material variation, but at the benchmark optimum it equals `phi_adverse`, so the adverse/rehabilitation distinction does not affect memory.

## ROLE OF m

Holding the benchmark policy fixed, welfare, misconduct, and recurrence are identical for `m=1,...,6`. Because adverse and rehabilitation persistence are equal, the threshold is substantively irrelevant.

## MINIMAL SUFFICIENT POLICY CLASS

The benchmark is exactly the two-state rule `phi_clean=0`, `phi_nonclean=.85`. It is best interpreted as **memory activation after an adverse event**, not earned forgetting. It is close to a punishment-state model with a persistent public score; the separate score dynamics still affect allocation and prediction, but novelty relative to punishment flags is limited.

## WELFARE GAIN NORMALIZATION

Absolute gain: `.015895`; gain per agent-period: `.002649`; gain as a share of the feasible lifecycle-policy welfare range: `.00636` (0.64%). Baseline welfare is negative, so percentage gain relative to its level is not reported.

## PREDICTION GAIN AUDIT

MSE falls by `.005978`, or `8.85%`, inside the exact deterministic model. There is no sampling uncertainty or out-of-sample validation. The gain comes from faster clean-score adaptation, not better rehabilitation behavior: effort and quality match the fixed rule in the benchmark.

## HORIZON ROBUSTNESS

The two-state advantage is positive for horizons 3, 4, 6, 8, 12, and 20. Optimal nonclean persistence remains high; longer horizons select `phi_rehab=.99` on the reduced audit grid, showing that the exact three-state shape is horizon-sensitive even though state contingency survives.

## ACTION-GRID ROBUSTNESS

Effort grids 101, 201, 501, and 1001 select the same `(0,.85,.85,1)` rule and the same `.015895` flexibility value to numerical precision. Welfare levels vary by less than `.00085`.

## REPEAT-MISCONDUCT AUDIT

Economically admissible longer-horizon/high-benefit cases generate positive recurrence. At horizon 20, the zero-memory rule produces about `8.10` repeat events, while `(0,.85,.85,1)` produces about `.96`; persistent nonclean memory substantially limits rather than eliminates gaming.

## WHAT THE M5 RESULT ACTUALLY MEANS

Activating persistent score memory after an adverse event can outperform applying the same persistence to clean and nonclean histories. The benchmark gain is real, numerically stable, and modest. It is chiefly an allocation/prediction result combined with punishment persistence, not a rehabilitation-relief result.

## WHAT M5 DOES NOT SHOW

Earned forgetting, accelerated relief, a meaningful three-state threshold, large benchmark welfare gains, a commitment-versus-discretion theorem, or a policy recommendation.

## SCIENTIFIC RISKS

The rule may be representable as a punishment flag plus score normalization; the clean parameter is weakly identified; long-horizon policy grids are reduced; signals are deterministic; and the opportunity schedule is exogenous.

## FINAL VERDICT

**M5 SURVIVES WITH REFRAMING — PROCEED TO M6.**
