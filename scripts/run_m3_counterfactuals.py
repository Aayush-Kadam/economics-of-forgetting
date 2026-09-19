"""Reproduce the core M3 matched-world and predictive checks."""

import json
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from economics_of_forgetting.dynamic import DynamicState
from economics_of_forgetting.m3 import (
    clipped_affine_policy,
    conditional_predictiveness,
    local_transition_jacobian,
    paired_policy_paths,
    propagation_components,
)


OUT = ROOT / "experiments" / "m3_endogenous_persistence"


def serial_path(paths):
    return {
        "quality_gap": paths.quality_gap.tolist(),
        "reputation_gap": paths.reputation_gap.tolist(),
        "effort_gap": paths.effort_gap.tolist(),
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    states = (DynamicState(0.8, 0.4, True), DynamicState(0.2, 0.4, True))
    full_policy = clipped_affine_policy(0.5, 0.35)
    fixed_policy = clipped_affine_policy(0.5, 0.0)
    full = paired_policy_paths(*states, full_policy, None, 6, 0.8, 0.0, 0.7)
    no_productive = paired_policy_paths(*states, full_policy, None, 6, 0.8, 0.0, 0.0)
    fixed = paired_policy_paths(*states, fixed_policy, None, 6, 0.8, 0.0, 0.7)
    minimal_memory = paired_policy_paths(*states, full_policy, None, 6, 0.0, 0.0, 0.7)
    correcting = paired_policy_paths(
        *states, clipped_affine_policy(0.5, -0.35), None, 6, 0.8, 0.0, 0.7
    )
    decomp = propagation_components(0.0, full.effort_gap, 0.0, 0.7)

    rng = np.random.default_rng(20260919)
    x = rng.normal(size=10000)
    random_record = rng.normal(size=10000)
    shock = rng.normal(scale=0.25, size=10000)
    full_predictive = conditional_predictiveness(x, random_record, 0.6 * x + 0.5 * random_record + shock)
    information_only = conditional_predictiveness(x, random_record, 0.6 * x + shock)

    result = {
        "parameters": {"phi": 0.8, "rho": 0.0, "alpha": 0.7, "periods": 6},
        "full_zero_rho": serial_path(full),
        "information_only_fixed_effort": serial_path(fixed),
        "no_productive_effect_alpha_zero": serial_path(no_productive),
        "minimal_memory_phi_zero": serial_path(minimal_memory),
        "self_correcting": serial_path(correcting),
        "propagation_decomposition": {k: v.tolist() for k, v in decomp.items()},
        "local_jacobian_full": local_transition_jacobian(0.8, 0.0, 0.7, 0.35, 0.0).tolist(),
        "predictiveness_random_record_full": full_predictive,
        "predictiveness_random_record_information_only": information_only,
    }
    (OUT / "counterfactual_results.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
