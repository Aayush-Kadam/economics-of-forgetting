# M8 reproducibility audit

- Platform: Windows, Python 3.12.
- Core command: `python scripts/reproduce_core.py`.
- Core result: PASS; 54 tests; 71.7 seconds.
- Full command: `python scripts/reproduce_full.py`.
- Full result: PASS; 54 tests plus every M1-M7 deterministic computation and PDF rebuild; 868.1 seconds.
- The first full attempt reached the M6 atlas but exceeded a 604-second process ceiling. It was rerun from the documented entry point with a 25-minute ceiling and completed normally.
- M7 robustness: 61 tests, all nested, continuous-effort maximum difference 0.0009714347.
- Randomness: deterministic drivers; metadata records null seeds where no random draw is used.
- Build: the documented PDF fallback uses ReportLab for layout and Matplotlib mathtext for native mathematical glyphs because no local LaTeX engine was available.

The regenerated JSON runtime fields and raster figure metadata may differ across machines while scientific values remain deterministic. The review candidate records the observed local runtimes rather than treating them as scientific output.
