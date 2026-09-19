"""Regenerate core figures, tables, tests, and the local manuscript PDF."""

import subprocess
import sys
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def run(*args):
    subprocess.run([sys.executable,*args],cwd=ROOT,check=True)


def main():
    start=time.time()
    subprocess.run([sys.executable,"-m","pytest","-q"],cwd=ROOT,check=True)
    for script in ("build_m1_figures.py","run_m3_counterfactuals.py","run_m4_planner.py","run_m5_analysis.py"):
        run("scripts/"+script)
    run("scripts/build_paper.py")
    print(f"Core reproduction completed in {time.time()-start:.1f} seconds")


if __name__=="__main__": main()
