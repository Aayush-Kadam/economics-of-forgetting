# M5 Earned Forgetting

The restricted earned rule requires a common high persistence before the favorable-streak threshold and weakly lower persistence afterward. In the benchmark it collapses to the optimal constant policy: all persistence parameters equal `.85`, `m=1`, and value over fixed memory is zero.

General lifecycle contingency does strictly improve welfare by `.01590` normalized units: `(phi_clean,phi_adverse,phi_rehab,m)=(0,.85,.85,1)`. The gain comes from state-specific score updating and lower misallocation/prediction error, not accelerated post-rehabilitation forgetting. The supported object is therefore **state-contingent memory**, not a general earned-forgetting theorem.

Across the `alpha x misconduct-harm` map, flexibility value ranges from zero to `.437`. Several cells collapse to a constant rule; others use persistent adverse memory and low clean/rehabilitation memory. Policy shape is regional and often nonmonotone in primitives.
