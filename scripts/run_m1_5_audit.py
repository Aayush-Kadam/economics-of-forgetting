from pathlib import Path
import csv
import sys

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from economics_of_forgetting.agent_problem import (  # noqa: E402
    logistic_effort_phi_sign_terms, optimal_effort_grid,
)
from economics_of_forgetting.reputation import horizon_reputation  # noqa: E402

OUT = ROOT / "outputs" / "figures"
DATA = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)
DATA.mkdir(parents=True, exist_ok=True)

phis = np.linspace(0.05, 0.95, 91)
records = np.linspace(-1.5, 1.5, 121)
signs = np.full((len(records), len(phis)), np.nan)
rows = []

common = dict(x0=0.2, rho=0.7, alpha=0.8, beta=0.95, kappa=1.0, value=2.0, horizon=3)
for i, r0 in enumerate(records):
    for j, phi in enumerate(phis):
        e = optimal_effort_grid(phi=phi, r0=r0, mapping="logistic", **common)
        terms = logistic_effort_phi_sign_terms(phi=phi, effort=e, r0=r0, **common)
        derivative = terms["de_dphi"]
        if 1e-3 < e < 1 - 1e-3 and np.isfinite(derivative):
            signs[i, j] = np.sign(derivative)
        rows.append({"r0": r0, "phi": phi, "effort": e, **terms})

with (DATA / "m1_5_logistic_sign_map.csv").open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

fig, ax = plt.subplots(figsize=(6.2, 4.0))
im = ax.imshow(
    signs, origin="lower", aspect="auto", extent=[phis.min(), phis.max(), records.min(), records.max()],
    cmap="coolwarm", vmin=-1, vmax=1,
)
ax.set(xlabel="Record persistence phi", ylabel="Initial reputation R0",
       title="Sign of local logistic effort response to memory")
cbar = fig.colorbar(im, ax=ax, ticks=[-1, 0, 1])
cbar.ax.set_yticklabels(["de/dphi < 0", "boundary/flat", "de/dphi > 0"])
fig.tight_layout()
fig.savefig(OUT / "m1_5_logistic_sign_map.png", dpi=200)
plt.close(fig)

# Mechanical versus behavioral path under a one-time rehabilitation choice.
periods = np.arange(0, 9)
r0 = -0.7
signal_if_fixed = 0.7
fig, ax = plt.subplots(figsize=(6.2, 4.0))
for phi, color in ((0.45, "tab:green"), (0.85, "tab:purple")):
    e = optimal_effort_grid(phi=phi, r0=r0, mapping="logistic", **common)
    x1 = common["rho"] * common["x0"] + common["alpha"] * e
    fixed = [horizon_reputation(phi, r0, signal_if_fixed, int(t)) for t in periods]
    endogenous = [horizon_reputation(phi, r0, x1, int(t)) for t in periods]
    ax.plot(periods, fixed, color=color, linestyle="--", label=f"phi={phi}: fixed effort/signal")
    ax.plot(periods, endogenous, color=color, label=f"phi={phi}: endogenous effort e={e:.2f}")
ax.set(xlabel="Periods after adverse record", ylabel="Public reputation",
       title="Mechanical score persistence versus behavioral response")
ax.legend(fontsize=8)
fig.tight_layout()
fig.savefig(OUT / "m1_5_mechanical_behavioral_decomposition.png", dpi=200)
plt.close(fig)

print(f"wrote {len(rows)} sign-map rows and 2 figures")
