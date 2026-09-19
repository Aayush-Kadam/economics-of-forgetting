# MILESTONE
M8 — local external-review candidate

# STATUS
Complete.

# VERDICT
Ready for external review as a narrow theory note.

# RECOVERY STATUS
Interrupted M8 work was preserved in recovery commit `89c3a88`; continuation was incremental.

# M7.5 VERDICT
READY FOR M8 WITH FURTHER NARROWING.

# M7.5 FREEZE COMMIT
`657ba85f6955aaa21e89c16dd24c5a6fd1f81fb1`

# FINAL TITLE
Persistent Records and Rehabilitation Incentives

# AUTHOR
Aayush Kadam

# FINAL PAPER ARCHITECTURE
Theory-first main text with two core contributions; proofs, mechanism qualifications, and numerical design exercises in the technical appendix.

# CORE CONTRIBUTION 1
Regional lifecycle asymmetry: persistence can strengthen ex ante discipline while reducing productive post-event effort on a nonempty open region.

# CORE CONTRIBUTION 2
Institution-produced future-quality divergence: records that alter effort can create next-period quality differences at intrinsic persistence `rho=0`, with finite-horizon propagation under repeated effort differences.

# SECONDARY / APPENDIX RESULTS
Self-confirming versus self-correcting feedback, planner counterexamples, adaptive design, parameter atlas, and robustness exercises.

# DROPPED CLAIMS
No global lifecycle theorem, universal optimal half-life, general policy case for forgetting, empirical causal estimate, or third core contribution.

# CLOSEST LITERATURE
Career concerns and endogenous reputation, strategic information persistence, and feedback from beliefs to real outcomes. The manuscript states a narrow mechanism-level distinction rather than priority over these literatures.

# FINAL NOVELTY CLAIM
Within one canonical lifecycle model, persistent records jointly affect pre-event discipline and post-event productive recovery, and the induced effort response can itself generate future-quality divergence even when intrinsic quality is not persistent.

# CANONICAL MODEL
Finite-horizon reputation state, record-memory parameter, endogenous productive effort, misconduct incentives, and a quality transition separating intrinsic persistence from effort-produced persistence.

# MAIN THEOREMS
Comparative statics for deterrence and rehabilitation effort; an open-region lifecycle-asymmetry result; and an identity/decomposition for institution-produced quality divergence.

# MAIN COMPUTATIONAL RESULTS
Matched-shock zero-rho examples, finite-horizon propagation, both feedback signs, and appendix-only state-contingent design calculations.

# PDF RENDERING FIX
The fallback renderer now typesets display mathematics as high-resolution native mathematical glyphs, preserves equation numbering, and imports the complete technical appendix. No source-pointer placeholders remain.

# TECHNICAL APPENDIX STATUS
Complete and included in the PDF; milestone-log labels were replaced by paper-facing section names.

# MAIN FIGURES
Lifecycle effort asymmetry and finite-horizon feedback/path illustrations.

# MAIN TABLES
Parameter definitions and appendix-only computational summaries.

# HOSTILE REFEREE VERDICT
MAJOR REVISION at first pass.

# REFEREE REVISIONS IMPLEMENTED
The numerical design exercise was removed from the main-text contribution architecture, claims were narrowed to regional and finite-horizon statements, and limitations/collision risks were made explicit.

# CLAIM AUDIT
Passed. Every headline claim is linked to support, proof location, robustness, collision risk, and allowed wording in `docs/M8_CLAIM_AUDIT.md`.

# JOURNAL FIT
Primary: Review of Economic Design. Backups: Economic Theory Bulletin and Journal of Economic Behavior & Organization; Games and Economic Behavior is a stretch target.

# TEST STATUS
PASS — 54 tests.

# CORE REPRODUCTION STATUS
PASS — 71.7 seconds.

# FULL REPRODUCTION STATUS
PASS — 868.1 seconds.

# PAPER BUILD STATUS
PASS — `paper/manuscript.pdf` built locally.

# PAGE-BY-PAGE VISUAL INSPECTION
PASS — all 12 post-reproduction pages inspected; equations, figures, appendix, references, margins, and pagination are legible with no clipping or placeholder formulas.

# REPOSITORY STATE
Recovery branch with logical M8 commits and no publication or remote push.

# CURRENT BRANCH
`recovery/m8-interrupted-session`

# CURRENT COMMIT
The commit targeted by the local M8 tag; resolve exactly with `git rev-list -n 1 m8-external-review-candidate`.

# CURRENT TAG
`m8-external-review-candidate`

# PAPER PDF PATH
`paper/manuscript.pdf`

# REPRODUCTION COMMAND
`python scripts/reproduce_core.py` (core); `python scripts/reproduce_full.py` (complete).

# KNOWN LIMITATIONS
Reduced-form opportunity and reputation mapping; finite horizon; no empirical identification; regional rather than global results; numerical design gains can be small; fallback PDF is not a journal typesetting source of record.

# OPEN QUESTIONS
Whether the lifecycle asymmetry survives richer equilibrium selection, endogenous information acquisition, and empirically disciplined primitives.

# FINAL DECISION
READY FOR EXTERNAL REVIEW
