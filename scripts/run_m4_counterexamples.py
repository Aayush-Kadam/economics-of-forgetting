"""Seeded global search for M4 reversals and nontrivial designer differences."""

from dataclasses import asdict
import json
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from economics_of_forgetting.m4 import PlannerParameters, optimize_memory  # noqa: E402


def main():
    rng = np.random.default_rng(20260919)
    grid = np.linspace(0.0, 0.99, 25)
    findings = {
        "prediction_longer_than_welfare": [], "prediction_shorter_than_welfare": [],
        "behavior_aware_shorter_than_naive": [], "behavior_aware_longer_than_naive": [],
        "interior_welfare_optimum": [], "multiple_local_maxima": [],
    }
    for _ in range(100):
        p = PlannerParameters(
            horizon=int(rng.choice([2, 4, 6, 8])), beta=float(rng.uniform(.75, .99)),
            rho=float(rng.uniform(0, .95)), alpha=float(rng.uniform(.15, 1.0)),
            kappa=float(rng.uniform(.4, 3.5)), output_value=float(rng.uniform(.8, 2.5)),
            bad_match_cost=float(rng.uniform(.2, 1.8)), misconduct_harm=float(rng.uniform(0, 4)),
            opportunity=str(rng.choice(["linear", "logistic"])), effort_grid_size=101,
        )
        full = optimize_memory(p, behavior="full", grid=grid)
        naive = optimize_memory(p, behavior="fixed", grid=grid)
        wf = full["optimum"]["phi"]
        nf = naive["optimum"]["phi"]
        pred = min(full["rows"], key=lambda row: row["prediction_mse"])["phi"]
        record = {"parameters": asdict(p), "welfare_phi": wf, "prediction_phi": pred, "naive_phi": nf,
                  "welfare": full["optimum"]["welfare"]}
        tests = {
            "prediction_longer_than_welfare": pred > wf + .1,
            "prediction_shorter_than_welfare": pred < wf - .1,
            "behavior_aware_shorter_than_naive": wf < nf - .1,
            "behavior_aware_longer_than_naive": wf > nf + .1,
            "interior_welfare_optimum": .05 < wf < .95,
            "multiple_local_maxima": len(full["local_maxima"]) > 1,
        }
        for key, passed in tests.items():
            if passed and len(findings[key]) < 5:
                findings[key].append(record | {"local_maxima_count": len(full["local_maxima"])})
    out = ROOT / "experiments" / "m4_planner" / "counterexamples.json"
    out.write_text(json.dumps(findings, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: len(value) for key, value in findings.items()}, indent=2))


if __name__ == "__main__":
    main()
