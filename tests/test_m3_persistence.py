import numpy as np

from economics_of_forgetting.dynamic import DynamicState
from economics_of_forgetting.m3 import (
    clipped_affine_policy,
    conditional_predictiveness,
    local_transition_jacobian,
    paired_policy_paths,
    propagation_components,
    propagation_gap,
)


def test_exact_multi_period_propagation_identity():
    effort_gaps = np.array([0.2, -0.1, 0.3, 0.0])
    recursive = propagation_gap(0.4, effort_gaps, rho=0.6, alpha=0.8)
    decomposed = propagation_components(0.4, effort_gaps, rho=0.6, alpha=0.8)
    assert np.allclose(recursive, decomposed["total"])


def test_zero_rho_can_have_repeated_institution_produced_quality_gaps():
    policy = clipped_affine_policy(0.5, reputation_slope=0.35)
    paths = paired_policy_paths(
        DynamicState(0.8, 0.4, True), DynamicState(0.2, 0.4, True),
        policy, None, periods=4, phi=0.8, rho=0.0, alpha=0.7,
    )
    assert paths.quality_gap[0] == 0.0
    assert np.all(np.abs(paths.quality_gap[1:]) > 1e-8)
    assert np.allclose(paths.quality_gap, propagation_gap(0.0, paths.effort_gap, 0.0, 0.7))


def test_alpha_zero_and_fixed_effort_placebos_kill_true_quality_channel():
    policy = clipped_affine_policy(0.5, reputation_slope=0.4)
    states = (DynamicState(0.9, 0.3, True), DynamicState(0.1, 0.3, True))
    alpha_zero = paired_policy_paths(*states, policy, None, 4, 0.8, 0.6, 0.0)
    fixed = clipped_affine_policy(0.4, reputation_slope=0.0)
    fixed_effort = paired_policy_paths(*states, fixed, None, 4, 0.8, 0.6, 0.9)
    assert np.allclose(alpha_zero.quality_gap, 0.0)
    assert np.allclose(fixed_effort.quality_gap, 0.0)
    assert np.any(np.abs(alpha_zero.reputation_gap) > 0.0)


def test_self_confirming_and_self_correcting_regions_both_exist():
    states = (DynamicState(0.8, 0.4, True), DynamicState(0.2, 0.4, True))
    confirming = paired_policy_paths(
        *states, clipped_affine_policy(0.5, 0.3), None, 1, 0.8, 0.0, 0.8
    )
    correcting = paired_policy_paths(
        *states, clipped_affine_policy(0.5, -0.3), None, 1, 0.8, 0.0, 0.8
    )
    assert confirming.quality_gap[1] > 0.0
    assert correcting.quality_gap[1] < 0.0


def test_local_jacobian_matches_finite_difference():
    phi, rho, alpha, e_r, e_x = 0.7, 0.4, 0.8, -0.2, 0.15
    jac = local_transition_jacobian(phi, rho, alpha, e_r, e_x)
    expected = np.array([
        [rho + alpha * e_x, alpha * e_r],
        [(1 - phi) * (rho + alpha * e_x), phi + (1 - phi) * alpha * e_r],
    ])
    assert np.allclose(jac, expected)


def test_conditional_predictiveness_appears_only_with_behavioral_channel():
    rng = np.random.default_rng(20260919)
    x = rng.normal(size=4000)
    randomized_record = rng.normal(size=4000)
    noise = rng.normal(scale=0.2, size=4000)
    full_future = 0.6 * x + 0.5 * randomized_record + noise
    placebo_future = 0.6 * x + noise
    full = conditional_predictiveness(x, randomized_record, full_future)
    placebo = conditional_predictiveness(x, randomized_record, placebo_future)
    assert full["partial_r2"] > 0.8
    assert abs(full["reputation_coefficient"] - 0.5) < 0.02
    assert placebo["partial_r2"] < 0.002


def test_frozen_quality_to_record_update_reveals_mechanical_memory_route():
    policy = clipped_affine_policy(0.5, reputation_slope=0.35)
    states = (DynamicState(0.8, 0.4, True), DynamicState(0.2, 0.4, True))
    persistent_record = paired_policy_paths(
        *states, policy, None, 4, 0.8, 0.0, 0.7, endogenous_signal_weight=0.0
    )
    no_carryover = paired_policy_paths(
        *states, policy, None, 4, 0.0, 0.0, 0.7, endogenous_signal_weight=0.0
    )
    assert np.all(np.abs(persistent_record.quality_gap[1:]) > 1e-8)
    assert no_carryover.quality_gap[1] != 0.0
    assert np.allclose(no_carryover.quality_gap[2:], 0.0)
