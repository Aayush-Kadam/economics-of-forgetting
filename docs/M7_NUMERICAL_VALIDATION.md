# M7 numerical validation

The deterministic battery contains 61 re-optimized cases on a common six-point memory mesh. All 61 satisfy policy-class nesting and all outputs are finite. A 501-point effort mesh was compared with bounded local and seeded global continuous optimization at 12 representative state-policy combinations; the maximum effort difference is 0.000972. This validates the action discretization locally, not the global two-dimensional memory optimum.

M6.5 separately used an effort grid of 301 and local memory meshes. Boundary optima remain common, so continuous memory optimality is not certified. The full suite passes 52 tests.

