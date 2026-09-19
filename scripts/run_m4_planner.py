"""Generate the M4 planner audit, tables, and scientifically useful figures."""

import csv
from dataclasses import replace
import json
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from economics_of_forgetting.m4 import (  # noqa: E402
    DEFAULT_POPULATION, PlannerParameters, benchmark_suite, evaluate_welfare,
    half_life, optimize_memory,
)

OUT = ROOT / "experiments" / "m4_planner"
FIG = ROOT / "outputs" / "figures"
TAB = ROOT / "outputs" / "tables"


def compact(result):
    row = result["optimum"]
    return {k: row[k] for k in row if k != "rows"} | {"local_maxima_count": len(result["local_maxima"])}


def classify(phi):
    if phi <= 0.05:
        return "SHORT"
    if phi < 0.75:
        return "INTERMEDIATE"
    if phi < 0.97:
        return "LONG"
    return "NEAR_PERMANENT"


def write_csv(path, rows):
    rows = list(rows)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    FIG.mkdir(parents=True, exist_ok=True)
    TAB.mkdir(parents=True, exist_ok=True)
    p = PlannerParameters(effort_grid_size=401)
    suite = benchmark_suite(p)
    benchmark_rows = []
    for name in ("full", "fixed_behavior", "no_rehabilitation", "no_deterrence"):
        row = compact(suite[name])
        benchmark_rows.append({"world": name, "regime": classify(row["phi"]), **row})
    pred = suite["prediction_optimum"]
    benchmark_rows.append({"world": "prediction_minimizer", "regime": classify(pred["phi"]), **pred, "local_maxima_count": ""})
    write_csv(TAB / "m4_benchmark_optima.csv", benchmark_rows)

    sensitivity_specs = {
        "alpha": [0.2, 0.4, 0.55, 0.75, 0.95],
        "rho": [0.0, 0.25, 0.55, 0.75, 0.9],
        "kappa": [0.5, 0.8, 1.2, 1.8, 3.0],
        "beta": [0.75, 0.85, 0.95, 0.98],
        "misconduct_harm": [0.0, 0.5, 1.2, 2.0, 4.0],
        "horizon": [2, 4, 6, 8, 10],
    }
    sensitivity = []
    grid = np.linspace(0.0, 0.99, 51)
    for parameter, values in sensitivity_specs.items():
        for value in values:
            q = replace(p, **{parameter: value}, effort_grid_size=201)
            result = optimize_memory(q, behavior="full", grid=grid)
            row = result["optimum"]
            sensitivity.append({
                "parameter": parameter, "value": value, "phi_star": row["phi"],
                "half_life_star": row["half_life"], "welfare": row["welfare"],
                "regime": classify(row["phi"]), "local_maxima_count": len(result["local_maxima"]),
            })
    write_csv(TAB / "m4_comparative_statics.csv", sensitivity)

    phase = []
    alphas = [0.2, 0.4, 0.6, 0.8, 1.0]
    rhos = [0.0, 0.225, 0.45, 0.675, 0.9]
    matrix = np.zeros((len(rhos), len(alphas)))
    for i, rho in enumerate(rhos):
        for j, alpha in enumerate(alphas):
            q = replace(p, rho=rho, alpha=alpha, effort_grid_size=151)
            row = optimize_memory(q, grid=np.linspace(0, .99, 41))["optimum"]
            matrix[i, j] = row["phi"]
            phase.append({"rho": rho, "alpha": alpha, "phi_star": row["phi"], "half_life_star": row["half_life"], "regime": classify(row["phi"])})
    write_csv(TAB / "m4_rho_alpha_phase_map.csv", phase)

    full_rows = suite["full"]["rows"]
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot([r["half_life"] for r in full_rows], [r["welfare"] for r in full_rows], label="Full welfare")
    ax.set(xlabel="Reputation half-life (periods)", ylabel="Discounted welfare", title="M4 welfare and fixed-memory duration")
    ax.set_xlim(0, min(30, max(r["half_life"] for r in full_rows if np.isfinite(r["half_life"]))))
    ax.grid(alpha=.25)
    fig.tight_layout(); fig.savefig(FIG / "m4_welfare_half_life.png", dpi=180); plt.close(fig)

    fig, ax = plt.subplots(figsize=(7, 4.5))
    for key, label in (("productive_surplus", "Productive surplus"), ("misallocation_loss", "Screening loss"), ("effort_cost", "Effort cost"), ("misconduct_harm", "Misconduct harm")):
        ax.plot([r["phi"] for r in full_rows], [r[key] for r in full_rows], label=label)
    ax.set(xlabel="Record persistence phi", ylabel="Discounted welfare component", title="M4 welfare decomposition")
    ax.legend(fontsize=8); ax.grid(alpha=.25); fig.tight_layout(); fig.savefig(FIG / "m4_welfare_components.png", dpi=180); plt.close(fig)

    fig, ax = plt.subplots(figsize=(6.5, 4.5))
    labels = ["Welfare", "Prediction", "Fixed behavior"]
    vals = [suite["full"]["optimum"]["phi"], pred["phi"], suite["fixed_behavior"]["optimum"]["phi"]]
    ax.bar(labels, vals, color=["#35618f", "#c5683c", "#6a8f55"])
    ax.set(ylabel="Chosen phi", title="Objective functions choose different memory")
    fig.tight_layout(); fig.savefig(FIG / "m4_designer_comparison.png", dpi=180); plt.close(fig)

    fig, ax = plt.subplots(figsize=(6.5, 4.8))
    im = ax.imshow(matrix, origin="lower", aspect="auto", vmin=0, vmax=.99, cmap="viridis")
    ax.set_xticks(range(len(alphas)), alphas); ax.set_yticks(range(len(rhos)), rhos)
    ax.set(xlabel="Rehabilitation productivity alpha", ylabel="Intrinsic persistence rho", title="Welfare-optimal record persistence")
    fig.colorbar(im, ax=ax, label="phi star"); fig.tight_layout(); fig.savefig(FIG / "m4_rho_alpha_phase_map.png", dpi=180); plt.close(fig)

    phi_star = suite["full"]["optimum"]["phi"]
    incidence = []
    for idx, person in enumerate(DEFAULT_POPULATION):
        solo = replace(person, weight=1.0)
        row = evaluate_welfare(phi_star, p, [solo], "full")
        incidence.append({"group": idx, "quality": person.quality, "reputation": person.reputation, "adverse": person.adverse, "welfare": row["welfare"]})
    write_csv(TAB / "m4_distributional_incidence.csv", incidence)

    summary = {
        "parameters": p.__dict__,
        "benchmarks": benchmark_rows,
        "comparative_statics": sensitivity,
        "phase_map": phase,
        "distributional_incidence": incidence,
    }
    (OUT / "planner_results.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"benchmarks": benchmark_rows, "comparative_statics": sensitivity}, indent=2))


if __name__ == "__main__":
    main()
