"""Hostile identification and convergence audit for the M5 policy."""

from dataclasses import replace
import json
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"src"))
from economics_of_forgetting.m4 import PlannerParameters  # noqa:E402
from economics_of_forgetting.m5 import AdaptivePolicy,evaluate_adaptive,optimize_adaptive  # noqa:E402


def profile(base,p,name,grid=np.linspace(0,.99,100)):
    rows=[]
    for value in grid:
        q=AdaptivePolicy(base.phi_clean,base.phi_adverse,base.phi_rehab,base.good_streak_required)
        q=replace(q,**{name:float(value)})
        x=evaluate_adaptive(q,p)
        rows.append({"value":float(value),"welfare":x["welfare"],"prediction_mse":x["prediction_mse"],
                     "misconduct":x["misconduct_events"],"repeat":x["repeat_misconduct"]})
    return rows


def main():
    p=PlannerParameters(effort_grid_size=401)
    fit=optimize_adaptive(p,family="lifecycle")
    base=fit["optimum"]["parameters"]
    profiles={name:profile(base,p,name) for name in ("phi_clean","phi_adverse","phi_rehab")}
    streak=[]
    for m in range(1,7):
        x=evaluate_adaptive(replace(base,good_streak_required=m),p)
        streak.append({"m":m,"welfare":x["welfare"],"misconduct":x["misconduct_events"],"repeat":x["repeat_misconduct"]})
    slices=[]
    for clean in np.linspace(0,.99,12):
        for nonclean in np.linspace(0,.99,12):
            x=evaluate_adaptive(AdaptivePolicy(float(clean),float(nonclean),float(nonclean),1),p)
            slices.append({"phi_clean":float(clean),"phi_nonclean":float(nonclean),"welfare":x["welfare"]})
    horizons=[]
    for horizon in (3,4,6,8,12,20):
        q=replace(p,horizon=horizon,effort_grid_size=201)
        audit_grid=(0.0,.45,.85,.99) if horizon <= 8 else (0.0,.85,.99)
        fixed=optimize_adaptive(q,family="constant",phi_grid=audit_grid,streaks=(1,),fixed_phi_grid=audit_grid)
        life=optimize_adaptive(q,family="lifecycle",phi_grid=audit_grid,streaks=(1,),fixed_phi_grid=audit_grid)
        pol=life["optimum"]["parameters"]
        horizons.append({"horizon":horizon,"fixed_policy":fixed["optimum"]["parameters"].__dict__,
                         "adaptive_policy":pol.__dict__,"value":life["value_over_fixed"],
                         "misconduct":life["optimum"]["misconduct_events"],
                         "repeat":life["optimum"]["repeat_misconduct"]})
    convergence=[]
    for effort_grid in (101,201,501,1001):
        q=replace(p,effort_grid_size=effort_grid)
        audit_grid=(0.0,.45,.85,.99)
        life=optimize_adaptive(q,family="lifecycle",phi_grid=audit_grid,streaks=(1,),fixed_phi_grid=audit_grid)
        convergence.append({"effort_grid":effort_grid,"policy":life["optimum"]["parameters"].__dict__,
                            "welfare":life["optimum"]["welfare"],"value":life["value_over_fixed"]})
    repeat_cases=[]
    for horizon in (12,20):
        q=replace(p,horizon=horizon,misconduct_harm=.6,private_benefit_max=2.5,effort_grid_size=201)
        for policy in (AdaptivePolicy(0,0,0,1),AdaptivePolicy(0,.85,.85,1)):
            x=evaluate_adaptive(policy,q)
            repeat_cases.append({"horizon":horizon,"policy":policy.__dict__,"welfare":x["welfare"],
                                 "misconduct":x["misconduct_events"],"repeat":x["repeat_misconduct"]})
    fixed=fit["fixed_optimum"]["welfare"]; adaptive=fit["optimum"]["welfare"]; gain=adaptive-fixed
    all_w=[row["welfare"] for row in fit["candidates"]]
    normalization={"fixed_welfare":fixed,"adaptive_welfare":adaptive,"absolute_gain":gain,
                   "gain_per_agent_period":gain/p.horizon,"feasible_welfare_range":max(all_w)-min(all_w),
                   "gain_share_of_range":gain/(max(all_w)-min(all_w)),
                   "mse_absolute_gain":fit["fixed_optimum"]["prediction_mse"]-fit["optimum"]["prediction_mse"],
                   "mse_percent_gain":100*(fit["fixed_optimum"]["prediction_mse"]-fit["optimum"]["prediction_mse"])/fit["fixed_optimum"]["prediction_mse"]}
    result={"timing":{"clean_phi_updates_clean score only; misconduct resets score":"phi_clean does not set punishment",
                      "adverse_phi":"governs score persistence, effort return, and misconduct penalty proxy",
                      "rehab_phi":"applies after streak while still adverse"},
            "optimum":base.__dict__,"profiles":profiles,"streak_profile":streak,"two_state_slice":slices,
            "horizon_robustness":horizons,"action_grid_convergence":convergence,
            "repeat_misconduct_cases":repeat_cases,"normalization":normalization}
    out=ROOT/"experiments"/"m5_adaptive_memory"/"m5_5_hostile_audit.json"
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"optimum":result["optimum"],"normalization":normalization,"horizons":horizons,"convergence":convergence,"repeat":repeat_cases},indent=2))


if __name__=="__main__":main()
