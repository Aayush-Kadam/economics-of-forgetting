from pathlib import Path
import json
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from economics_of_forgetting.agent_problem import (  # noqa: E402
    logistic_effort_phi_sign_terms, optimal_effort_grid,
)

OUT = ROOT / "experiments" / "m2_theorems" / "counterexamples"
OUT.mkdir(parents=True, exist_ok=True)
rng = np.random.default_rng(20260919)
examples = {"positive_memory_effect": [], "bad_record_higher_effort": [], "boundary_flat": []}

for _ in range(25000):
    phi = rng.uniform(0.05, 0.95)
    r0 = rng.uniform(-1.5, 1.5)
    x0 = rng.uniform(-0.3, 0.8)
    rho = rng.uniform(0.0, 0.95)
    alpha = rng.uniform(0.1, 1.5)
    beta = rng.uniform(0.7, 0.995)
    kappa = rng.uniform(0.2, 3.0)
    value = rng.uniform(0.5, 4.0)
    slope = rng.uniform(1.0, 12.0)
    args = dict(x0=x0, rho=rho, alpha=alpha, beta=beta, kappa=kappa, value=value,
                horizon=3, threshold=0.5, logistic_slope=slope)
    e = optimal_effort_grid(phi=phi, r0=r0, mapping="logistic", grid_size=4001, **args)
    terms = logistic_effort_phi_sign_terms(phi=phi, effort=e, r0=r0, **args)
    record = {"phi": phi, "r0": r0, "effort": e, **args, **terms}
    if 0.01 < e < 0.99 and np.isfinite(terms["de_dphi"]) and terms["de_dphi"] > 1e-4:
        if len(examples["positive_memory_effect"]) < 10:
            examples["positive_memory_effect"].append(record)
    if e in (0.0, 1.0) and len(examples["boundary_flat"]) < 10:
        examples["boundary_flat"].append(record)
    e_better = optimal_effort_grid(phi=phi, r0=r0 + 0.25, mapping="logistic", grid_size=4001, **args)
    if e > e_better + 0.02 and len(examples["bad_record_higher_effort"]) < 10:
        examples["bad_record_higher_effort"].append({**record, "better_record_effort": e_better})

with (OUT / "logistic_counterexamples.json").open("w", encoding="utf-8") as f:
    json.dump(examples, f, indent=2)
print({k: len(v) for k, v in examples.items()})

