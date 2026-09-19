"""Reproduce M5 policy comparisons, robustness, placebos, and figures."""

import csv
from dataclasses import replace
import json
from pathlib import Path
import sys

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from economics_of_forgetting.m4 import PlannerParameters  # noqa: E402
from economics_of_forgetting.m5 import evaluate_adaptive, optimize_adaptive  # noqa: E402

OUT=ROOT/"experiments"/"m5_adaptive_memory"; TAB=ROOT/"outputs"/"tables"; FIG=ROOT/"outputs"/"figures"


def serial(row):
    result={k:v for k,v in row.items() if k!="parameters"}
    if "parameters" in row: result["parameters"]=row["parameters"].__dict__
    return result


def write_csv(path, rows):
    with path.open("w",newline="",encoding="utf-8") as h:
        w=csv.DictWriter(h,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)


def main():
    OUT.mkdir(parents=True,exist_ok=True);TAB.mkdir(parents=True,exist_ok=True);FIG.mkdir(parents=True,exist_ok=True)
    p=PlannerParameters(effort_grid_size=201)
    suites={f:optimize_adaptive(p,family=f) for f in ("constant","earned","lifecycle")}
    rows=[]
    for family,result in suites.items():
        x=result["optimum"]; pol=x["parameters"]
        rows.append({"mechanism":family,"phi_clean":pol.phi_clean,"phi_adverse":pol.phi_adverse,
                     "phi_rehab":pol.phi_rehab,"streak":pol.good_streak_required,
                     "welfare":x["welfare"],"value_over_fixed":result["value_over_fixed"],
                     "misconduct":x["misconduct_events"],"repeat_misconduct":x["repeat_misconduct"],
                     "effort":x["discounted_effort"],"quality":x["discounted_quality"],"prediction_mse":x["prediction_mse"]})
    write_csv(TAB/"m5_mechanism_comparison.csv",rows)

    robustness=[]
    for alpha in (0,.3,.55,.8):
        for harm in (0,.6,1.2,2.4):
            q=replace(p,alpha=alpha,misconduct_harm=harm,effort_grid_size=101)
            r=optimize_adaptive(q,family="lifecycle")
            pol=r["optimum"]["parameters"]
            robustness.append({"alpha":alpha,"misconduct_harm":harm,"value_of_adaptation":r["value_over_fixed"],
                               "phi_clean":pol.phi_clean,"phi_adverse":pol.phi_adverse,"phi_rehab":pol.phi_rehab,
                               "streak":pol.good_streak_required})
    write_csv(TAB/"m5_strict_dominance_regions.csv",robustness)

    best=suites["lifecycle"]["optimum"]["parameters"]
    placebos=[]
    for name,q,independent,repeats in (
        ("baseline",p,False,True),("alpha_zero",replace(p,alpha=0),False,True),
        ("no_misconduct",replace(p,misconduct_harm=0),False,True),
        ("effort_independent",p,True,True),("no_repeat_misconduct",p,False,False)):
        x=evaluate_adaptive(best,q,effort_independent=independent,allow_repeat_misconduct=repeats)
        placebos.append({"placebo":name,**{k:x[k] for k in ("welfare","discounted_effort","misconduct_events","repeat_misconduct","prediction_mse")}})
    write_csv(TAB/"m5_placebos.csv",placebos)

    fig,ax=plt.subplots(figsize=(6.5,4.3));ax.bar([r["mechanism"] for r in rows],[r["welfare"] for r in rows]);ax.set(ylabel="Expected welfare",title="Fixed, earned, and lifecycle memory");fig.tight_layout();fig.savefig(FIG/"m5_mechanism_welfare.png",dpi=180);plt.close(fig)
    fig,ax=plt.subplots(figsize=(6.5,4.3));
    for r in rows: ax.scatter(r["prediction_mse"],r["welfare"],s=70,label=r["mechanism"])
    ax.set(xlabel="Prediction MSE",ylabel="Welfare",title="Prediction–welfare comparison");ax.legend();fig.tight_layout();fig.savefig(FIG/"m5_prediction_welfare.png",dpi=180);plt.close(fig)
    fig,ax=plt.subplots(figsize=(6.5,4.3));
    for r in rows: ax.scatter(r["misconduct"],r["effort"],s=70,label=r["mechanism"])
    ax.set(xlabel="Expected misconduct events",ylabel="Discounted rehabilitation effort",title="Deterrence–rehabilitation outcomes");ax.legend();fig.tight_layout();fig.savefig(FIG/"m5_deterrence_rehabilitation.png",dpi=180);plt.close(fig)

    summary={"mechanisms":rows,"robustness":robustness,"placebos":placebos,
             "raw_optima":{k:serial(v["optimum"]) for k,v in suites.items()}}
    (OUT/"m5_results.json").write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2))


if __name__=="__main__": main()
