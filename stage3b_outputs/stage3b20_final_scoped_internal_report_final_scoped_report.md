# Stage 3B-20 final scoped internal report

Generated UTC: `2026-05-09T03:41:33+00:00`

This report consolidates the scoped DEU posterior, matched native/baseline descriptive comparison, tri-anchor context, and claim lock.
It is an internal staged report. It is not a model-superiority result, not a Bayes-factor/evidence result, and not a final publication claim.

## Decision

Decision type: `FINAL_SCOPED_INTERNAL_REPORT_PASS_SUPERIORITY_STILL_GATED`

Recommendation: Book Stage 3B-20 as the final scoped internal report. Stronger model-superiority, evidence/Bayes-factor, or publication-style claims require an explicit evidence/model-selection stage.

Next-stage hint: `Stage 3B-21 explicit evidence/model-selection design or publication-claim preflight`

## DEU posterior summary

| Parameter | Mean | SD | q16 | q50 | q84 |
|---|---:|---:|---:|---:|---:|
| beta | 0.029491217 | 0.00055247252 | 0.028849905 | 0.029503285 | 0.030128599 |
| p_vis | 1.0474182 | 0.0013180231 | 1.0459375 | 1.0473475 | 1.048932 |
| omega_b | 0.021980021 | 4.9536282e-05 | 0.021927323 | 0.021972856 | 0.0220347 |
| n_s | 0.98152322 | 0.00056806878 | 0.98086835 | 0.9815207 | 0.98217567 |
| A_planck | 1.0250557 | 0.00084646128 | 1.0242044 | 1.0250715 | 1.0259026 |

## Native/baseline posterior summary

| Parameter | Mean | SD | q16 | q50 | q84 |
|---|---:|---:|---:|---:|---:|
| omega_b | 0.021934117 | 2.8648401e-05 | 0.021907334 | 0.02192558 | 0.021965164 |
| n_s | 0.98177763 | 0.00051560051 | 0.98117982 | 0.98186963 | 0.98230608 |
| A_planck | 1.0200423 | 0.00012027436 | 1.0200057 | 1.0200261 | 1.02007 |

## Matched descriptive comparison

| Parameter | DEU mean | Native mean | Shift / quadrature sd | Interpretation limit |
|---|---:|---:|---:|---|
| omega_b | 0.021980021 | 0.021934117 | 0.80218681 | descriptive posterior comparison only; not model evidence or superiority |
| n_s | 0.98152322 | 0.98177763 | -0.33162241 | descriptive posterior comparison only; not model evidence or superiority |
| A_planck | 1.0250557 | 1.0200423 | 5.8639125 | descriptive posterior comparison only; not model evidence or superiority |
| beta | 0.029491217 |  |  | DEU-only shape parameter; no native analogue |
| p_vis | 1.0474182 |  |  | DEU-only shape parameter; no native analogue |

## Tri-anchor context

| Anchor | beta | p_vis | omega_b | n_s | A_planck | profile |
|---|---:|---:|---:|---:|---:|---:|
| highl_anchor | 0.029 | 1.0475 | 0.02195 | 0.98 | 1.025 | 2 |
| lowl_plus_anchor | 0.0295 | 1.0475 | 0.02195 | 0.98125 | 1.025 | 2 |
| full_objective_working_lock | 0.03 | 1.0475 | 0.022 | 0.981875 | 1.025 | 2 |

## Claim lock

Allowed: scoped/caveated internal DEU posterior and descriptive DEU/native posterior comparison.

Blocked: model-superiority, Bayes-factor/evidence, TT_lite-in-posterior, and final publication-style claims.
