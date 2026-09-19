# The Economics of Forgetting

**Author:** Aayush Kadam

**Working paper:** *Persistent Records and Rehabilitation Incentives*

## Abstract

Past behavior can predict future behavior and discipline current actions. When agents can invest in changing their future productive state, however, a persistent public record also changes the return to that investment. I study a finite-horizon dynamic control problem that separates persistence of an institutional score from persistence of underlying quality. On a nonempty region, greater score persistence strengthens ex ante discipline while reducing productive effort after an adverse history. Records can consequently produce differences in future quality rather than merely reveal them: even with zero intrinsic quality persistence, different records generate different next-period quality whenever they induce different effort. Repeated score-dependent effort can propagate these differences over a finite horizon. The feedback is regional. Depending on the local geometry of opportunity, an adverse record can suppress or stimulate effort, producing self-confirming and self-correcting regions. A secondary numerical exercise finds that lifecycle-contingent persistence can outperform a constant rule in parts of parameter space, but gains can be small and direct punishment can substitute for memory. The paper therefore establishes neither a universal case for forgetting nor a universal optimal record duration.

## Paper

[Download the working-paper PDF](paper/manuscript.pdf).

**Status:** Working paper — external review version v0.1.0. It has not been peer reviewed, accepted, or published by a journal.

## Main results

- Regional lifecycle asymmetry: one persistence parameter can deter misconduct and weaken post-event productive effort.
- Institution-produced outcomes: record-dependent effort can create next-period quality gaps at zero intrinsic persistence, with finite-horizon propagation when effort differences recur.

## Repository structure

- `src/economics_of_forgetting/`: model and numerical routines.
- `tests/`: analytical identities, counterexamples, solver nesting, and regression cases.
- `scripts/`: milestone experiments, PDF build, and reproduction entry points.
- `outputs/`: generated figures and tables.
- `experiments/`: deterministic metadata and checkpoints.
- `paper/`: manuscript source, appendix, bibliography, and local review PDF.
- `docs/`: claim freeze, audits, ledgers, referee report, and phase reports.
- `external_review/`: optional one-page research brief.
- `release/`: working-paper release and preprint-policy metadata.

## Installation

Python 3.10 or later is required.

```text
python -m pip install -e .[test]
```

The fallback PDF builder also requires `reportlab`, `pypdf`, and `pypdfium2`.

## Reproduction

Core paper results, tests, figures, tables, and PDF:

```text
python scripts/reproduce_core.py
```

Full deterministic milestone package:

```text
python scripts/reproduce_full.py
```

The validated local core runtime is about 72 seconds. The full command includes the M6 atlas, M6.5 audit, and M7 battery; the validated M8 run took about 14.5 minutes (868.1 seconds). Runtime depends on hardware and software versions.

## Tests

```text
python -m pytest -q
```

## Paper build

```text
python scripts/build_paper.py
```

The canonical source is `paper/manuscript.tex`. The local fallback builder produces `paper/manuscript.pdf` without requiring a system LaTeX installation.

## License

Copyright (c) 2026 Aayush Kadam. All rights reserved. No reuse or redistribution license is granted at this stage.

## Citation

Citation metadata are provided in `CITATION.cff`. Cite version v0.1.0 as a working paper and reproducibility package.

## Limitations

The environment is finite horizon and the opportunity schedule is reduced form rather than a solved market equilibrium. Central comparative statics are regional. The project establishes no universal benefit of forgetting, optimal record half-life, global self-fulfilling-reputation theorem, or dominance of memory over direct sanctions. Numerical design results are appendix-only.
