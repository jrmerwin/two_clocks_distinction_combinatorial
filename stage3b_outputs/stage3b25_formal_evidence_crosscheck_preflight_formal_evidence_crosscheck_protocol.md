# Stage 3B-25 formal evidence-estimator cross-check protocol

Generated UTC: `2026-05-09T05:00:44+00:00`

This stage is a preflight only. It does not compute evidence, does not launch MCMC, and does not allow model-superiority claims.

## Current status

- Stage 3B-24 decision: `EVIDENCE_RESULT_SENSITIVITY_AUDIT_PASS_PROXY_ONLY_FORMAL_CLAIMS_STILL_GATED`
- Proxy log-BF DEU-minus-native: `158.76404705020616`
- Formal Bayes-factor claims allowed: `False`
- Model-superiority claims allowed: `False`

## Candidate formal/cross-check estimators

| Estimator | Kind | Uses current chains | Requires new sampling | Status |
|---|---|---:|---:|---|
| bridge_sampling_crosscheck | formal_crosscheck_candidate | True | False | preflighted_not_executed |
| nested_sampling_matched_full_objective | formal_evidence_candidate | False | True | design_only_not_executed |
| thermodynamic_integration_ladder | formal_evidence_candidate | False | True | design_only_not_executed |
| laplace_proxy_independent_reimplementation | diagnostic_proxy_crosscheck | True | False | preflighted_not_executed |
| tt_lite_inclusive_matched_evidence_design | new_matched_design_required | False | True | blocked_until_tt_lite_matched_sampler_is_booked |

## Required controls before any formal claim

- Same matched full-objective likelihood scope on DEU and native sides.
- Same shared priors for `omega_b`, `n_s`, and `A_planck`.
- DEU-only prior-volume contribution for `beta` and `p_vis` explicitly counted.
- Estimator uncertainty, numerical sensitivity, and prior-volume sensitivity recorded.
- TT_lite remains diagnostic-only unless a separate TT_lite-inclusive branch is booked.
