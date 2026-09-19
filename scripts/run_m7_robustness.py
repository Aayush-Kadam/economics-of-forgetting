"""Pre-registered, bounded M7 robustness battery."""

import csv
import json
import sys
import time
from dataclasses import replace
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from economics_of_forgetting.m4 import DEFAULT_POPULATION, PlannerParameters, PopulationState  # noqa:E402
from economics_of_forgetting.m5 import AdaptivePolicy, evaluate_adaptive  # noqa:E402
from economics_of_forgetting.m7 import effort_solver_check  # noqa:E402

GRID = (0.0, .25, .5, .75, .9, .99)
OUT = ROOT / "experiments" / "m7_robustness"
TABLE = ROOT / "outputs" / "tables" / "m7_robustness.csv"


def optimize(p, population=DEFAULT_POPULATION, allow_repeat=True):
    fixed = []
    two = []
    for clean in GRID:
        for adverse in GRID:
            result = evaluate_adaptive(AdaptivePolicy(clean, adverse, adverse, 1), p, population,
                                       allow_repeat_misconduct=allow_repeat)
            two.append(result)
            if clean == adverse:
                fixed.append(result)
    f = max(fixed, key=lambda x: x["welfare"])
    a = max(two, key=lambda x: x["welfare"])
    return f, a


def populations():
    def pop(qualities, reputations, adverse, weights):
        return tuple(PopulationState(*x) for x in zip(qualities, reputations, adverse, weights))
    return {
        "baseline": DEFAULT_POPULATION,
        "high_quality": pop((.9,.8,.75,.7),(.8,.3,.45,.7),(0,1,1,0),(.25,)*4),
        "low_quality": pop((.4,.3,.2,.1),(.7,.2,.35,.6),(0,1,1,0),(.25,)*4),
        "high_adverse": pop((.8,.65,.35,.2),(.78,.25,.38,.65),(0,1,1,1),(.1,.3,.3,.3)),
        "low_adverse": pop((.8,.65,.35,.2),(.78,.25,.38,.65),(0,0,1,0),(.3,.2,.1,.4)),
        "bimodal": pop((.95,.85,.15,.05),(.9,.2,.8,.1),(0,1,0,1),(.25,)*4),
    }


def add_case(rows, family, spec, p, population=DEFAULT_POPULATION, allow_repeat=True):
    fixed, adaptive = optimize(p, population, allow_repeat)
    fp, ap = fixed["parameters"], adaptive["parameters"]
    rows.append({
        "family": family, "specification": spec, "horizon": p.horizon,
        "fixed_phi": fp.phi_clean, "clean_phi": ap.phi_clean, "nonclean_phi": ap.phi_adverse,
        "fixed_welfare": fixed["welfare"], "adaptive_welfare": adaptive["welfare"],
        "gain": adaptive["welfare"] - fixed["welfare"],
        "fixed_misconduct": fixed["misconduct_events"], "adaptive_misconduct": adaptive["misconduct_events"],
        "adaptive_repeat": adaptive["repeat_misconduct"], "adaptive_effort": adaptive["discounted_effort"],
        "adaptive_quality": adaptive["discounted_quality"], "prediction_mse": adaptive["prediction_mse"],
        "nested_ok": adaptive["welfare"] + 1e-10 >= fixed["welfare"],
        "allow_repeat": allow_repeat,
    })


