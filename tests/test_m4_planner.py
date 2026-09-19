import math

from economics_of_forgetting.m4 import (
    PlannerParameters, benchmark_suite, evaluate_welfare, half_life, misconduct_rate,
    optimize_memory,
)


def test_welfare_components_sum_exactly():
    row = evaluate_welfare(0.5)
    expected = sum(row[key] for key in (
        "productive_surplus", "misallocation_loss", "effort_cost", "misconduct_harm"
    ))
    assert math.isclose(row["welfare"], expected)


def test_half_life_boundaries_and_interior():
    assert half_life(0.0) == 0.0
    assert math.isclose(half_life(0.5), 1.0)
    assert math.isinf(half_life(1.0))


def test_global_planner_returns_admissible_verified_grid_point():
    result = optimize_memory(grid=[0.0, 0.25, 0.5, 0.75, 0.99])
    optimum = result["optimum"]
    assert 0.0 <= optimum["phi"] < 1.0
    assert optimum["welfare"] == max(row["welfare"] for row in result["rows"])


def test_core_benchmark_worlds_are_distinct_and_finite():
    suite = benchmark_suite(PlannerParameters(effort_grid_size=201))
    values = [suite[key]["optimum"]["welfare"] for key in (
        "full", "fixed_behavior", "no_rehabilitation", "no_deterrence"
    )]
    assert all(math.isfinite(value) for value in values)
    assert len({round(value, 6) for value in values}) >= 3


def test_linear_and_logistic_opportunity_are_supported():
    for mapping in ("linear", "logistic"):
        result = optimize_memory(PlannerParameters(opportunity=mapping, effort_grid_size=201), grid=[0, .3, .6, .9])
        assert math.isfinite(result["optimum"]["welfare"])


def test_discrete_deterrence_has_no_spurious_zero_boundary_jump():
    p = PlannerParameters()
    assert misconduct_rate(0.0, p) == misconduct_rate(1e-6, p)
