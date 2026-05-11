# Stage 3B-29 external publication-claim preflight

Generated UTC: `2026-05-09T06:36:44+00:00`

This stage does not launch MCMC and does not compute new evidence.
It converts the Stage 3B-28 internal formal-evidence claim lock into a publication-claim preflight.

## Decision

Decision type: `EXTERNAL_PUBLICATION_CLAIM_PREFLIGHT_PASS_INDEPENDENT_VALIDATION_REQUIRED`

Recommendation: Book Stage 3B-29. Internal formal-evidence language remains allowed with caveats; external/publication, model-superiority, and final claims require independent validation.

Next-stage hint: `Stage 3B-30 independent evidence validation preflight or execution design`

## Evidence values under the current scoped lineage

- DEU formal cross-check log-evidence-style value: `-576.0487181192134`
- Native formal cross-check log-evidence-style value: `-734.8127651694195`
- Formal cross-check log-BF-style value, DEU minus native: `158.76404705020616`

These values are locked for internal use with caveats only.

## Allowed current statements

- **internal_project_record**: The Stage 3B formal cross-check estimator recorded matched DEU and native log-evidence-style values under the scoped full-objective likelihood configuration. Caveat: Use as an internal formal cross-check estimator result, not as a final publication-grade evidence claim.
- **internal_project_record**: The formal cross-check log-BF-style value is positive for DEU relative to native under the matched scoped estimator lineage. Caveat: Do not phrase this as model superiority or decisive external evidence.
- **internal_project_record**: The DEU formal cross-check log-evidence-style value was recorded. Caveat: The estimator lineage and prior-volume assumptions must accompany the value.
- **internal_project_record**: The native formal cross-check log-evidence-style value was recorded. Caveat: The native baseline must be described as matched to the scoped full-objective likelihood and excluded TT_lite.
- **external_preprint_draft_only_if_caveated**: A formal cross-check evidence estimator has been run as part of an internal validation workflow. Caveat: External/publication-grade claims require independent validation before model-superiority language.

## Blocked publication claims

- DEU is proven superior to the native/baseline model. Required to unblock: Independent evidence estimator validation, prior-volume sensitivity, and explicit publication claim lock.
- The formal cross-check log-BF value is a final publication-grade Bayes factor. Required to unblock: Stage 3B-30+ independent validation using a distinct estimator family or matched external evidence protocol.
- TT_lite was included in the production posterior or formal evidence comparison. Required to unblock: A separately booked TT_lite-included sampler/evidence branch.
- The DEU posterior/evidence results are final cosmological publication results. Required to unblock: External robustness, independent reruns, final claim review, and publication-specific validation.
- The evidence result is insensitive to prior-volume choices in a publication-grade sense. Required to unblock: Formal prior-volume sensitivity campaign with pre-registered comparison rules.

## Independent validation requirements

- **Independent evidence estimator family**: Run a distinct estimator family or externally audited formal evidence workflow, not just the current chain-local formal cross-check.
- **Prior-volume sensitivity campaign**: Predefine matched prior-volume alternatives for shared and DEU-only dimensions and report sensitivity of log-BF-style values.
- **Matched likelihood-scope declaration**: Keep full-objective likelihood matching explicit and keep TT_lite exclusion visible unless a separate TT_lite-included branch is booked.
- **Native/baseline reproducibility check**: Confirm native sampler/evidence inputs reproduce the Stage 3B-15/16/18 lineage before independent evidence execution.
- **DEU reproducibility check**: Confirm DEU sampler/evidence inputs reproduce the Stage 3B-9/10/11/27/28 lineage before independent evidence execution.
- **Final claim-lock review**: Write a final claim-lock stage that distinguishes internal evidence language from any external/publication wording.
