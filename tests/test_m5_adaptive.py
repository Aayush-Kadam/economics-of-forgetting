import math

from economics_of_forgetting.m4 import PlannerParameters
from economics_of_forgetting.m5 import (
    AdaptivePolicy, evaluate_adaptive, memory_for, optimize_adaptive,
    strict_contingency_gain, update_streak,
)


def test_constant_policy_is_nested_exactly():
    policy = AdaptivePolicy.constant(.45)
    assert memory_for(policy, "clean", 0) == .45
    assert memory_for(policy, "adverse", 0) == .45
    assert memory_for(policy, "adverse", 3) == .45


def test_earned_rule_transition_and_streak_reset():
    policy = AdaptivePolicy(.8, .8, .1, 2)
    assert memory_for(policy, "adverse", 1) == .8
    assert memory_for(policy, "adverse", 2) == .1
    assert update_streak(1, True) == 2
    assert update_streak(2, False) == 0


def test_adaptive_evaluation_is_deterministic():
    policy = AdaptivePolicy(.45, .8, 0, 2)
    assert evaluate_adaptive(policy)["welfare"] == evaluate_adaptive(policy)["welfare"]


def test_optimizer_contains_constant_family_and_is_consistent():
    p = PlannerParameters(effort_grid_size=101)
    constant = optimize_adaptive(p, phi_grid=(0, .45), streaks=(1,2), family="constant")
    adaptive = optimize_adaptive(p, phi_grid=(0, .45), streaks=(1,2), family="lifecycle")
    assert adaptive["optimum"]["welfare"] >= constant["optimum"]["welfare"]


def test_alpha_zero_and_effort_independent_placebos_remove_effort():
    policy = AdaptivePolicy(.45, .8, 0, 2)
    assert evaluate_adaptive(policy, PlannerParameters(alpha=0))["discounted_effort"] == 0
    assert evaluate_adaptive(policy, effort_independent=True)["discounted_effort"] == 0


def test_no_misconduct_placebo_removes_misconduct_and_repeat_events():
    result = evaluate_adaptive(AdaptivePolicy(.45, .8, 0, 1), PlannerParameters(misconduct_harm=0))
    assert result["misconduct_events"] == 0
    assert result["repeat_misconduct"] == 0


def test_repeat_misconduct_dynamics_are_finite_and_nonnegative():
    result = evaluate_adaptive(AdaptivePolicy(0, 0, 0, 1))
    assert math.isfinite(result["welfare"])
    assert result["repeat_misconduct"] >= 0


def test_strict_state_contingency_theorem_object():
    gain = strict_contingency_gain([{0: 2, 1: 0}, {0: 0, 1: 2}])
    assert gain == 2
    assert strict_contingency_gain([{0: 2, 1: 1}, {0: 2, 1: 1}]) == 0
