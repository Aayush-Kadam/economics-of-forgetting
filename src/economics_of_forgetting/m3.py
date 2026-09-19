"""M3 tools for institution-produced outcome persistence.

The routines here keep the canonical M2 timing: opportunity is assigned from
the current score, effort is chosen, quality moves, a signal is realized, and
the public score updates.  A policy is deliberately passed in rather than
being called an equilibrium object.
"""

from dataclasses import dataclass
from typing import Callable, Iterable

import numpy as np

from .dynamic import DynamicState, transition


Policy = Callable[[int, DynamicState], float]


@dataclass(frozen=True)
class PairedPath:
    quality_a: np.ndarray
    quality_b: np.ndarray
    reputation_a: np.ndarray
    reputation_b: np.ndarray
    effort_a: np.ndarray
    effort_b: np.ndarray

    @property
    def quality_gap(self) -> np.ndarray:
        return self.quality_a - self.quality_b

    @property
    def reputation_gap(self) -> np.ndarray:
        return self.reputation_a - self.reputation_b

    @property
    def effort_gap(self) -> np.ndarray:
        return self.effort_a - self.effort_b


def simulate_policy(
    state: DynamicState,
    policy: Policy,
    periods: int,
    phi: float,
    rho: float,
    alpha: float,
    signal_shocks: Iterable[float] | None = None,
    endogenous_signal_weight: float = 1.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Simulate the canonical deterministic policy path with optional shocks."""
    if periods < 0:
        raise ValueError("periods must be nonnegative")
    shocks = np.zeros(periods) if signal_shocks is None else np.asarray(list(signal_shocks), dtype=float)
    if len(shocks) != periods:
        raise ValueError("one signal shock is required per transition")
    qualities = [state.quality]
    reputations = [state.reputation]
    efforts: list[float] = []
    current = state
    for t in range(periods):
        effort = float(policy(t, current))
        if not 0.0 <= effort <= 1.0:
            raise ValueError("policy effort must lie in [0, 1]")
        efforts.append(effort)
        nxt = transition(current, effort, phi, rho, alpha, float(shocks[t]))
        if endogenous_signal_weight != 1.0:
            signal = endogenous_signal_weight * nxt.quality + float(shocks[t])
            nxt = DynamicState(
                phi * current.reputation + (1.0 - phi) * signal,
                nxt.quality,
                nxt.adverse,
            )
        current = nxt
        qualities.append(current.quality)
        reputations.append(current.reputation)
    return np.asarray(qualities), np.asarray(reputations), np.asarray(efforts)


def paired_policy_paths(
    state_a: DynamicState,
    state_b: DynamicState,
    policy_a: Policy,
    policy_b: Policy | None,
    periods: int,
    phi: float,
    rho: float,
    alpha: float,
    signal_shocks: Iterable[float] | None = None,
    endogenous_signal_weight: float = 1.0,
) -> PairedPath:
    """Run two worlds under identical primitive shocks."""
    shocks = np.zeros(periods) if signal_shocks is None else np.asarray(list(signal_shocks), dtype=float)
    policy_b = policy_a if policy_b is None else policy_b
    qa, ra, ea = simulate_policy(
        state_a, policy_a, periods, phi, rho, alpha, shocks, endogenous_signal_weight
    )
    qb, rb, eb = simulate_policy(
        state_b, policy_b, periods, phi, rho, alpha, shocks, endogenous_signal_weight
    )
    return PairedPath(qa, qb, ra, rb, ea, eb)


def propagation_gap(delta_x0: float, effort_gaps: Iterable[float], rho: float, alpha: float) -> np.ndarray:
    """Exact state-equation decomposition of the quality gap at every horizon."""
    gaps = [float(delta_x0)]
    for delta_e in effort_gaps:
        gaps.append(rho * gaps[-1] + alpha * float(delta_e))
    return np.asarray(gaps)


def propagation_components(delta_x0: float, effort_gaps: Iterable[float], rho: float, alpha: float) -> dict:
    """Return intrinsic and behavioral terms in Delta x_h exactly."""
    effort_gaps = np.asarray(list(effort_gaps), dtype=float)
    horizons = np.arange(len(effort_gaps) + 1)
    intrinsic = np.power(rho, horizons) * delta_x0
    behavioral = np.zeros_like(intrinsic, dtype=float)
    for h in range(1, len(intrinsic)):
        weights = np.power(rho, np.arange(h - 1, -1, -1))
        behavioral[h] = alpha * float(weights @ effort_gaps[:h])
    return {"intrinsic": intrinsic, "behavioral": behavioral, "total": intrinsic + behavioral}


def clipped_affine_policy(
    intercept: float,
    reputation_slope: float,
    quality_slope: float = 0.0,
) -> Policy:
    """Transparent local policy used to test propagation and sign regions."""
    def policy(_: int, state: DynamicState) -> float:
        return float(np.clip(intercept + reputation_slope * state.reputation + quality_slope * state.quality, 0.0, 1.0))
    return policy


def local_transition_jacobian(
    phi: float,
    rho: float,
    alpha: float,
    effort_r: float,
    effort_x: float,
) -> np.ndarray:
    """Jacobian of (x', R') with respect to (x, R) under a differentiable policy."""
    # State ordering is (x, R). R'=phi R+(1-phi)x' under a zero signal shock.
    x_x = rho + alpha * effort_x
    x_r = alpha * effort_r
    return np.asarray([
        [x_x, x_r],
        [(1.0 - phi) * x_x, phi + (1.0 - phi) * x_r],
    ])


def conditional_predictiveness(
    current_quality: Iterable[float],
    current_reputation: Iterable[float],
    future_quality: Iterable[float],
) -> dict[str, float]:
    """Incremental linear predictive content of R after controlling for current x."""
    x = np.asarray(list(current_quality), dtype=float)
    r = np.asarray(list(current_reputation), dtype=float)
    y = np.asarray(list(future_quality), dtype=float)
    if not (len(x) == len(r) == len(y)) or len(x) < 4:
        raise ValueError("aligned samples of length at least four are required")
    restricted = np.column_stack([np.ones(len(x)), x])
    full = np.column_stack([np.ones(len(x)), x, r])
    fit0 = restricted @ np.linalg.lstsq(restricted, y, rcond=None)[0]
    fit1 = full @ np.linalg.lstsq(full, y, rcond=None)[0]
    sse0 = float(np.sum((y - fit0) ** 2))
    sse1 = float(np.sum((y - fit1) ** 2))
    partial_r2 = 0.0 if sse0 == 0.0 else max(0.0, (sse0 - sse1) / sse0)
    return {
        "restricted_mse": sse0 / len(x),
        "full_mse": sse1 / len(x),
        "mse_improvement": (sse0 - sse1) / len(x),
        "partial_r2": partial_r2,
        "reputation_coefficient": float(np.linalg.lstsq(full, y, rcond=None)[0][2]),
    }
