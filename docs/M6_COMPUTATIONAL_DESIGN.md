# M6 Computational Design

M6 uses 36 deterministic predeclared points: `rho in {0,.45,.9}`, `alpha in {.3,.55,.8}`, misconduct harm in `{.6,1.8}`, and horizon in `{6,12}`. Every point uses the same four-type population, logistic opportunity, 101-point effort grid, and memory grid `{0,.45,.85,.99}`.

Policy classes are nested: P0 constant; P1 clean/nonclean; P2 clean/adverse/rehab; P3 adds streak threshold. A restricted earned rule is retained separately and is not placed on the nesting ladder. Expectations are exact; no Monte Carlo seed or standard error applies. Results are checkpointed after every point.
