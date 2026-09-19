"""M4 finite-horizon planner for a constant public-record persistence rule."""

from dataclasses import dataclass, replace
import math
from typing import Iterable

import numpy as np

from .agent_problem import optimal_effort_grid
from .market import hard_access, linear_access, logistic_access
from .reputation import recovery_time


@dataclass(frozen=True)
class PopulationState:
    quality: float
    reputation: float
    adverse: bool
    weight: float


@dataclass(frozen=True)
class PlannerParameters:
    horizon: int = 6
    beta: float = 0.95
    rho: float = 0.55
    alpha: float = 0.55
    kappa: float = 1.2
    opportunity_value: float = 2.0
    output_value: float = 1.6
    bad_match_cost: float = 0.8
    misconduct_harm: float = 1.2
    detection_probability: float = 0.65
    private_benefit_max: float = 1.5
    bad_record: float = 0.05
    threshold: float = 0.5
    good_signal: float = 0.85
    logistic_slope: float = 6.0
    opportunity: str = "logistic"
    effort_grid_size: int = 501
    direct_penalty: float = 0.0


DEFAULT_POPULATION = (
    PopulationState(0.80, 0.78, False, 0.25),
    PopulationState(0.65, 0.25, True, 0.25),   # false/adverse record
    PopulationState(0.35, 0.38, True, 0.25),
    PopulationState(0.20, 0.65, False, 0.25),  # favorable but noisy record
)


def half_life(phi: float) -> float:
    if phi <= 0.0:
        return 0.0
    if phi >= 1.0:
        return math.inf
    return math.log(0.5) / math.log(phi)


def access(reputation: float, p: PlannerParameters) -> float:
    if p.opportunity == "logistic":
        return logistic_access(reputation, p.threshold, p.logistic_slope)
    if p.opportunity == "linear":
        return linear_access(reputation)
    if p.opportunity == "hard":
        return hard_access(reputation, p.threshold)
    raise ValueError("opportunity must be logistic, linear, or hard")


def misconduct_rate(phi: float, p: PlannerParameters) -> float:
    if p.misconduct_harm == 0.0:
        return 0.0
    if phi >= 1.0 or p.good_signal <= p.threshold:
        delay = math.inf
    else:
        # The canonical model updates in discrete periods.  Using the continuous
        # relaxation for phi>0 but an integer delay at phi=0 creates a spurious
        # discontinuity exactly at the planner boundary.
        delay = float(recovery_time(phi, p.bad_record, p.threshold, p.good_signal))
    penalty = p.opportunity_value if math.isinf(delay) else p.opportunity_value * (1.0 - p.beta**delay)
    threshold = p.detection_probability * (penalty + p.direct_penalty)
    return float(np.clip(1.0 - threshold / p.private_benefit_max, 0.0, 1.0))


def effort_choice(phi: float, reputation: float, quality: float, remaining: int, p: PlannerParameters) -> float:
    if p.alpha <= 0.0 or remaining <= 0:
        return 0.0
    return optimal_effort_grid(
        phi=phi, r0=reputation, x0=quality, rho=p.rho, alpha=p.alpha,
        beta=p.beta, kappa=p.kappa, value=p.opportunity_value,
        horizon=remaining, mapping=p.opportunity, threshold=p.threshold,
        logistic_slope=p.logistic_slope, grid_size=p.effort_grid_size,
    )


def _fixed_effort_schedules(population, p: PlannerParameters, reference_phi: float = 0.5):
    schedules = {}
    for i, person in enumerate(population):
        r, x = person.reputation, person.quality
        values = []
        for t in range(p.horizon):
            e = effort_choice(reference_phi, r, x, max(1, p.horizon - t), p) if person.adverse else 0.0
            values.append(e)
            x = float(np.clip(p.rho * x + p.alpha * e, 0.0, 1.0))
            r = reference_phi * r + (1.0 - reference_phi) * x
        schedules[i] = values
    return schedules


