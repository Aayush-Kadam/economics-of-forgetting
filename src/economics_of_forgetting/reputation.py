import math
import numpy as np


def reputation_path(phi: float, r0: float, signal: float, periods: int) -> np.ndarray:
    """Closed-form path R_t = y + phi^t (R_0-y), including t=0."""
    if not 0 <= phi <= 1:
        raise ValueError("phi must lie in [0, 1]")
    if periods < 0:
        raise ValueError("periods must be nonnegative")
    t = np.arange(periods + 1, dtype=float)
    return signal + np.power(phi, t) * (r0 - signal)


def continuous_recovery_time(phi: float, r0: float, threshold: float, signal: float) -> float:
    """Continuous relaxation of threshold-crossing time under a constant signal."""
    if r0 >= threshold:
        return 0.0
    if signal <= threshold:
        return math.inf
    if phi == 0:
        return 0.0
    if phi == 1:
        return math.inf
    if not 0 < phi < 1:
        raise ValueError("phi must lie in [0, 1]")
    q = (signal - threshold) / (signal - r0)
    return math.log(q) / math.log(phi)


def recovery_time(phi: float, r0: float, threshold: float, signal: float) -> float:
    """First integer t >= 0 for which R_t >= threshold."""
    if r0 >= threshold:
        return 0
    if signal <= threshold or phi == 1:
        return math.inf
    if phi == 0:
        return 1
    return int(math.ceil(continuous_recovery_time(phi, r0, threshold, signal)))


def recovery_time_derivative(phi: float, r0: float, threshold: float, signal: float) -> float:
    """Derivative of the continuous crossing time with respect to phi."""
    if not 0 < phi < 1 or not r0 < threshold < signal:
        raise ValueError("requires 0<phi<1 and r0<threshold<signal")
    q = (signal - threshold) / (signal - r0)
    return -math.log(q) / (phi * math.log(phi) ** 2)


def horizon_reputation(phi: float, r0: float, signal: float, horizon: int) -> float:
    return signal + phi**horizon * (r0 - signal)

