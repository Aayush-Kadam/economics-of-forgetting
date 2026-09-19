"""M5 precommitted lifecycle and earned-forgetting mechanisms."""

from dataclasses import dataclass
from itertools import product
from typing import Iterable

import numpy as np

from .m4 import (
    DEFAULT_POPULATION, PlannerParameters, PopulationState, access, effort_choice,
    half_life, misconduct_rate, optimize_memory,
)


@dataclass(frozen=True)
class AdaptivePolicy:
    phi_clean: float
    phi_adverse: float
    phi_rehab: float
    good_streak_required: int = 2

    def validate(self):
        if any(not 0 <= value < 1 for value in (self.phi_clean, self.phi_adverse, self.phi_rehab)):
            raise ValueError("memory parameters must lie in [0,1)")
        if self.good_streak_required < 1:
            raise ValueError("good streak must be positive")

    @classmethod
    def constant(cls, phi: float, streak: int = 2):
        return cls(phi, phi, phi, streak)


@dataclass(frozen=True)
class Node:
    quality: float
    reputation: float
    lifecycle: str
    streak: int
    offenses: int
    probability: float


def memory_for(policy: AdaptivePolicy, lifecycle: str, streak: int) -> float:
    if lifecycle == "clean":
        return policy.phi_clean
    if streak >= policy.good_streak_required:
        return policy.phi_rehab
    return policy.phi_adverse


def update_streak(streak: int, favorable: bool) -> int:
    return streak + 1 if favorable else 0


def evaluate_adaptive(
    policy: AdaptivePolicy,
    p: PlannerParameters = PlannerParameters(),
    population: Iterable[PopulationState] = DEFAULT_POPULATION,
    effort_independent: bool = False,
    allow_repeat_misconduct: bool = True,
) -> dict[str, float]:
    """Expected finite-horizon welfare under a publicly committed rule."""
    policy.validate()
    population = tuple(population)
    weight = sum(person.weight for person in population)
    nodes = [Node(person.quality, person.reputation, "adverse" if person.adverse else "clean", 0, 0,
                  person.weight / weight) for person in population]
    components = {"productive_surplus": 0.0, "misallocation_loss": 0.0,
                  "effort_cost": 0.0, "misconduct_harm": 0.0}
    effort_total = quality_total = prediction_loss = misconduct_total = repeat_total = 0.0
    for t in range(p.horizon):
        discount = p.beta**t
        next_nodes = []
        for node in nodes:
            prob = node.probability
            a = access(node.reputation, p)
            components["productive_surplus"] += prob * discount * p.output_value * a * node.quality
            components["misallocation_loss"] -= prob * discount * p.bad_match_cost * a * max(0.0, 1-node.quality)
            phi = memory_for(policy, node.lifecycle, node.streak)
            if node.lifecycle == "adverse":
                e = 0.0 if effort_independent or p.alpha <= 0 else effort_choice(phi, node.reputation, node.quality, max(1, p.horizon-t), p)
            else:
                e = 0.0
            components["effort_cost"] -= prob * discount * .5 * p.kappa * e**2
            effort_total += prob * discount * e
            x_next = float(np.clip(p.rho*node.quality + p.alpha*e, 0, 1))
            prediction_loss += prob * discount * (node.reputation-x_next)**2
            quality_total += prob * discount * x_next
            r_next = phi*node.reputation + (1-phi)*x_next
            if (node.lifecycle == "clean" and p.misconduct_harm > 0
                    and (allow_repeat_misconduct or node.offenses == 0)):
                rate = misconduct_rate(policy.phi_adverse, p)
                misconduct_total += prob * rate
                repeat_total += prob * rate * float(node.offenses > 0)
                components["misconduct_harm"] -= prob * discount * p.misconduct_harm * rate
                if rate > 0:
                    next_nodes.append(Node(x_next, p.bad_record, "adverse", 0, node.offenses+1, prob*rate))
                if rate < 1:
                    next_nodes.append(Node(x_next, r_next, "clean", 0, node.offenses, prob*(1-rate)))
            else:
                favorable = x_next >= p.threshold
                streak = update_streak(node.streak, favorable)
                # Credible streak plus score recovery returns the agent to clean status.
                lifecycle = "clean" if streak >= policy.good_streak_required and r_next >= p.threshold else node.lifecycle
                next_nodes.append(Node(x_next, r_next, lifecycle, 0 if lifecycle == "clean" else streak,
                                       node.offenses, prob))
        nodes = next_nodes
    welfare = sum(components.values())
    norm = sum(p.beta**t for t in range(p.horizon))
    return {"welfare": welfare, **components, "discounted_effort": effort_total,
            "discounted_quality": quality_total, "prediction_mse": prediction_loss/norm,
            "misconduct_events": misconduct_total, "repeat_misconduct": repeat_total,
            "parameters": policy}


def optimize_adaptive(
    p: PlannerParameters = PlannerParameters(),
    population=DEFAULT_POPULATION,
    phi_grid=(0.0, .45, .8, .85, .99),
    streaks=(1, 2, 3),
    family: str = "lifecycle",
    fixed_phi_grid=None,
) -> dict:
    candidates = []
    if family == "lifecycle":
        iterator = product(phi_grid, phi_grid, phi_grid, streaks)
    elif family == "earned":
        iterator = ((high, high, low, m) for high, low, m in product(phi_grid, phi_grid, streaks) if low <= high)
    elif family == "constant":
        iterator = ((phi, phi, phi, m) for phi, m in product(phi_grid, streaks))
    else:
        raise ValueError("unknown policy family")
    for clean, adverse, rehab, streak in iterator:
        policy = AdaptivePolicy(float(clean), float(adverse), float(rehab), int(streak))
        result = evaluate_adaptive(policy, p, population)
        candidates.append(result)
    optimum = max(candidates, key=lambda row: row["welfare"])
    fixed_candidates = []
    fixed_grid = np.linspace(0.0, .99, 100) if fixed_phi_grid is None else fixed_phi_grid
    for phi, streak in product(fixed_grid, streaks):
        fixed_candidates.append(evaluate_adaptive(AdaptivePolicy.constant(float(phi), int(streak)), p, population))
    fixed = max(fixed_candidates, key=lambda row: row["welfare"])
    return {"optimum": optimum, "candidates": candidates, "fixed_optimum": fixed,
            "value_over_fixed": optimum["welfare"]-fixed["welfare"]}


def strict_contingency_gain(state_values: list[dict[float, float]]) -> float:
    """Finite-state theorem object: separate maxima minus best common action."""
    actions = set.intersection(*(set(values) for values in state_values))
    adaptive = sum(max(values.values()) for values in state_values)
    constant = max(sum(values[action] for values in state_values) for action in actions)
    return adaptive - constant
