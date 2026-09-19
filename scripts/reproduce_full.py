"""Regenerate the full deterministic research package."""

import subprocess
import sys
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def run(script,*args):
    subprocess.run([sys.executable,"scripts/"+script,*args],cwd=ROOT,check=True)


def main():
    start=time.time()
    subprocess.run([sys.executable,"-m","pytest","-q"],cwd=ROOT,check=True)
    for script in ("build_m1_figures.py","run_m3_counterfactuals.py","run_m3_5_audit.py","run_m4_planner.py",
                   "run_m4_counterexamples.py","run_m4_5_audit.py","run_m5_analysis.py","run_m5_5_audit.py",
                   "run_m6_atlas.py","run_m6_5_audit.py","run_m7_robustness.py"):
        run(script)
    run("build_paper.py")
    print(f"Full reproduction completed in {time.time()-start:.1f} seconds")


if __name__=="__main__": main()
