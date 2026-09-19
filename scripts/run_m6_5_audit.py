"""Hostile, higher-resolution checks of the M6 atlas."""

import csv
import json
import sys
import time
from dataclasses import replace
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from economics_of_forgetting.m4 import DEFAULT_POPULATION, PlannerParameters  # noqa: E402
from economics_of_forgetting.m5 import AdaptivePolicy, evaluate_adaptive  # noqa: E402

ATLAS = ROOT / "outputs" / "tables" / "m6_atlas.csv"
OUT = ROOT / "experiments" / "m6_5_audit"
TABLE = ROOT / "outputs" / "tables" / "m6_5_audit.csv"


def read_atlas():
    with ATLAS.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def evaluate_grid(p, values):
    fixed = []
    adaptive = []
    for clean in values:
        for adverse in values:
            result = evaluate_adaptive(AdaptivePolicy(clean, adverse, adverse, 1), p)
            adaptive.append(result)
            if clean == adverse:
                fixed.append(result)
    return max(fixed, key=lambda x: x["welfare"]), max(adaptive, key=lambda x: x["welfare"]), fixed


def local_values(*centers):
    values = {0.0, 0.99}
    for center in centers:
        for delta in np.linspace(-0.12, 0.12, 9):
            values.add(round(float(np.clip(center + delta, 0, 0.99)), 4))
    return sorted(values)


def main():
    started = time.time()
    OUT.mkdir(parents=True, exist_ok=True)
    atlas = read_atlas()
    audited = []
    for row in atlas:
        idx = int(row["index"])
        p = PlannerParameters(
            rho=float(row["rho"]), alpha=float(row["alpha"]),
            misconduct_harm=float(row["misconduct_harm"]), horizon=int(row["horizon"]),
            effort_grid_size=301,
        )
        original_gain = float(row["adaptive_value"])
        suspicious = row["adaptive_regime"] in {"LARGE", "NEGLIGIBLE"} or row["prediction_order"] == "SAME"
        values = local_values(float(row["fixed_phi"]), float(row["two_clean"]), float(row["two_nonclean"])) if suspicious else [float(row["fixed_phi"]), float(row["two_clean"]), float(row["two_nonclean"])]
        fixed, adaptive, fixed_rows = evaluate_grid(p, values)
        gain = adaptive["welfare"] - fixed["welfare"]
        prediction = min(fixed_rows, key=lambda x: x["prediction_mse"])
        ap = adaptive["parameters"]
        fp = fixed["parameters"]
        longer = None
        if float(row["repeat_misconduct"]) > 1e-10:
            p_long = replace(p, horizon=min(50, 2 * p.horizon))
            fixed_long = evaluate_adaptive(AdaptivePolicy.constant(fp.phi_clean, 1), p_long)
            adaptive_long = evaluate_adaptive(AdaptivePolicy(ap.phi_clean, ap.phi_adverse, ap.phi_adverse, 1), p_long)
            longer = adaptive_long["welfare"] - fixed_long["welfare"]
        welfare_range = max(x["welfare"] for x in fixed_rows) - min(x["welfare"] for x in fixed_rows)
        audited.append({
            "index": idx, "rho": p.rho, "alpha": p.alpha, "misconduct_harm": p.misconduct_harm,
            "horizon": p.horizon, "original_regime": row["adaptive_regime"],
            "original_gain": original_gain, "refined_fixed_phi": fp.phi_clean,
            "refined_clean_phi": ap.phi_clean, "refined_nonclean_phi": ap.phi_adverse,
            "refined_gain": gain, "gain_change": gain - original_gain,
            "normalized_gain_fixed_range": gain / max(welfare_range, 1e-12),
            "prediction_phi_refined": prediction["parameters"].phi_clean,
            "prediction_welfare_distance": prediction["parameters"].phi_clean - fp.phi_clean,
            "misconduct": adaptive["misconduct_events"], "repeat_misconduct": adaptive["repeat_misconduct"],
            "effort": adaptive["discounted_effort"], "quality": adaptive["discounted_quality"],
            "lower_bound_hit": ap.phi_clean == 0 or ap.phi_adverse == 0,
            "upper_bound_hit": ap.phi_clean == .99 or ap.phi_adverse == .99,
            "longer_horizon_fixed_policy_gain": longer,
            "nested_ok": adaptive["welfare"] + 1e-10 >= fixed["welfare"],
            "grid_points": len(values),
        })
    with TABLE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(audited[0]))
        writer.writeheader(); writer.writerows(audited)
    summary = {
        "model": "M6.5-v1", "deterministic": True, "seed": None,
        "effort_grid": 301, "runtime_seconds": time.time() - started,
        "points": len(audited),
        "positive_refined": sum(x["refined_gain"] > 1e-8 for x in audited),
        "large_checked": sum(x["original_regime"] == "LARGE" for x in audited),
        "negligible_checked": sum(x["original_regime"] == "NEGLIGIBLE" for x in audited),
        "large_still_positive": sum(x["original_regime"] == "LARGE" and x["refined_gain"] > 1e-8 for x in audited),
        "negligible_still_negligible": sum(x["original_regime"] == "NEGLIGIBLE" and abs(x["refined_gain"]) < 1e-8 for x in audited),
        "repeat_longer_gain_positive": sum(x["longer_horizon_fixed_policy_gain"] is not None and x["longer_horizon_fixed_policy_gain"] > 0 for x in audited),
        "all_nested": all(x["nested_ok"] for x in audited),
    }
    (OUT / "metadata.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
