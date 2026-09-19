# M5 Proof Audit

## M5-P1 — nesting

**PROVED.** `phi_clean=phi_adverse=phi_rehab=phi` reproduces a constant-memory rule. Optimization over a class containing those vectors weakly dominates optimization over the same constant grid.

## M5-P2 — strict value of contingency

**PROVED FOR FINITE STATE/ACTION SETS.** If two positive-weight reachable states have different unique maximizing memory actions, the sum of statewise maxima strictly exceeds the best common action. The executable `strict_contingency_gain` test verifies the constructive argument. Application to the calibrated dynamic model is numerical.

## M5-P3 — lifecycle conditionality

**NUMERICALLY SUPPORTED.** The benchmark lifecycle rule strictly beats the globally searched constant rule by `.01590`, using clean persistence zero and adverse persistence `.85`.

## M5-P4 — accelerated forgetting after rehabilitation

**FAILS IN THE BENCHMARK.** The restricted earned rule collapses to constant memory.

## M5-P5 — gaming condition

**PARTIAL ONLY.** Streak reset and repeat offenses are implemented; no benchmark cycle occurs. No analytical cycling boundary is proved.

## M5-P6 — commitment/time inconsistency

**NOT ESTABLISHED.** Only commitment is solved.

## M5-P7 — simple rule efficiency

**PARTIAL.** The three-regime lifecycle rule is the most general solved policy ceiling, so a distinct full dynamic-policy denominator is unavailable.
