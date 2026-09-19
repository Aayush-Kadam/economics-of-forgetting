"""Hostile robustness checks for the completed M3 mechanism."""

import json
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from economics_of_forgetting.agent_problem import optimal_effort_grid  # noqa: E402
from economics_of_forgetting.dynamic import DynamicState  # noqa: E402
from economics_of_forgetting.m3 import paired_policy_paths  # noqa: E402


OUT = ROOT / "experiments" / "m3_endogenous_persistence" / "hostile_audit.json"


def rolling_logistic_policy(decision_horizon: int):
    def policy(_t, state):
        return optimal_effort_grid(
            phi=0.8, r0=state.reputation, x0=state.quality, rho=0.0,
            alpha=0.7, beta=0.95, kappa=1.0, value=2.0,
            horizon=decision_horizon, mapping="logistic", grid_size=4001,
        )
    return policy


def path_summary(periods: int, decision_horizon: int, signal_weight: float = 1.0, phi: float = 0.8):
    states = (DynamicState(0.8, 0.4, True), DynamicState(0.2, 0.4, True))
    policy = rolling_logistic_policy(decision_horizon)
    paths = paired_policy_paths(
        *states, policy, None, periods, phi, 0.0, 0.7,
        endogenous_signal_weight=signal_weight,
    )
    return {
        "quality_gap": paths.quality_gap.tolist(),
        "effort_gap": paths.effort_gap.tolist(),
        "effort_a": paths.effort_a.tolist(),
        "effort_b": paths.effort_b.tolist(),
        "mean_absolute_quality_gap": float(np.mean(np.abs(paths.quality_gap[1:]))),
    }


def local_record_slopes():
    results = {}
    eps = 1e-3
    for r in np.linspace(-0.2, 1.2, 29):
        kwargs = dict(
            phi=0.8, x0=0.4, rho=0.0, alpha=0.7, beta=0.95,
            kappa=1.0, value=2.0, horizon=3, mapping="logistic", grid_size=10001,
        )
        lo = optimal_effort_grid(r0=float(r - eps), **kwargs)
        hi = optimal_effort_grid(r0=float(r + eps), **kwargs)
        slope = (hi - lo) / (2 * eps)
        if 1e-6 < lo < 1 - 1e-6 and 1e-6 < hi < 1 - 1e-6:
            label = "self_confirming" if slope > 1e-6 else "self_correcting" if slope < -1e-6 else "flat"
            results.setdefault(label, []).append({"reputation": float(r), "e_R": float(slope)})
    return results


def main():
    horizons = {str(h): path_summary(h, min(3, h)) for h in (2, 4, 6, 8, 12)}
    result = {
        "smooth_logistic_horizon_robustness": horizons,
        "frozen_quality_update_phi_08": path_summary(6, 3, signal_weight=0.0, phi=0.8),
        "frozen_quality_update_phi_0": path_summary(6, 3, signal_weight=0.0, phi=0.0),
        "smooth_logistic_sign_regions": local_record_slopes(),
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
