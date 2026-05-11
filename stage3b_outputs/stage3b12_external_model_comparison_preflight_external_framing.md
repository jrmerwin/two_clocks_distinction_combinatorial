# Stage 3B-12 external/model-comparison framing

Generated UTC: `2026-05-08T23:21:57+00:00`

This is a preflight for external wording. It does not launch MCMC and does not unlock final publication-style claims.

## Current allowed scope

The current result can be framed as a caveated internal posterior summary for the DEU full-objective production sampler, with readiness and robustness checks booked.

## Posterior parameter recap

| Parameter | Mean | q16 | q50 | q84 | Working lock |
|---|---:|---:|---:|---:|---:|
| beta | 0.02949121724807528 | 0.028849905 | 0.029503285 | 0.030128599 | 0.03 |
| p_vis | 1.0474182267750214 | 1.0459375 | 1.0473475 | 1.048932 | 1.0475 |
| omega_b | 0.021980020954662106 | 0.021927323 | 0.021972856 | 0.0220347 | 0.022 |
| n_s | 0.9815232201591104 | 0.98086835 | 0.9815207 | 0.98217567 | 0.981875 |
| A_planck | 1.0250557243798117 | 1.0242044 | 1.0250715 | 1.0259026 | 1.025 |

## Claim matrix summary

### Allowed or required statements

- **internal_caveated_posterior_summary**: A first internal posterior summary for the DEU full-objective production sampler may be reported with caveats. Status: `allowed_with_caveats`. Caveat: Use Stage 3B-10 caveats; not a final publication claim.
- **tt_lite_monitoring_context**: TT_lite can be discussed as diagnostic monitoring context only. Status: `allowed_with_caveats`. Caveat: Do not treat TT_lite diagnostic checks as production likelihood evidence.
- **tri_anchor_context_required**: Tri-anchor split context must remain attached to posterior statements. Status: `required`. Caveat: High-l, lowl+TTTEEE, and full-objective anchors remain recorded; production posterior uses the full-objective working lock.
- **baseline_native_context**: Native/baseline comparisons can be described as fixed diagnostic context. Status: `allowed_as_context_only`. Caveat: Do not describe fixed diagnostic gaps as a posterior model comparison or Bayes factor.
- **external_abstract_style_summary**: A concise external-facing summary may state that the internal DEU posterior workflow passed readiness and robustness gates. Status: `allowed_with_caveats`. Caveat: Phrase as workflow/readiness result, not final cosmological evidence or model superiority.

### Blocked statements

- **final_publication_style_claim**: This is a final external/publication-level cosmological result. Reason: Final publication-style claims remain gated until a later final-claim lock explicitly allows them.
- **model_superiority_or_bayes_factor**: DEU is preferred over native/LambdaCDM by model comparison evidence. Reason: No explicit sampled model-comparison/Bayes-factor stage has been booked.
- **tt_lite_included_in_production_likelihood**: TT_lite was included in the production posterior likelihood. Reason: TT_lite remains diagnostic-only in the current production posterior.

## TT_lite status

`diagnostic_only_not_sampled_likelihood`: TT_lite was monitored as a diagnostic context but was excluded from the production sampler likelihood.

## Final-claim preflight decision

Decision type: `EXTERNAL_MODEL_COMPARISON_PREFLIGHT_PASS_FINAL_CLAIMS_STILL_GATED`

Recommendation: Book Stage 3B-12. Use only the scoped/caveated posterior wording; run the next claim-lock or explicit model-comparison stage before stronger final claims.

Next-stage hint: `Stage 3B-13 scoped final-claim lock or explicit model-comparison extension`
