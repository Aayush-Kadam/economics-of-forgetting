import math
import numpy as np

from .market import hard_access, linear_access, logistic_access
from .reputation import continuous_recovery_time, horizon_reputation
from .states import next_state


def binary_rehabilitation_value(
    phi: float, r0: float, threshold: float, good_signal: float,
    beta: float, access_value: float, cost: float,
) -> float:
    n = continuous_recovery_time(phi, r0, threshold, good_signal)
    if math.isinf(n):
        return -cost
    return beta**n * access_value - cost


def binary_rehabilitate(**kwargs) -> bool:
    return binary_rehabilitation_value(**kwargs) >= 0


def linear_optimal_effort(
    phi: float, rho: float, alpha: float, beta: float, kappa: float,
    value: float, horizon: int, access_slope: float = 0.5,
) -> float:
    """Interior FOC, clipped to [0,1], for a linear opportunity mapping."""
    del rho  # rho shifts the payoff level but not its marginal return in this one-investment benchmark.
    marginal = beta**horizon * value * access_slope * alpha * (1 - phi**horizon)
    return float(np.clip(marginal / kappa, 0.0, 1.0))


def optimal_effort_grid(
    phi: float,
    r0: float,
    x0: float,
    rho: float,
    alpha: float,
    beta: float,
    kappa: float,
    value: float,
    horizon: int,
    mapping: str = "logistic",
    threshold: float = 0.5,
    logistic_slope: float = 6.0,
    grid_size: int = 20001,
) -> float:
    """Deterministic global solution on [0,1] for possibly nonconcave payoffs."""
    efforts = np.linspace(0.0, 1.0, grid_size)
    x1 = rho * x0 + alpha * efforts
    reputations = x1 + phi**horizon * (r0 - x1)
    if mapping == "hard":
        access = (reputations >= threshold).astype(float)
    elif mapping == "logistic":
        z = np.clip(logistic_slope * (reputations - threshold), -700, 700)
        access = 1.0 / (1.0 + np.exp(-z))
    elif mapping == "linear":
        access = np.clip(0.25 + 0.5 * reputations, 0.0, 1.0)
    elif mapping == "constant":
        access = np.full_like(efforts, 0.5)
    elif mapping == "perfect_quality":
        z = np.clip(logistic_slope * (x1 - threshold), -700, 700)
        access = 1.0 / (1.0 + np.exp(-z))
    else:
        raise ValueError(f"unknown mapping: {mapping}")
    utility = beta**horizon * value * access - 0.5 * kappa * efforts**2
    return float(efforts[int(np.argmax(utility))])


def misconduct_penalty(
    phi: float, r_bad: float, threshold: float, good_signal: float,
    beta: float, access_value: float,
) -> float:
    """PV loss from delayed rather than immediate access after detection."""
    n = continuous_recovery_time(phi, r_bad, threshold, good_signal)
    return access_value if math.isinf(n) else access_value * (1 - beta**n)


def misconduct_probability(
    phi: float, detection_probability: float, private_benefit_max: float,
    r_bad: float, threshold: float, good_signal: float, beta: float,
    access_value: float,
) -> float:
    """Probability of misconduct for a uniform private benefit on [0,b_max]."""
    penalty = detection_probability * misconduct_penalty(
        phi, r_bad, threshold, good_signal, beta, access_value
    )
    return float(np.clip(1 - penalty / private_benefit_max, 0.0, 1.0))


def logistic_derivatives(reputation: float, threshold: float, slope: float) -> tuple[float, float, float]:
    """Return A, A', A'' for a logistic opportunity map."""
    z = np.clip(slope * (reputation - threshold), -700, 700)
    a = float(1.0 / (1.0 + np.exp(-z)))
    first = slope * a * (1.0 - a)
    second = slope * first * (1.0 - 2.0 * a)
    return a, first, second


def logistic_effort_phi_sign_terms(
    phi: float, effort: float, r0: float, x0: float, rho: float, alpha: float,
    beta: float, kappa: float, value: float, horizon: int,
    threshold: float = 0.5, logistic_slope: float = 6.0,
) -> dict[str, float]:
    """IFT decomposition of de*/dphi at an interior strict local maximum."""
    m = phi**horizon
    mp = horizon * phi ** (horizon - 1)
    x1 = rho * x0 + alpha * effort
    rt = m * r0 + (1.0 - m) * x1
    _, ap, app = logistic_derivatives(rt, threshold, logistic_slope)
    q = alpha * (1.0 - m)
    attenuation = -alpha * mp * ap
    relocation = q * app * mp * (r0 - x1)
    numerator = beta**horizon * value * (attenuation + relocation)
    denominator = kappa - beta**horizon * value * q**2 * app
    derivative = numerator / denominator if denominator > 0 else float("nan")
    return {
        "reputation": rt,
        "A_prime": ap,
        "A_second": app,
        "attenuation": attenuation,
        "relocation": relocation,
        "soc_denominator": denominator,
        "de_dphi": derivative,
    }
