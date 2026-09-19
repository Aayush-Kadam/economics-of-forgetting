import math
import numpy as np

from economics_of_forgetting.reputation import (
    continuous_recovery_time, recovery_time, recovery_time_derivative, reputation_path,
)


def test_closed_form_matches_recursion():
    path = reputation_path(0.8, -0.5, 1.0, 8)
    recursive = [-0.5]
    for _ in range(8):
        recursive.append(0.8 * recursive[-1] + 0.2)
    assert np.allclose(path, recursive)


def test_integer_recovery_time_crosses_first():
    n = recovery_time(0.8, -0.5, 0.5, 1.0)
    path = reputation_path(0.8, -0.5, 1.0, n)
    assert path[n] >= 0.5 and path[n - 1] < 0.5


def test_recovery_time_derivative_positive():
    assert recovery_time_derivative(0.8, -0.5, 0.5, 1.0) > 0


def test_recovery_boundaries():
    assert recovery_time(0.0, -0.5, 0.5, 1.0) == 1
    assert math.isinf(recovery_time(1.0, -0.5, 0.5, 1.0))
    assert continuous_recovery_time(0.0, -0.5, 0.5, 1.0) == 0

