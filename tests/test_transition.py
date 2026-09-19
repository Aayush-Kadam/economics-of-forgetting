from economics_of_forgetting.states import next_state, state_path


def test_state_transition_separates_rho_and_alpha():
    assert next_state(0.4, 0.5, rho=0.25, alpha=0.8) == 0.5


def test_alpha_zero_placebo():
    assert next_state(0.4, 1.0, rho=0.5, alpha=0.0) == 0.2


def test_state_path_is_deterministic():
    assert state_path(0.2, 0.5, 0.8, 0.6, 4) == state_path(0.2, 0.5, 0.8, 0.6, 4)

