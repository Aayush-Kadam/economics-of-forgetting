# M1 Phase Report

## MILESTONE

M1 — minimal model skeleton

## STATUS

COMPLETE

## VERDICT

PASS WITH LIMITATIONS

## M0.5 COLLISION VERDICT

PROCEED TO M1 WITH FURTHER NARROWING.

## FINAL SURVIVING NOVELTY CLAIM

Candidate only: one explicit record-memory parameter can jointly strengthen pre-event discipline and weaken post-event productive rehabilitation, with the latter changing a distinct underlying state. Neither component nor reputation-induced quality investment is novel alone.

## MODEL SUMMARY

Four nested benchmarks separate mechanical recovery, binary rehabilitation, continuous productive effort, and heterogeneous misconduct. Public record persistence `phi`, intrinsic state persistence `rho`, and rehabilitation productivity `alpha` are distinct throughout.

## TIMING

Misconduct precedes a possible adverse record; after the record, the agent chooses rehabilitation; productive effort changes true quality; signals update public reputation; market opportunity depends on reputation.

## CORE EQUATIONS

`R_t=y_G+phi^t(R_0-y_G)`; `x_1=rho x_0+alpha e`; `R_T=phi^T R_0+(1-phi^T)x_1`; `U(e)=beta^T V A(R_T)-kappa e^2/2`.

## KEY ASSUMPTIONS

Discounting, productive rehabilitation, reputation-dependent opportunity, convex effort cost, and imperfect current-quality observation. Nonlinearity is required for history-specific marginal effort gaps in the one-investment model, but not for effort to decrease with persistence.

## ANALYTICAL RESULTS

Recovery time increases in `phi`; binary rehabilitation admits a critical persistence; linear-market effort decreases in `phi`; and misconduct probability decreases in `phi` in the interior.

## COUNTEREXAMPLES FOUND

Logistic effort is not globally monotone; bad reputation need not always discourage effort; linear opportunity eliminates history-level effort differences; and `rho=0` does not eliminate a next-period behavioral gap.

## LIFECYCLE ASYMMETRY RESULT

The reduced-form model proves coexistence: higher `phi` lowers misconduct probability and lowers productive rehabilitation effort. The result is economically transparent but partly mechanical, and general-equilibrium robustness is untested.

## RECORD MEMORY VS STATE PERSISTENCE

`phi` affects how records absorb new outcomes; `rho` carries actual quality forward; `alpha` governs whether effort changes actual quality. The deterrence result uses `phi`; persistence of the induced quality gap depends on `rho` and repeated effort.

## PLACEBO RESULTS

At `alpha=0`, the future-quality channel vanishes. Constant opportunity eliminates reputation-induced effort. `phi=0` makes records immediately responsive. At `rho=0`, a next-period effort-created gap survives but subsequently decays in the one-investment model. Perfect observation removes the effect of public history on effort.

## THEOREMS / RESULTS STATUS

T1–T4 proved in their stated reduced-form environments; T5 proved as coexistence in M1; T6 numerically supported and conditionally true; T7 untested.

## KEY FILES CREATED

`docs/MODEL_SPEC.md`, `docs/ASSUMPTION_LEDGER.md`, source modules, deterministic tests, and the M1 figure builder.

## TEST STATUS

15 deterministic tests passed. Closed-form paths, recovery boundaries, state transitions, all required placebos, deterrence, smooth-market history divergence, and reproducibility were checked.

## FIGURES CREATED

Recovery time, effort by history, lifecycle asymmetry, and underlying-state paths.

## WHAT SURVIVED

Mechanical recovery, a binary rehabilitation threshold, smooth-market discouragement, ex ante deterrence, and a minimal effort-to-future-quality pathway.

## WHAT FAILED

Global logistic monotonicity, automatic history divergence under linear opportunity, and any M1 claim to a statistical predictiveness decomposition.

## SCIENTIFIC RISKS

Partial-equilibrium timing may make T5 too mechanical; nonlinear opportunity is needed for reputation-history traps; prior work already owns most primitives; quantitative importance is unknown.

## REPOSITORY STATE

Source, tests, documents, and four code-generated figures are reproducible; pending final clean commit.

## CURRENT COMMIT

To be recorded by Git.

## CURRENT TAG

`m1-model-skeleton` only after tests pass.

## DECISION

Proceed to M2 with the narrowed joint proposition, while treating T6 and any predictiveness claim as unresolved.

## NEXT MILESTONE

M2 — formal dynamic theory, equilibrium consistency, and proof audit.
