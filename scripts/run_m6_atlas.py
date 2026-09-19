"""Deterministic checkpointed M6 computational atlas."""

import csv,json,subprocess,time
from dataclasses import replace
from itertools import product
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"src"))
from economics_of_forgetting.m4 import DEFAULT_POPULATION,PlannerParameters  # noqa:E402
from economics_of_forgetting.m6 import best_from_policies,classify_fixed,classify_value,efficiency_ratio,memory_conflict_index,policy_classes  # noqa:E402
from economics_of_forgetting.parameter_registry import PARAMETER_REGISTRY,validate_registry  # noqa:E402

OUT=ROOT/"experiments"/"m6_atlas";TAB=ROOT/"outputs"/"tables";FIG=ROOT/"outputs"/"figures";CHECK=OUT/"checkpoint.csv"


def write_rows(path,rows):
    with path.open("w",newline="",encoding="utf-8") as h:
        w=csv.DictWriter(h,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)


def main(smoke=False):
    start=time.time();OUT.mkdir(parents=True,exist_ok=True);TAB.mkdir(parents=True,exist_ok=True);FIG.mkdir(parents=True,exist_ok=True)
    validate_registry(); classes=policy_classes((0,.45,.85,.99))
    design=list(product((0,.45,.9),(.3,.55,.8),(.6,1.8),(6,12)))
    if smoke:design=design[:3]
    rows=[]; checkpoint_path=OUT/("checkpoint_smoke.csv" if smoke else "checkpoint.csv")
    for idx,(rho,alpha,harm,horizon) in enumerate(design):
        p=PlannerParameters(rho=rho,alpha=alpha,misconduct_harm=harm,horizon=horizon,effort_grid_size=101)
        opt={};allrows={}
        for name,policies in classes.items():opt[name],allrows[name]=best_from_policies(p,policies)
        fixed=opt["P0_constant"];two=opt["P1_two_state"];three=opt["P2_three_state"];threshold=opt["P3_threshold"];earned=opt["earned_diagnostic"]
        welfare_range=max(x["welfare"] for x in allrows["P2_three_state"])-min(x["welfare"] for x in allrows["P2_three_state"])
        pred=min(allrows["P0_constant"],key=lambda x:x["prediction_mse"])
        fp=fixed["parameters"];tp=two["parameters"];xp=three["parameters"]
        confirming=sum(s.weight for s in DEFAULT_POPULATION if s.reputation<.5)
        correcting=sum(s.weight for s in DEFAULT_POPULATION if s.reputation>.5)
        row={"index":idx,"rho":rho,"alpha":alpha,"misconduct_harm":harm,"horizon":horizon,
             "fixed_phi":fp.phi_clean,"fixed_regime":classify_fixed(fp.phi_clean),
             "two_clean":tp.phi_clean,"two_nonclean":tp.phi_adverse,"three_clean":xp.phi_clean,
             "three_adverse":xp.phi_adverse,"three_rehab":xp.phi_rehab,
             "fixed_welfare":fixed["welfare"],"two_welfare":two["welfare"],"three_welfare":three["welfare"],
             "earned_welfare":earned["welfare"],"adaptive_value":two["welfare"]-fixed["welfare"],
             "adaptive_regime":classify_value(two["welfare"]-fixed["welfare"],welfare_range),
             "three_increment":three["welfare"]-two["welfare"],"threshold_welfare":threshold["welfare"],
             "threshold_increment":threshold["welfare"]-three["welfare"],"earned_increment":earned["welfare"]-fixed["welfare"],
             "p1_efficiency":efficiency_ratio(two["welfare"],fixed["welfare"],threshold["welfare"]),
             "prediction_phi":pred["parameters"].phi_clean,"prediction_order":"LONGER" if pred["parameters"].phi_clean>fp.phi_clean else "SHORTER" if pred["parameters"].phi_clean<fp.phi_clean else "SAME",
             "prediction_mse":two["prediction_mse"],"misconduct":two["misconduct_events"],"repeat_misconduct":two["repeat_misconduct"],
             "effort":two["discounted_effort"],"quality":two["discounted_quality"],"memory_conflict":memory_conflict_index(p),
             "self_confirming_mass":confirming,"self_correcting_mass":correcting,
             "nested_ok":threshold["welfare"]+1e-10>=three["welfare"]>=two["welfare"]>=fixed["welfare"]-1e-10,
             "finite_ok":all(np.isfinite([fixed["welfare"],two["welfare"],three["welfare"]]))}
        rows.append(row);write_rows(checkpoint_path,rows)
    write_rows(TAB/("m6_atlas_smoke.csv" if smoke else "m6_atlas.csv"),rows)
    if smoke:return
    prevalence=[]
    for field in ("fixed_regime","adaptive_regime","prediction_order"):
        for value in sorted(set(r[field] for r in rows)):
            count=sum(r[field]==value for r in rows);prevalence.append({"dimension":field,"regime":value,"count":count,"design_fraction":count/len(rows)})
    write_rows(TAB/"m6_regime_prevalence.csv",prevalence)
    complexity=[]
    for name,count in (("P0_constant",1),("P1_two_state",2),("P2_three_state",3),("P3_threshold",4)):
        vals=[r[{"P0_constant":"fixed_welfare","P1_two_state":"two_welfare","P2_three_state":"three_welfare","P3_threshold":"threshold_welfare"}[name]] for r in rows]
        complexity.append({"policy_class":name,"parameters":count,"mean_welfare":float(np.mean(vals)),"mean_gain_over_p0":float(np.mean(np.asarray(vals)-np.asarray([r["fixed_welfare"] for r in rows])))})
    write_rows(TAB/"m6_policy_complexity.csv",complexity)
    fig,ax=plt.subplots(figsize=(6.4,4.5));sc=ax.scatter([r["memory_conflict"] for r in rows],[r["adaptive_value"] for r in rows],c=[r["alpha"] for r in rows],cmap="viridis");ax.set(xlabel="Memory-conflict index",ylabel="Two-state adaptive value",title="Memory conflict and flexibility value");fig.colorbar(sc,ax=ax,label="alpha");fig.tight_layout();fig.savefig(FIG/"m6_memory_conflict_value.png",dpi=180);plt.close(fig)
    fig,ax=plt.subplots(figsize=(6.4,4.5));ax.hist([r["adaptive_value"] for r in rows],bins=12);ax.set(xlabel="Adaptive value",ylabel="Predeclared design points",title="Distribution across computational design");fig.tight_layout();fig.savefig(FIG/"m6_adaptive_value_distribution.png",dpi=180);plt.close(fig)
    fig,ax=plt.subplots(figsize=(6.4,4.5));ax.plot([x["parameters"] for x in complexity],[x["mean_gain_over_p0"] for x in complexity],marker="o");ax.set(xlabel="Policy parameters",ylabel="Mean gain over P0",title="Policy complexity frontier");fig.tight_layout();fig.savefig(FIG/"m6_policy_complexity.png",dpi=180);plt.close(fig)
    metadata={"model_version":"M6-v1","git_commit":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),"deterministic":True,"seed":None,"design_points":len(rows),"effort_grid":101,"memory_grid":[0,.45,.85,.99],"streaks":[1,2,3],"runtime_seconds":time.time()-start,"parameters":PARAMETER_REGISTRY}
    (OUT/"metadata.json").write_text(json.dumps(metadata,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"metadata":metadata,"prevalence":prevalence,"all_nested":all(r["nested_ok"] for r in rows)},indent=2))


if __name__=="__main__":main("--smoke" in sys.argv)
