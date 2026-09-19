def next_state(x: float, effort: float, rho: float, alpha: float) -> float:
    if effort < 0:
        raise ValueError("effort must be nonnegative")
    return rho * x + alpha * effort


def state_path(x0: float, initial_effort: float, rho: float, alpha: float, periods: int) -> list[float]:
    """One rehabilitation investment followed by natural state persistence."""
    values = [x0]
    if periods == 0:
        return values
    values.append(next_state(x0, initial_effort, rho, alpha))
    for _ in range(1, periods):
        values.append(rho * values[-1])
    return values

