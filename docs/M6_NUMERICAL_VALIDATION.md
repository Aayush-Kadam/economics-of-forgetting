# M6 Numerical Validation

- All 36 points satisfy `W(P3)>=W(P2)>=W(P1)>=W(P0)` within tolerance.
- All stored welfare values are finite.
- M5.5 effort grids 101–1001 select the same benchmark two-state rule and flexibility value.
- Smoke and full atlas commands are deterministic.
- Checkpoint CSV is rewritten after each completed design point.
- M4.5 showed coarse-action local peaks were mostly numerical artifacts; M6 does not report peak multiplicity.

Limitations: M6 uses a coarse memory grid, no interpolation/Bellman residual because policies are enumerated rather than solved by value-function iteration, and no stochastic simulation error because signals are deterministic.
