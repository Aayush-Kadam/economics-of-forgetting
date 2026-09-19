from economics_of_forgetting.simulations import paired_history_simulation


def test_smooth_opportunity_can_generate_history_dependent_state_paths():
    result = paired_history_simulation(
        good_reputation=0.4, bad_reputation=-1.0, x0=0.2, phi=0.8,
        rho=0.8, alpha=0.8, beta=0.95, kappa=1.0, value=2.0, horizon=3,
    )
    assert result["good"]["effort"] != result["bad"]["effort"]
    assert result["good"]["state"][1] != result["bad"]["state"][1]


def test_rho_zero_does_not_remove_first_period_behavioral_gap():
    result = paired_history_simulation(
        good_reputation=0.4, bad_reputation=-1.0, x0=0.2, phi=0.8,
        rho=0.0, alpha=0.8, beta=0.95, kappa=1.0, value=2.0, horizon=3,
    )
    assert result["good"]["state"][1] != result["bad"]["state"][1]

