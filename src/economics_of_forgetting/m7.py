"""M7 numerical validation helpers."""

import numpy as np
from scipy.optimize import differential_evolution, minimize_scalar

from .agent_problem import optimal_effort_grid
from .m4 import PlannerParameters


def effort_utility(effort, phi, reputation, quality, remaining, p):
    x1 = p.rho * quality + p.alpha * effort
    r = x1 + phi**remaining * (reputation - x1)
    if p.opportunity == "hard":
        a = float(r >= p.threshold)
    elif p.opportunity == "linear":
        a = float(np.clip(.25 + .5 * r, 0, 1))
    else:
        a = float(1 / (1 + np.exp(-np.clip(p.logistic_slope * (r-p.threshold), -700, 700))))
    return p.beta**remaining * p.opportunity_value * a - .5 * p.kappa * effort**2


def continuous_effort(phi, reputation, quality, remaining, p=PlannerParameters()):
    """Bounded continuous effort search, with a global fallback for nonconcavity."""
    objective = lambda x: -effort_utility(float(x), phi, reputation, quality, remaining, p)
    local = minimize_scalar(objective, bounds=(0, 1), method="bounded", options={"xatol":1e-10})
    global_result = differential_evolution(lambda x: objective(x[0]), [(0, 1)], seed=0, tol=1e-10, polish=True)
    candidates = (0.0, 1.0, float(local.x), float(global_result.x[0]))
    return max(candidates, key=lambda x: -objective(x))


def effort_solver_check(p=PlannerParameters(effort_grid_size=501)):
    rows=[]
    for phi in (0,.5,.9,.99):
        for reputation,quality in ((.05,.35),(.25,.65),(.65,.2)):
            grid=optimal_effort_grid(phi,reputation,quality,p.rho,p.alpha,p.beta,p.kappa,
                                     p.opportunity_value,p.horizon,p.opportunity,p.threshold,
                                     p.logistic_slope,p.effort_grid_size)
            continuous=continuous_effort(phi,reputation,quality,p.horizon,p)
            rows.append({"phi":phi,"reputation":reputation,"quality":quality,"grid":grid,
                         "continuous":continuous,"absolute_difference":abs(grid-continuous)})
    return rows
