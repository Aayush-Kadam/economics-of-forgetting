from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from economics_of_forgetting.agent_problem import (  # noqa: E402
    linear_optimal_effort, misconduct_probability, optimal_effort_grid,
)
from economics_of_forgetting.reputation import continuous_recovery_time  # noqa: E402
from economics_of_forgetting.simulations import paired_history_simulation  # noqa: E402


OUT = ROOT / "outputs" / "figures"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / name, dpi=200)
    plt.close(fig)


phis = np.linspace(0.02, 0.98, 150)

fig, ax = plt.subplots(figsize=(5.5, 3.5))
ax.plot(phis, [continuous_recovery_time(p, -0.5, 0.5, 1.0) for p in phis])
ax.set(xlabel="Record persistence phi", ylabel="Continuous recovery time", title="Mechanical reputation recovery")
save(fig, "m1_recovery_time.png")

fig, ax = plt.subplots(figsize=(5.5, 3.5))
for r0 in (-1.0, -0.5, 0.2):
    efforts = [optimal_effort_grid(p, r0, 0.2, 0.8, 0.8, 0.95, 1.0, 2.0, 3) for p in phis]
    ax.plot(phis, efforts, label=f"R0={r0}")
ax.set(xlabel="Record persistence phi", ylabel="Optimal effort", title="Smooth-market rehabilitation effort")
ax.legend()
save(fig, "m1_effort_by_history.png")

fig, ax1 = plt.subplots(figsize=(5.8, 3.7))
misconduct = [misconduct_probability(p, 0.8, 2.0, -0.5, 0.5, 1.0, 0.95, 2.0) for p in phis]
rehab = [linear_optimal_effort(p, 0.8, 0.8, 0.95, 1.0, 2.0, 3) for p in phis]
ax1.plot(phis, misconduct, label="Misconduct probability", color="tab:red")
ax1.plot(phis, rehab, label="Rehabilitation effort", color="tab:blue")
ax1.set(xlabel="Record persistence phi", ylabel="Decision or effort", title="Lifecycle asymmetry")
ax1.legend()
save(fig, "m1_lifecycle_asymmetry.png")

result = paired_history_simulation(0.4, -1.0, 0.2, 0.8, 0.8, 0.8, 0.95, 1.0, 2.0, 3)
fig, ax = plt.subplots(figsize=(5.5, 3.5))
for label, style in (("good", "-"), ("bad", "--")):
    ax.plot(result[label]["state"], style, label=f"{label} history; e={result[label]['effort']:.2f}")
ax.set(xlabel="Period", ylabel="Underlying quality x", title="Identical fundamentals, different public histories")
ax.legend()
save(fig, "m1_state_paths.png")

print(f"created 4 figures in {OUT}")

