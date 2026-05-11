# Stage 3B-19 matched DEU/native comparison summary

Generated UTC: `2026-05-09T03:27:34+00:00`

This stage does not launch MCMC. It summarizes the matched native/baseline posterior side and compares it descriptively to the caveated DEU posterior summary.

## Native posterior summary

| Parameter | Mean | SD | q16 | q50 | q84 |
|---|---:|---:|---:|---:|---:|
| omega_b | 0.021934117 | 2.8648401e-05 | 0.021907334 | 0.02192558 | 0.021965164 |
| n_s | 0.98177763 | 0.00051560051 | 0.98117982 | 0.98186963 | 0.98230608 |
| A_planck | 1.0200423 | 0.00012027436 | 1.0200057 | 1.0200261 | 1.02007 |

## DEU/native descriptive comparison

| Parameter | DEU mean | Native mean | DEU - native | shift / quadrature SD |
|---|---:|---:|---:|---:|
| omega_b | 0.021980021 | 0.021934117 | 4.5904254e-05 | 0.80218681 |
| n_s | 0.98152322 | 0.98177763 | -0.00025440994 | -0.33162241 |
| A_planck | 1.0250557 | 1.0200423 | 0.0050134312 | 5.8639125 |
| beta | 0.029491217 |  |  |  |
| p_vis | 1.0474182 |  |  |  |

## Reference/loglike context

- `native_reference_eval_status` = `success` (configuration/readiness context only)
- `native_reference_matches_stage3b15_sampler_ref` = `True` (configuration/readiness context only)
- `native_reference_matches_stage3b16_checkpoint` = `True` (configuration/readiness context only)
- `native_tt_lite_excluded` = `True` (configuration/readiness context only)
- `native_config_has_no_deu_keys` = `True` (configuration/readiness context only)
- `deu_shape_params_absent_from_native_sampler` = `True` (configuration/readiness context only)

## Claim lock

Decision: `MATCHED_DEU_NATIVE_COMPARISON_SUMMARY_PASS_SUPERIORITY_STILL_GATED`

Next stage: `Stage 3B-20 final scoped internal report or explicit evidence/model-selection design`
