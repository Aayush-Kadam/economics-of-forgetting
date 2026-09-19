from economics_of_forgetting.agent_problem import (
    binary_rehabilitate, linear_optimal_effort, misconduct_probability, optimal_effort_grid,
)


def test_binary_rehabilitation_can_collapse_with_persistence():
    common = dict(r0=-0.5, threshold=0.5, good_signal=1.0, beta=0.9, access_value=2.0, cost=0.8)
    assert binary_rehabilitate(phi=0.3, **common)
    assert not binary_rehabilitate(phi=0.98, **common)


def test_linear_effort_decreases_with_phi():
    args = dict(rho=0.7, alpha=0.8, beta=0.95, kappa=1.0, value=2.0, horizon=3)
    assert linear_optimal_effort(phi=0.9, **args) < linear_optimal_effort(phi=0.4, **args)


def test_alpha_zero_eliminates_productive_effort():
    e = optimal_effort_grid(
        phi=0.8, r0=-0.5, x0=0.2, rho=0.7, alpha=0.0, beta=0.95,
        kappa=1.0, value=2.0, horizon=3, mapping="logistic",
    )
    assert e == 0.0


def test_reputation_independent_opportunity_eliminates_effort():
    e = optimal_effort_grid(
        phi=0.8, r0=-0.5, x0=0.2, rho=0.7, alpha=0.8, beta=0.95,
        kappa=1.0, value=2.0, horizon=3, mapping="constant",
    )
    assert e == 0.0


def test_perfect_quality_observation_removes_history_effect():
    args = dict(
        phi=0.8, x0=0.2, rho=0.7, alpha=0.8, beta=0.95, kappa=1.0,
        value=2.0, horizon=3, mapping="perfect_quality",
    )
    assert optimal_effort_grid(r0=-1.0, **args) == optimal_effort_grid(r0=0.4, **args)


def test_misconduct_probability_decreases_with_phi():
    args = dict(
        detection_probability=0.8, private_benefit_max=2.0, r_bad=-0.5,
        threshold=0.5, good_signal=1.0, beta=0.95, access_value=2.0,
    )
    assert misconduct_probability(0.9, **args) < misconduct_probability(0.4, **args)

