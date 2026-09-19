from dataclasses import dataclass
from typing import Callable
import numpy as np

from .market import logistic_access


@dataclass(frozen=True)
class DynamicState:
    reputation: float
    quality: float
    adverse: bool


def transition(
    state: DynamicState,
    effort: float,
    phi: float,
    rho: float,
    alpha: float,
    signal_shock: float = 0.0,
) -> DynamicState:
    """Score-based transition; reputation is a mechanical score, not a belief."""
    x_next = rho * state.quality + alpha * effort
    signal = x_next + signal_shock
    r_next = phi * state.reputation + (1.0 - phi) * signal
    return DynamicState(r_next, x_next, state.adverse)


def adverse_bellman_step(
    state: DynamicState,
    continuation: Callable[[DynamicState], float],
    phi: float,
    rho: float,
    alpha: float,
    beta: float,
    kappa: float,
    opportunity_value: float,
    threshold: float = 0.5,
    logistic_slope: float = 6.0,
    grid_size: int = 2001,
) -> tuple[float, float]:
    """One Bellman operator for an adverse-state agent on an effort grid."""
    efforts = np.linspace(0.0, 1.0, grid_size)
    values = np.empty_like(efforts)
    for i, effort in enumerate(efforts):
        nxt = transition(state, float(effort), phi, rho, alpha)
        flow = opportunity_value * logistic_access(state.reputation, threshold, logistic_slope)
        values[i] = flow - 0.5 * kappa * effort**2 + beta * continuation(nxt)
    idx = int(np.argmax(values))
    return float(values[idx]), float(efforts[idx])


def clean_misconduct_threshold(
    clean_continuation: float,
    adverse_continuation: float,
    detection_probability: float,
) -> float:
    """Private benefit above which misconduct is optimal."""
    return detection_probability * max(0.0, clean_continuation - adverse_continuation)

