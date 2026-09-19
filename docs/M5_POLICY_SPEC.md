# M5 Policy Specification

The institution commits at `t=0` to `Psi=(phi_clean,phi_adverse,phi_rehab,m)`. Clean histories use `phi_clean`; an adverse history uses `phi_adverse`; after `m` consecutive favorable quality signals it uses `phi_rehab`. A recovered score returns the agent to clean status. New adverse events reset the streak. Constant memory is nested by setting all three persistence parameters equal.

The public rule is known before effort and misconduct. The finite-horizon solver carries probability mass over quality, score, lifecycle, streak, and offense count. It permits repeat misconduct after recovery and reports expected recurrence. Calendar decay and behavior-contingent decay are separate policy choices.
