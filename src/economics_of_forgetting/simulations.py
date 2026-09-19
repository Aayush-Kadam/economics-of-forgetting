from .agent_problem import optimal_effort_grid
from .states import state_path


def paired_history_simulation(
    good_reputation: float,
    bad_reputation: float,
    x0: float,
    phi: float,
    rho: float,
    alpha: float,
    beta: float,
    kappa: float,
    value: float,
    horizon: int,
    periods: int = 8,
) -> dict:
    common = dict(
        x0=x0, phi=phi, rho=rho, alpha=alpha, beta=beta, kappa=kappa,
        value=value, horizon=horizon, mapping="logistic",
    )
    e_good = optimal_effort_grid(r0=good_reputation, **common)
    e_bad = optimal_effort_grid(r0=bad_reputation, **common)
    return {
        "good": {"effort": e_good, "state": state_path(x0, e_good, rho, alpha, periods)},
        "bad": {"effort": e_bad, "state": state_path(x0, e_bad, rho, alpha, periods)},
    }

