# Stage 3B-14 baseline/native model-comparison extension

Generated UTC: `2026-05-09T00:51:08+00:00`

This stage does not launch MCMC. It records model-comparison scope and keeps model-superiority/final publication claims gated.

## Decision

Decision type: `BASELINE_NATIVE_MODEL_COMPARISON_EXTENSION_PASS_SUPERIORITY_STILL_GATED`

Recommendation: Book Stage 3B-14. Use only scoped posterior-summary language; run a matched native/baseline comparison or evidence stage before model-superiority or final publication claims.

Next-stage hint: `Stage 3B-15 matched native/baseline comparison preflight or final scoped report`

## Posterior recap

| Parameter | mean | q16 | q50 | q84 | working lock |
|---|---:|---:|---:|---:|---:|
| beta | 0.02949121724807528 | 0.028849905 | 0.029503285 | 0.030128599 | 0.03 |
| p_vis | 1.0474182267750214 | 1.0459375 | 1.0473475 | 1.048932 | 1.0475 |
| omega_b | 0.021980020954662106 | 0.021927323 | 0.021972856 | 0.0220347 | 0.022 |
| n_s | 0.9815232201591104 | 0.98086835 | 0.9815207 | 0.98217567 | 0.981875 |
| A_planck | 1.0250557243798117 | 1.0242044 | 1.0250715 | 1.0259026 | 1.025 |

## Native/baseline context

Rows recorded: `24`

This context is not a Bayes factor, evidence ratio, or matched native posterior comparison.

## Model-superiority gate

| Gate | Pass | Allows superiority claim | Meaning |
|---|---:|---:|---|
| native_baseline_context_recorded | True | False | There is recorded native/baseline context to discuss scope. |
| matched_native_posterior_or_evidence_available | False | False | No booked matched native/baseline posterior or evidence/Bayes-factor calculation is present in Stage 3B artifacts. |
| same_likelihood_set_comparison_available | False | False | Production posterior excludes TT_lite and does not constitute a full native/DEU model comparison on its own. |
| model_superiority_claims_allowed | False | False | Model-superiority claims remain blocked by this extension. |

## Claim status

- Scoped internal posterior claims: allowed with caveats.
- Final publication claims: blocked.
- Model-superiority claims: blocked.
- TT_lite-in-production-posterior claims: blocked.
