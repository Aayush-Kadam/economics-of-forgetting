"""Hostile audit of the M4 boundary, regimes, peaks, and state margins."""

from dataclasses import asdict, replace
import json
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from economics_of_forgetting.m4 import (  # noqa: E402
    DEFAULT_POPULATION, PlannerParameters, PopulationState, evaluate_welfare,
    optimize_memory,
)


def slopes_near_zero(p):
    rows = [evaluate_welfare(phi, p) for phi in (0.0, .001, .005, .01)]
    keys = ("welfare", "productive_surplus", "misallocation_loss", "effort_cost", "misconduct_harm")
    return {key: (rows[-1][key] - rows[0][key]) / .01 for key in keys} | {"rows": rows}


def state_margins(p):
    states = {
        "clean_high_safe": PopulationState(.85, .85, False, 1),
        "clean_low_false_positive": PopulationState(.25, .75, False, 1),
        "recent_adverse_high_quality": PopulationState(.75, .10, True, 1),
        "recent_adverse_low_quality": PopulationState(.25, .10, True, 1),
        "intermediate_recovery": PopulationState(.55, .45, True, 1),
        "credible_rehabilitation": PopulationState(.80, .55, True, 1),
        "very_low_reputation": PopulationState(.45, -.10, True, 1),
        "old_adverse_near_threshold": PopulationState(.65, .48, True, 1),
    }
    result = []
    for name, state in states.items():
        opt = optimize_memory(p, [state], grid=np.linspace(0, .99, 61))["optimum"]
        w0 = evaluate_welfare(0, p, [state])["welfare"]
        w1 = evaluate_welfare(.01, p, [state])["welfare"]
        result.append({"state": name, "quality": state.quality, "reputation": state.reputation,
                       "adverse": state.adverse, "local_slope_at_zero": (w1-w0)/.01,
                       "phi_star": opt["phi"], "half_life_star": opt["half_life"],
                       "welfare_star": opt["welfare"]})
    return result


def peak_audit():
    base = PlannerParameters(
        horizon=8, beta=.8450002737935648, rho=.10634435959378695,
        alpha=.8317251486848815, kappa=1.7156470768058867,
        output_value=2.388810631514426, bad_match_cost=.2564411675340818,
        misconduct_harm=1.7518568709732256, opportunity="linear",
    )
    audits = []
    for effort_grid in (101, 401, 1001):
        for scale in (.98, 1.0, 1.02):
            p = replace(base, kappa=base.kappa*scale, effort_grid_size=effort_grid)
            phis = np.linspace(0, .999, 801)
            rows = [evaluate_welfare(float(phi), p) for phi in phis]
            values = np.array([r["welfare"] for r in rows])
            # Material peaks exceed both neighbors and have at least 1e-4 prominence
            peaks = []
            for i in range(2, len(values)-2):
                prominence = values[i] - max(min(values[i-2:i]), min(values[i+1:i+3]))
                if values[i] > values[i-1] and values[i] >= values[i+1] and prominence > 1e-4:
                    peaks.append({"phi": float(phis[i]), "welfare": float(values[i]), "prominence": float(prominence)})
            best = rows[int(np.argmax(values))]
            audits.append({"effort_grid": effort_grid, "kappa_scale": scale,
                           "global_phi": best["phi"], "global_welfare": best["welfare"],
                           "material_peak_count": len(peaks), "material_peaks": peaks[:10]})
    return {"parameters": asdict(base), "audits": audits}


def regime_examples(p):
    specs = {
        "short_baseline": p,
        "intermediate_high_cost": replace(p, kappa=3.0),
        "long_zero_rho": replace(p, rho=0.0),
        "near_permanent_short_horizon": replace(p, horizon=2),
    }
    rows = []
    for name, q in specs.items():
        result = optimize_memory(q, grid=np.linspace(0, .99, 101))
        opt = result["optimum"]
        pred = min(result["rows"], key=lambda x: x["prediction_mse"])
        fixed = optimize_memory(q, behavior="fixed", grid=np.linspace(0, .99, 101))["optimum"]
        rows.append({"regime": name, "parameters": asdict(q), "phi_star": opt["phi"],
                     "half_life_star": opt["half_life"], "prediction_phi": pred["phi"],
                     "fixed_behavior_phi": fixed["phi"], "local_maxima": len(result["local_maxima"])})
    return rows


def main():
    p = PlannerParameters(effort_grid_size=401)
    result = {"boundary_decomposition": slopes_near_zero(p),
              "regime_transition_table": regime_examples(p),
              "state_specific_margins": state_margins(p),
              "multiple_local_maxima_audit": peak_audit()}
    out = ROOT / "experiments" / "m4_planner" / "m4_5_hostile_audit.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
