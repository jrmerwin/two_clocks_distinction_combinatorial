# Author-led preprint manuscript draft: DEU CMB validation pipeline

Generated UTC: `2026-05-09T17:35:03+00:00`

## Status and scope

This draft is an author-led preprint / technical report package. It is not a peer-reviewed manuscript and does not claim independent external review.
The permitted scope is a caveated posterior summary, a descriptive DEU/native comparison, and internal independent-validation evidence-estimator language with caveats.
Model-superiority, TT_lite-in-posterior/evidence, and final publication-style claims remain blocked.

## DEU posterior summary

| Parameter | Mean | SD | q16 | q50 | q84 | Working lock |
|---|---:|---:|---:|---:|---:|---:|
| beta | 0.029491217 | 0.00055247252 | 0.028849905 | 0.029503285 | 0.030128599 | 0.03 |
| p_vis | 1.0474182 | 0.0013180231 | 1.0459375 | 1.0473475 | 1.048932 | 1.0475 |
| omega_b | 0.021980021 | 4.9536282e-05 | 0.021927323 | 0.021972856 | 0.0220347 | 0.022 |
| n_s | 0.98152322 | 0.00056806878 | 0.98086835 | 0.9815207 | 0.98217567 | 0.981875 |
| A_planck | 1.0250557 | 0.00084646128 | 1.0242044 | 1.0250715 | 1.0259026 | 1.025 |

## Matched DEU/native descriptive comparison

These rows are descriptive posterior comparisons only and are not model evidence or superiority claims.

| Parameter | DEU mean | Native mean | DEU-native mean | Shift / quadrature SD | Scope |
|---|---:|---:|---:|---:|---|
| omega_b | 0.021980021 | 0.021934117 | 4.5904254e-05 | 0.80218681 | descriptive posterior comparison only; not model evidence or superiority |
| n_s | 0.98152322 | 0.98177763 | -0.00025440994 | -0.33162241 | descriptive posterior comparison only; not model evidence or superiority |
| A_planck | 1.0250557 | 1.0200423 | 0.0050134312 | 5.8639125 | descriptive posterior comparison only; not model evidence or superiority |
| beta | 0.029491217 |  |  |  | DEU-only shape parameter; no native analogue |
| p_vis | 1.0474182 |  |  |  | DEU-only shape parameter; no native analogue |

## Internal independent-validation evidence lineage

- DEU independent-validation log evidence: `-542.297479066`
- Native independent-validation log evidence: `-711.303887687`
- Internal independent-validation log-BF-style contrast, DEU minus native: `169.006408621`
- Formal/proxy log-BF lineage: `158.76404705`

These are internal estimator results with caveats. They do not by themselves authorize model-superiority or final publication-style claims.

## Tri-anchor context

The tri-anchor ledger remains part of the monitoring context.

| Anchor | beta | p_vis | omega_b | n_s | A_planck | profile | full-objective loglike |
|---|---:|---:|---:|---:|---:|---:|---:|
| highl_anchor | 0.029 | 1.0475 | 0.02195 | 0.98 | 1.025 | 2 | -603.9366549798966 |
| lowl_plus_anchor | 0.0295 | 1.0475 | 0.02195 | 0.98125 | 1.025 | 2 | -603.8525238512426 |
| full_objective_working_lock | 0.03 | 1.0475 | 0.022 | 0.981875 | 1.025 | 2 | -603.8280689556785 |

## Stage lineage recap

| Stage | Loaded | Hard guard | Decision | Claim status |
|---|---:|---:|---|---|
| Stage 3B0 | True | True | STAGE3B0_LOCK_NOTE_AND_MINIMAL_SAMPLER_SEED_WRITTEN | external_claims_blocked; superiority_blocked; final_claims_blocked |
| Stage 3B9 | True | True | ADDITIONAL_PRODUCTION_CHAINS_READINESS_GATE_PASS | external_claims_blocked; superiority_blocked; final_claims_blocked |
| Stage 3B10 | True | True | FIRST_POSTERIOR_SUMMARY_WITH_TRI_ANCHOR_CAVEATS_WRITTEN | external_claims_blocked; superiority_blocked; final_claims_blocked |
| Stage 3B11 | True | True | POSTERIOR_ROBUSTNESS_COMPARISON_PASS | external_claims_blocked; superiority_blocked; final_claims_blocked |
| Stage 3B18 | True | True | ADDITIONAL_NATIVE_BASELINE_CHAINS_READINESS_GATE_PASS_COMPARISON_READY_SUPERIORITY_STILL_GATED | external_claims_blocked; superiority_blocked; final_claims_blocked |
| Stage 3B19 | True | True | MATCHED_DEU_NATIVE_COMPARISON_SUMMARY_PASS_SUPERIORITY_STILL_GATED | external_claims_blocked; superiority_blocked; final_claims_blocked |
| Stage 3B20 | True | True | FINAL_SCOPED_INTERNAL_REPORT_PASS_SUPERIORITY_STILL_GATED | external_claims_blocked; superiority_blocked; final_claims_blocked |
| Stage 3B32 | True | True | INDEPENDENT_EVIDENCE_VALIDATION_RESULT_GATE_PASS_INTERNAL_VALIDATION_ALLOWED_PUBLICATION_STILL_GATED | internal_evidence_language_allowed_with_caveats; external_claims_blocked; superiority_blocked; final_claims_blocked |
| Stage 3B33 | True | True | EXTERNAL_EVIDENCE_PUBLICATION_CLAIM_LOCK_PASS_INTERNAL_VALIDATION_ALLOWED_PUBLICATION_STILL_GATED | internal_evidence_language_allowed_with_caveats; external_claims_blocked; superiority_blocked; final_claims_blocked |
| Stage 3B34 | True | True | PUBLICATION_GRADE_REPLICATION_PREFLIGHT_PASS_EXTERNAL_REVIEW_REQUIRED | internal_evidence_language_allowed_with_caveats; external_claims_blocked; superiority_blocked; final_claims_blocked |
| Stage 3B35 | True | True | INDEPENDENT_REPLICATION_PACKAGE_FREEZE_DRY_RUN_PASS_EXTERNAL_REVIEW_READY_PUBLICATION_STILL_GATED | internal_evidence_language_allowed_with_caveats; external_claims_blocked; superiority_blocked; final_claims_blocked |
| Stage 3B36 | True | True | EXTERNAL_REVIEWER_HANDOFF_RESULT_GATE_PASS_REVIEW_PENDING_PUBLICATION_STILL_GATED | internal_evidence_language_allowed_with_caveats; external_claims_blocked; superiority_blocked; final_claims_blocked |
| Stage 3B37 | True | True | PREPRINT_RELEASE_SCOPE_LOCK_PASS_PUBLICATION_CLAIMS_STILL_GATED | external_claims_blocked; superiority_blocked; final_claims_blocked |

## Blocked claims

- This work has passed peer review or independent external review. Reason: No reviewer branch result is booked for this path.
- DEU is proven superior to native/baseline cosmology. Reason: Model-superiority claims remain blocked.
- The evidence/Bayes factor is final or publication-grade. Reason: Evidence language remains internal/caveated.
- TT_lite was included in the sampled posterior or evidence likelihood. Reason: TT_lite is diagnostic-only in this lineage.
- This is a final publication-style claim rather than a preprint/technical report result. Reason: Final publication claims remain gated.
