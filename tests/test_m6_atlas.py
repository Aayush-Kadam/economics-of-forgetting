import math

from economics_of_forgetting.m4 import PlannerParameters
from economics_of_forgetting.m6 import classify_fixed,classify_value,efficiency_ratio,memory_conflict_index,policy_classes
from economics_of_forgetting.parameter_registry import validate_registry


def test_parameter_registry_integrity(): assert validate_registry()
def test_regime_classification_boundaries():
    assert classify_fixed(0)=="MINIMAL" and classify_fixed(.99)=="NEAR_PERMANENT"
    assert classify_value(0,1)=="NEGLIGIBLE" and classify_value(.02,1)=="MODERATE"
def test_policy_classes_are_nested():
    c=policy_classes((0,.5)); assert len(c["P0_constant"])==2 and len(c["P1_two_state"])==4
    constants={(p.phi_clean,p.phi_adverse,p.phi_rehab) for p in c["P0_constant"]}
    richer={(p.phi_clean,p.phi_adverse,p.phi_rehab) for p in c["P2_three_state"]}
    assert constants <= richer
def test_memory_conflict_is_deterministic_nonnegative():
    p=PlannerParameters(effort_grid_size=101); assert memory_conflict_index(p)==memory_conflict_index(p)>=0
def test_policy_efficiency_ratio():
    assert efficiency_ratio(2,1,3)==.5 and math.isfinite(efficiency_ratio(1,1,1))
