from dataclasses import replace

from economics_of_forgetting.m4 import PlannerParameters, access, misconduct_rate
from economics_of_forgetting.m7 import continuous_effort, effort_utility


def test_hard_opportunity_is_supported():
    p = PlannerParameters(opportunity="hard", threshold=.5)
    assert access(.49, p) == 0
    assert access(.5, p) == 1


def test_direct_penalty_weakly_reduces_misconduct():
    p = PlannerParameters()
    assert misconduct_rate(.5, replace(p, direct_penalty=1)) <= misconduct_rate(.5, p)


def test_continuous_effort_beats_endpoints():
    p = PlannerParameters()
    effort = continuous_effort(.8, .2, .4, 6, p)
    value = effort_utility(effort, .8, .2, .4, 6, p)
    assert value >= max(effort_utility(0, .8, .2, .4, 6, p), effort_utility(1, .8, .2, .4, 6, p)) - 1e-8
