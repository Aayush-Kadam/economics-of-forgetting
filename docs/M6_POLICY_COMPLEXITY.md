# M6 Policy Complexity

| Class | Parameters | Mean gain over P0 |
|---|---:|---:|
| P0 constant | 1 | 0 |
| P1 clean/nonclean | 2 | `.188` |
| P2 clean/adverse/rehab | 3 | `.305` |
| P3 lifecycle plus streak threshold | 4 | `1.117` |

P2 strictly improves on P1 at 12 of 36 points; P3 strictly improves on P2 at 19. The large P3 gain must be interpreted cautiously because the streak threshold changes recovery and reoffense eligibility as well as memory timing. It is not pure value of an additional score-decay parameter.

The simple P1 efficiency ratio is stored pointwise relative to P3. No full arbitrary state-contingent or dynamic-policy ceiling is claimed.
