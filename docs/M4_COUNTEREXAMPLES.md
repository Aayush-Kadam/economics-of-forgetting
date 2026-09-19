# M4 Counterexamples and Reversals

The seeded search evaluates 100 parameter vectors under both linear and logistic opportunity. It stores up to five examples per class in `experiments/m4_planner/counterexamples.json`.

## Rejected global claims

- Prediction-optimal memory is always longer: false; both orderings occur.
- Behavior-aware memory is always shorter: false; both orderings occur.
- The fixed-memory optimum is always interior: false; both boundaries occur.
- Welfare is unimodal: false; multiple local maxima occur.
- Greater rehabilitation productivity always shortens memory: not established and false as a protected intuition.
- Greater intrinsic persistence always lengthens memory: false in the benchmark sweep; `rho=0` chooses long memory while positive benchmark values choose short memory.

## Representative reversals

A logistic, two-period case selects welfare memory `phi=0` but prediction memory `.949`. A linear, two-period high-misconduct-harm case selects welfare memory near `.999` but prediction memory `0`. Other cases move the behavior-aware solution from near-permanent naive retention to zero, while a logistic eight-period case moves it from zero to `.654`.

These examples establish possibility, not prevalence. They prevent one-direction policy language.
