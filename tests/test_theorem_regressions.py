import math
import numpy as np

from economics_of_forgetting.agent_problem import (
    linear_optimal_effort, logistic_effort_phi_sign_terms, misconduct_probability,
    optimal_effort_grid,
)
from economics_of_forgetting.reputation import continuous_recovery_time, recovery_time_derivative
from economics_of_forgetting.states import next_state


SEED = 20260919
DRAWS = 1000


def test_t1_recovery_derivative_random_draws():
    rng = np.random.default_rng(SEED)
    for _ in range(DRAWS):
        r0 = rng.uniform(-2.0, 0.0)
        threshold = rng.uniform(0.05, 0.8)
        signal = rng.uniform(threshold + 0.05, 2.0)
        phi = rng.uniform(0.01, 0.99)
        assert recovery_time_derivative(phi, r0, threshold, signal) > 0


def test_t2_discounted_rehabilitation_return_falls_with_phi():
    rng = np.random.default_rng(SEED + 1)
    for _ in range(DRAWS):
        r0 = rng.uniform(-1.5, 0.0)
        threshold = rng.uniform(0.05, 0.7)
        signal = rng.uniform(threshold + 0.1, 1.8)
        beta = rng.uniform(0.7, 0.995)
        lo, hi = sorted(rng.uniform(0.01, 0.99, 2))
        assert beta ** continuous_recovery_time(hi, r0, threshold, signal) <= beta ** continuous_recovery_time(lo, r0, threshold, signal)


def test_t3_linear_effort_weakly_falls_random_draws():
    rng = np.random.default_rng(SEED + 2)
    for _ in range(DRAWS):
        args = dict(
            rho=rng.uniform(0, 1), alpha=rng.uniform(0.05, 2), beta=rng.uniform(0.7, 0.995),
            kappa=rng.uniform(0.1, 4), value=rng.uniform(0.1, 5), horizon=int(rng.integers(1, 8)),
            access_slope=rng.uniform(0.05, 1),
        )
        lo, hi = sorted(rng.uniform(0.01, 0.99, 2))
        assert linear_optimal_effort(hi, **args) <= linear_optimal_effort(lo, **args) + 1e-12


def test_t4_clean_misconduct_weakly_falls_random_draws():
    rng = np.random.default_rng(SEED + 3)
    for _ in range(DRAWS):
        threshold = rng.uniform(0.1, 0.8)
        args = dict(
            detection_probability=rng.uniform(0.05, 1), private_benefit_max=rng.uniform(0.2, 5),
            r_bad=rng.uniform(-2, threshold - 0.05), threshold=threshold,
            good_signal=rng.uniform(threshold + 0.05, 2), beta=rng.uniform(0.7, 0.995),
            access_value=rng.uniform(0.1, 5),
        )
        lo, hi = sorted(rng.uniform(0.01, 0.99, 2))
        assert misconduct_probability(hi, **args) <= misconduct_probability(lo, **args) + 1e-12


def test_logistic_ift_matches_finite_difference_at_regular_interior_points():
    rng = np.random.default_rng(SEED + 4)
    checked = 0
    for _ in range(3000):
        phi = rng.uniform(0.15, 0.85)
        args = dict(
            r0=rng.uniform(-1.0, 1.0), x0=rng.uniform(-0.2, 0.6), rho=rng.uniform(0, 0.9),
            alpha=rng.uniform(0.2, 1.2), beta=rng.uniform(0.8, 0.99), kappa=rng.uniform(0.5, 2.5),
            value=rng.uniform(0.5, 3), horizon=3, threshold=0.5,
            logistic_slope=rng.uniform(2, 8), mapping="logistic", grid_size=20001,
        )
        e = optimal_effort_grid(phi=phi, **args)
        terms = logistic_effort_phi_sign_terms(phi=phi, effort=e, **{k: v for k, v in args.items() if k not in ("mapping", "grid_size")})
        if not (0.05 < e < 0.95 and terms["soc_denominator"] > 0.2 and abs(terms["de_dphi"]) > 0.02):
            continue
        h = 1e-3
        e_lo = optimal_effort_grid(phi=phi - h, **args)
        e_hi = optimal_effort_grid(phi=phi + h, **args)
        numerical = (e_hi - e_lo) / (2 * h)
        assert math.copysign(1, numerical) == math.copysign(1, terms["de_dphi"])
        checked += 1
        if checked >= 30:
            break
    assert checked >= 20


def test_rho_zero_allows_next_state_history_gap():
    common = dict(phi=0.8, x0=0.2, rho=0.0, alpha=0.8, beta=0.95, kappa=1.0,
                  value=2.0, horizon=3, mapping="logistic")
    e_a = optimal_effort_grid(r0=0.4, **common)
    e_b = optimal_effort_grid(r0=-1.0, **common)
    assert next_state(0.2, e_a, 0.0, 0.8) != next_state(0.2, e_b, 0.0, 0.8)

