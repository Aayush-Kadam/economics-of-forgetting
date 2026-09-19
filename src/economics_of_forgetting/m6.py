"""M6 atlas metrics, regime classification, and policy-complexity helpers."""

import numpy as np

from .m4 import DEFAULT_POPULATION, evaluate_welfare
from .m5 import AdaptivePolicy, evaluate_adaptive


def classify_fixed(phi):
    if phi<=.05:return "MINIMAL"
    if phi<.35:return "SHORT"
    if phi<.75:return "INTERMEDIATE"
    if phi<.97:return "LONG"
    return "NEAR_PERMANENT"


def classify_value(value, welfare_range):
    scale=max(abs(welfare_range),1e-12); share=value/scale
    if value < -1e-8:return "NEGATIVE_NUMERICAL_FAILURE"
    if share < .001:return "NEGLIGIBLE"
    if share < .01:return "SMALL"
    if share < .05:return "MODERATE"
    return "LARGE"


def memory_conflict_index(p, step=.01):
    slopes=[];weights=[]
    for person in DEFAULT_POPULATION:
        lo=evaluate_welfare(0,p,[person])["welfare"]
        hi=evaluate_welfare(step,p,[person])["welfare"]
        slopes.append((hi-lo)/step);weights.append(person.weight)
    return float(np.sqrt(np.average((np.asarray(slopes)-np.average(slopes,weights=weights))**2,weights=weights)))


def efficiency_ratio(simple,fixed,ceiling,tol=1e-12):
    denominator=ceiling-fixed
    if denominator<=tol:return 1.0 if abs(simple-fixed)<=tol else float("nan")
    return (simple-fixed)/denominator


def best_from_policies(p, policies):
    rows=[evaluate_adaptive(policy,p) for policy in policies]
    return max(rows,key=lambda x:x["welfare"]),rows


def policy_classes(phi_grid=(0,.45,.85,.99)):
    p0=[AdaptivePolicy.constant(phi,1) for phi in phi_grid]
    p1=[AdaptivePolicy(c,n,n,1) for c in phi_grid for n in phi_grid]
    p2=[AdaptivePolicy(c,a,r,1) for c in phi_grid for a in phi_grid for r in phi_grid]
    p3=[AdaptivePolicy(c,a,r,m) for c in phi_grid for a in phi_grid for r in phi_grid for m in (1,2,3)]
    earned=[AdaptivePolicy(h,h,l,m) for h in phi_grid for l in phi_grid if l<=h for m in (1,2,3)]
    return {"P0_constant":p0,"P1_two_state":p1,"P2_three_state":p2,
            "P3_threshold":p3,"earned_diagnostic":earned}