def main():
    started = time.time(); rows = []
    base = PlannerParameters(effort_grid_size=101)
    for opportunity, slope in (("logistic",3),("logistic",6),("logistic",10),("linear",6),("hard",6)):
        add_case(rows,"opportunity",f"{opportunity}_slope_{slope}",replace(base,opportunity=opportunity,logistic_slope=slope))
    for kappa in (.6,1.2,2.5): add_case(rows,"effort_cost",f"kappa_{kappa}",replace(base,kappa=kappa))
    for rho in (0,.45,.9): add_case(rows,"persistence",f"rho_{rho}",replace(base,rho=rho))
    for alpha in (.3,.55,.8): add_case(rows,"rehabilitation",f"alpha_{alpha}",replace(base,alpha=alpha))
    for detection in (.25,.65,.95): add_case(rows,"detection",f"detection_{detection}",replace(base,detection_probability=detection))
    for threshold in (.35,.5,.65):
        add_case(rows,"normalization",f"threshold_{threshold}",replace(base,threshold=threshold,bad_record=max(0,threshold-.45),good_signal=min(1,threshold+.35)))
    for name,population in populations().items(): add_case(rows,"initial_distribution",name,base,population)
    for horizon in (3,6,12,20,30,50): add_case(rows,"horizon",f"T_{horizon}",replace(base,horizon=horizon),allow_repeat=horizon<=20)
    for beta in (.7,.85,.95,.99): add_case(rows,"discounting",f"beta_{beta}",replace(base,beta=beta))
    for harm in (.3,1.2,3): add_case(rows,"social_harm",f"harm_{harm}",replace(base,misconduct_harm=harm))
    for benefit in (.75,1.5,3): add_case(rows,"private_benefit",f"benefit_{benefit}",replace(base,private_benefit_max=benefit))
    for benefit in (.75,1.5,3):
        for detection in (.25,.65):
            for horizon in (12,20):
                add_case(rows,"repeat_misconduct",f"b_{benefit}_d_{detection}_T_{horizon}",replace(base,private_benefit_max=benefit,detection_probability=detection,horizon=horizon))
    for penalty in (0,.25,.5,1,2): add_case(rows,"direct_punishment",f"penalty_{penalty}",replace(base,direct_penalty=penalty))
    # Common-policy heterogeneity: average the objective across two latent types.
    for label, field, lo, hi in (("alpha_mix","alpha",.3,.8),("rho_mix","rho",0,.9)):
        ps = (replace(base,**{field:lo}),replace(base,**{field:hi}))
        fixed=[]; two=[]
        for c in GRID:
            for a in GRID:
                vals=[evaluate_adaptive(AdaptivePolicy(c,a,a,1),p) for p in ps]
                result={"welfare":sum(v["welfare"] for v in vals)/2,"parameters":AdaptivePolicy(c,a,a,1),
                        "misconduct_events":sum(v["misconduct_events"] for v in vals)/2,
                        "repeat_misconduct":sum(v["repeat_misconduct"] for v in vals)/2,
                        "discounted_effort":sum(v["discounted_effort"] for v in vals)/2,
                        "discounted_quality":sum(v["discounted_quality"] for v in vals)/2,
                        "prediction_mse":sum(v["prediction_mse"] for v in vals)/2}
                two.append(result)
                if c==a: fixed.append(result)
        f=max(fixed,key=lambda x:x["welfare"]); a=max(two,key=lambda x:x["welfare"])
        fp,ap=f["parameters"],a["parameters"]
        rows.append({"family":"heterogeneity","specification":label,"horizon":base.horizon,"fixed_phi":fp.phi_clean,
                     "clean_phi":ap.phi_clean,"nonclean_phi":ap.phi_adverse,"fixed_welfare":f["welfare"],
                     "adaptive_welfare":a["welfare"],"gain":a["welfare"]-f["welfare"],
                     "fixed_misconduct":f["misconduct_events"],"adaptive_misconduct":a["misconduct_events"],
                     "adaptive_repeat":a["repeat_misconduct"],"adaptive_effort":a["discounted_effort"],
                     "adaptive_quality":a["discounted_quality"],"prediction_mse":a["prediction_mse"],
                     "nested_ok":a["welfare"]+1e-10>=f["welfare"],"allow_repeat":True})
    OUT.mkdir(parents=True,exist_ok=True); TABLE.parent.mkdir(parents=True,exist_ok=True)
    with TABLE.open("w",newline="",encoding="utf-8") as h:
        w=csv.DictWriter(h,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    families={}
    for family in sorted(set(r["family"] for r in rows)):
        group=[r for r in rows if r["family"]==family]
        families[family]={"tests":len(group),"positive":sum(r["gain"]>1e-8 for r in group),
                          "material":sum(r["gain"]>=.01 for r in group),"min_gain":min(r["gain"] for r in group),
                          "max_gain":max(r["gain"] for r in group)}
    metadata={"model":"M7-v1","deterministic":True,"seed":None,"memory_grid":GRID,
              "effort_grid":101,"runtime_seconds":time.time()-started,"tests":len(rows),
              "all_nested":all(r["nested_ok"] for r in rows),"families":families}
    solver_rows=effort_solver_check(replace(base,effort_grid_size=501))
    with (ROOT/"outputs"/"tables"/"m7_effort_solver.csv").open("w",newline="",encoding="utf-8") as h:
        w=csv.DictWriter(h,fieldnames=list(solver_rows[0]));w.writeheader();w.writerows(solver_rows)
    metadata["continuous_effort_max_difference"]=max(r["absolute_difference"] for r in solver_rows)
    (OUT/"metadata.json").write_text(json.dumps(metadata,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(metadata,indent=2))


if __name__=="__main__": main()
