import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_m6_5_audit_covers_atlas_and_preserves_nesting():
    with (ROOT / "outputs" / "tables" / "m6_5_audit.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 36
    assert all(row["nested_ok"] == "True" for row in rows)
    assert sum(float(row["refined_gain"]) > 1e-8 for row in rows) == 34


def test_all_original_large_points_remain_positive():
    with (ROOT / "outputs" / "tables" / "m6_5_audit.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    large = [row for row in rows if row["original_regime"] == "LARGE"]
    assert len(large) == 13
    assert all(float(row["refined_gain"]) > 0 for row in large)