def evaluate_welfare(
    phi: float,
    p: PlannerParameters = PlannerParameters(),
    population: Iterable[PopulationState] = DEFAULT_POPULATION,
    behavior: str = "full",
    reference_phi: float = 0.5,
) -> dict[str, float]:
    """Evaluate discounted real welfare; transfers are excluded."""
    if not 0.0 <= phi < 1.0:
        raise ValueError("planner domain is 0 <= phi < 1")
    population = tuple(population)
    total_weight = sum(person.weight for person in population)
    if total_weight <= 0:
        raise ValueError("population weights must sum to a positive number")
    fixed = _fixed_effort_schedules(population, p, reference_phi) if behavior in {"fixed", "no_feedback"} else None
    components = {"productive_surplus": 0.0, "misallocation_loss": 0.0, "effort_cost": 0.0}
    prediction_loss = 0.0
    adverse_effort = 0.0
    for i, person in enumerate(population):
        r, x = person.reputation, person.quality
        w = person.weight / total_weight
        for t in range(p.horizon):
            discount = p.beta**t
            a = access(r, p)
            components["productive_surplus"] += w * discount * p.output_value * a * x
            components["misallocation_loss"] -= w * discount * p.bad_match_cost * a * max(0.0, 1.0 - x)
            if person.adverse:
                if behavior == "full":
                    e = effort_choice(phi, r, x, max(1, p.horizon - t), p)
                elif behavior in {"fixed", "no_feedback"}:
                    e = fixed[i][t]
                elif behavior == "no_rehab":
                    e = 0.0
                else:
                    raise ValueError("unknown behavior mode")
            else:
                e = 0.0
            components["effort_cost"] -= w * discount * 0.5 * p.kappa * e**2
            adverse_effort += w * discount * e
            x_next = float(np.clip(p.rho * x + p.alpha * e, 0.0, 1.0))
            prediction_loss += w * discount * (r - x_next) ** 2
            r = phi * r + (1.0 - phi) * x_next
            x = x_next
    clean_weight = sum(person.weight for person in population if not person.adverse) / total_weight
    rate = misconduct_rate(phi, p)
    misconduct_harm = -clean_weight * p.misconduct_harm * rate
    components["misconduct_harm"] = misconduct_harm
    welfare = sum(components.values())
    return {
        "phi": phi,
        "half_life": half_life(phi),
        "welfare": welfare,
        **components,
        "misconduct_rate": rate,
        "discounted_adverse_effort": adverse_effort,
        "prediction_mse": prediction_loss / sum(p.beta**t for t in range(p.horizon)),
    }


def optimize_memory(
    p: PlannerParameters = PlannerParameters(),
    population: Iterable[PopulationState] = DEFAULT_POPULATION,
    behavior: str = "full",
    grid: Iterable[float] | None = None,
) -> dict:
    """Global grid search with local refinement; no concavity assumption."""
    coarse = np.asarray(list(grid) if grid is not None else np.linspace(0.0, 0.99, 100), dtype=float)
    rows = [evaluate_welfare(float(phi), p, population, behavior) for phi in coarse]
    best = max(rows, key=lambda row: row["welfare"])
    spacing = float(np.min(np.diff(np.unique(coarse)))) if len(coarse) > 1 else 0.01
    lo, hi = max(0.0, best["phi"] - spacing), min(0.999, best["phi"] + spacing)
    fine = np.linspace(lo, hi, 81)
    fine_rows = [evaluate_welfare(float(phi), p, population, behavior) for phi in fine]
    all_rows = {round(row["phi"], 12): row for row in rows + fine_rows}
    ordered = [all_rows[key] for key in sorted(all_rows)]
    optimum = max(ordered, key=lambda row: row["welfare"])
    local_maxima = [row for j, row in enumerate(ordered[1:-1], 1)
                    if row["welfare"] >= ordered[j-1]["welfare"] and row["welfare"] >= ordered[j+1]["welfare"]]
    return {"optimum": optimum, "rows": ordered, "local_maxima": local_maxima}


def benchmark_suite(p: PlannerParameters = PlannerParameters(), population=DEFAULT_POPULATION) -> dict:
    full = optimize_memory(p, population, "full")
    fixed = optimize_memory(p, population, "fixed")
    no_rehab = optimize_memory(replace(p, alpha=0.0), population, "no_rehab")
    no_deterrence = optimize_memory(replace(p, misconduct_harm=0.0), population, "full")
    prediction_row = min(full["rows"], key=lambda row: row["prediction_mse"])
    return {
        "full": full,
        "fixed_behavior": fixed,
        "no_rehabilitation": no_rehab,
        "no_deterrence": no_deterrence,
        "prediction_optimum": prediction_row,
    }
