# Stage 3B-13 scoped final-claim lock

Generated UTC: `2026-05-09T00:34:11+00:00`

This stage does not launch MCMC. It locks the current claim scope after the Stage 3B-12 external/model-comparison preflight.

Decision type: `SCOPED_FINAL_CLAIM_LOCK_PASS_MODEL_COMPARISON_EXTENSION_REQUIRED`

Recommendation: Book Stage 3B-13. Use only the allowed scoped/caveated posterior claims. Next run an explicit baseline/native model-comparison extension before model-superiority or publication-style claims.

Next-stage hint: `Stage 3B-14 explicit baseline/native model-comparison extension`

## Claim status

- Scoped internal posterior claims allowed: `True`
- Final publication claims allowed: `False`
- Model-superiority claims allowed: `False`

## Parameter claim summary

| Parameter | Mean | Median | q16 | q84 | Claim status |
|---|---:|---:|---:|---:|---|
| beta | 0.02949121724807528 | 0.029503285 | 0.028849905 | 0.030128599 | caveated_internal_posterior_summary_allowed |
| p_vis | 1.0474182267750214 | 1.0473475 | 1.0459375 | 1.048932 | caveated_internal_posterior_summary_allowed |
| omega_b | 0.021980020954662106 | 0.021972856 | 0.021927323 | 0.0220347 | caveated_internal_posterior_summary_allowed |
| n_s | 0.9815232201591104 | 0.9815207 | 0.98086835 | 0.98217567 | caveated_internal_posterior_summary_allowed |
| A_planck | 1.0250557243798117 | 1.0250715 | 1.0242044 | 1.0259026 | caveated_internal_posterior_summary_allowed |

## Allowed scoped claims

- **allowed_001**: A caveated posterior summary exists for the DEU full-objective working-lock production sampler.
- **allowed_002**: The production posterior used the full-objective likelihood set and the guarded working-lock configuration.
- **allowed_003**: The readiness and robustness gates passed on two production chain files and 4000 combined rows.
- **allowed_004**: The tri-anchor context is retained as a monitoring caveat around the full-objective posterior.
- **allowed_005**: TT_lite may be described as diagnostic-only monitoring context, not part of the sampled posterior likelihood.
- **param_beta**: Posterior summary for beta: mean=0.02949121724807528, median=0.029503285, q16=0.028849905, q84=0.030128599.
- **param_p_vis**: Posterior summary for p_vis: mean=1.0474182267750214, median=1.0473475, q16=1.0459375, q84=1.048932.
- **param_omega_b**: Posterior summary for omega_b: mean=0.021980020954662106, median=0.021972856, q16=0.021927323, q84=0.0220347.
- **param_n_s**: Posterior summary for n_s: mean=0.9815232201591104, median=0.9815207, q16=0.98086835, q84=0.98217567.
- **param_A_planck**: Posterior summary for A_planck: mean=1.0250557243798117, median=1.0250715, q16=1.0242044, q84=1.0259026.

## Blocked claims

- **blocked_001**: DEU is superior to ΛCDM or the native baseline. — No explicit baseline/native model-comparison evidence stage has been booked.
- **blocked_002**: The production posterior includes TT_lite. — TT_lite was diagnostic-only and excluded from the production sampler likelihood.
- **blocked_003**: Final publication-style claim or external robustness claim. — Stage 3B-12 explicitly kept final publication claims blocked.
- **blocked_004**: All Planck likelihood components prefer the same DEU anchor. — The tri-anchor split is retained and must remain visible.
- **blocked_005**: The MAP-like chain row is an optimizer result or independent best fit. — Stage 3B-10 records it as a chain diagnostic only.

## Required extensions

- **ext_001**: Explicit native/baseline model-comparison extension — Compare DEU scoped posterior/fit context against native/baseline under matched likelihood scope.
- **ext_002**: Final publication-claim lock — Review all caveats, TT_lite scope, tri-anchor context, and model-comparison evidence before external claims.
- **ext_003**: TT_lite-inclusive sensitivity sampler or fixed diagnostic — Clarify whether diagnostic TT_lite behavior changes the production posterior story.
- **ext_004**: Best-fit optimizer check at/near posterior summary — Avoid overinterpreting chain MAP-like rows as optimizer outputs.
