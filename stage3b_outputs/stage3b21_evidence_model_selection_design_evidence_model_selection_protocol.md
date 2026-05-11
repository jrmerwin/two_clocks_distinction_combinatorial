# Stage 3B-21 evidence/model-selection protocol

Generated UTC: `2026-05-09T03:56:55+00:00`

This stage does not launch MCMC or compute evidence. It defines the design required before model-superiority, Bayes-factor/evidence, or final publication-style claims can be considered.

## Recommended design path

1. Freeze a matched likelihood/prior manifest for DEU and native/baseline.
2. Choose an evidence estimator, preferably a matched nested-sampling or otherwise explicit evidence workflow.
3. Run both DEU and native/baseline evidence jobs under the same data/likelihood scope.
4. Repeat or otherwise estimate numerical evidence uncertainty.
5. Run prior-sensitivity checks, especially for DEU-only beta and p_vis.
6. Only then update the claim lock.

## Design matrix

| Design | Status | Purpose | Claim unlocked if passed |
|---|---|---|---|
| matched_nested_sampling_evidence | recommended_primary_path | Compute matched log evidence for DEU and native/baseline under the same likelihood family. | Bayes-factor/evidence language, still caveated by prior dependence |
| matched_native_deu_production_chains_ic | secondary_descriptive_path | Compute descriptive AIC/BIC/DIC/WAIC-like summaries from matched posterior chains if available. | descriptive information-criterion comparison only |
| prior_sensitivity_evidence_grid | required_for_stronger_claims | Assess whether any evidence/comparison result is stable under reasonable prior-width choices. | robustness qualifier for evidence/model-selection statements |
| tt_lite_inclusion_extension | optional_scope_extension | Run an explicit sampled likelihood configuration including TT_lite if TT_lite posterior language is desired. | TT_lite-included posterior claims for that new run only |
| external_data_or_holdout_check | required_for_publication_strength | Check whether posterior/model comparison survives a data split or external dataset. | external robustness language |

## Required evidence artifacts

| Artifact | Required | Description |
|---|---:|---|
| matched_likelihood_manifest | True | Defines identical DEU/native likelihood components and explicitly states TT_lite status. |
| matched_prior_manifest | True | Defines shared native parameters and DEU-only beta/p_vis prior treatment. |
| evidence_estimator_config | True | Specifies nested/evidence estimator, stopping criteria, seeds, and outputs. |
| native_evidence_run | True | Native/baseline evidence or approved comparison run. |
| deu_evidence_run | True | DEU evidence or approved comparison run using matched settings. |
| evidence_reproducibility_or_error_budget | True | Independent repeat or estimator uncertainty sufficient to support any comparison. |
| prior_sensitivity_check | True | Shows comparison is not an artifact of arbitrary prior widths. |
| claim_lock_update | True | Maps evidence outputs to allowed and blocked external claims. |
