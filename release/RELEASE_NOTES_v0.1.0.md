# The Economics of Forgetting — Working Paper v0.1.0

**Author:** Aayush Kadam
**Status:** Working paper — external review version. Not peer reviewed, accepted, or journal-published.

## Paper

*Persistent Records and Rehabilitation Incentives* studies how persistence of an institutional score jointly affects discipline before an adverse event and productive rehabilitation afterward.

## Core contributions

1. There exists a nonempty region in which greater score persistence strengthens ex ante discipline while reducing productive post-event effort.
2. Record-dependent effort can create next-period quality differences at zero intrinsic quality persistence; repeated effort differences can propagate gaps over a finite horizon.

## Reproducibility

- Test suite: 54 tests passed.
- Core reproduction: `python scripts/reproduce_core.py`.
- Full reproduction: `python scripts/reproduce_full.py`.
- Validated runtimes on the release machine: about 35–72 seconds for core runs and 868.1 seconds for the full deterministic pipeline.

## Known limitations

The environment is finite horizon and uses a reduced-form opportunity schedule rather than a solved market equilibrium. The central comparative static is regional. Numerical design results are appendix-only and can be small.

The paper does not establish a universal benefit of forgetting, a universal optimal record half-life, a global self-fulfilling-reputation theorem, a fixed prediction-versus-welfare ordering, or dominance of memory over direct sanctions.

## External review

Version v0.1.0 is the first public external-review working paper. Journal submission remains gated on real theory-reader feedback and author approval.
