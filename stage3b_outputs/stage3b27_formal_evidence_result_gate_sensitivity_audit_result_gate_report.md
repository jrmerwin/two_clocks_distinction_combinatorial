# Stage 3B-27 formal evidence result gate and sensitivity audit

Generated UTC: `2026-05-09T05:44:47+00:00`

This stage audits the Stage 3B-26 formal evidence cross-check result. It does not launch MCMC and does not run a new estimator.

## Decision

Decision type: `FORMAL_EVIDENCE_RESULT_GATE_PASS_CAVEATED_EVIDENCE_ALLOWED_SUPERIORITY_STILL_GATED`

Recommendation: Book Stage 3B-27. Formal cross-check evidence/BF language is allowed only with internal caveats; model-superiority and final publication claims remain gated.

Next-stage hint: `Stage 3B-28 formal evidence claim lock and final scoped report addendum`

## Formal evidence summary

| Quantity | Value | Scope |
|---|---:|---|
| deu_log_evidence_formal_crosscheck | -576.048718119 | formal cross-check estimator value; scoped internal language only |
| native_log_evidence_formal_crosscheck | -734.812765169 | formal cross-check estimator value; scoped internal language only |
| log_bayes_factor_formal_crosscheck_deu_minus_native | 158.76404705 | may be stated only as a caveated matched formal cross-check result; not final publication evidence |

## Allowed scoped statements

- **formal_crosscheck_value_internal**: The matched formal cross-check estimator recorded log BF(DEU-native) = 158.76404705. Caveat: Not a final publication Bayes factor; model-superiority claims remain blocked.
- **formal_crosscheck_matches_proxy**: The formal cross-check value agrees with the previously booked diagnostic proxy lineage within the configured tolerance. Caveat: Agreement is among this project's estimator artifacts only; it is not external validation.
- **prior_sensitivity_recorded**: Prior-volume sensitivity rows were recorded and passed the Stage 3B-27 gate. Caveat: Sensitivity audit does not replace external model comparison or publication review.
- **posterior_summary_still_allowed**: The caveated DEU posterior summary and matched DEU/native descriptive comparison remain allowed. Caveat: TT_lite remains diagnostic-only and outside the sampled posterior/evidence likelihood.

## Blocked statements

- **model_superiority**: DEU is superior to the native/baseline model. Reason: Requires a separate final claim lock/publication preflight after formal result gating.
- **publication_bayes_factor**: The reported log BF is a final publication-grade Bayes factor. Reason: Stage 3B-27 allows only scoped internal formal cross-check language.
- **tt_lite_in_evidence**: TT_lite was included in the sampled posterior or evidence estimator. Reason: TT_lite was diagnostic-only in this pipeline.
- **external_validation**: The result is externally validated or robust to all estimator choices. Reason: External validation and independent estimator/review remain separate follow-up work.
- **final_publication_claim**: This completes final publication-style claims. Reason: Final publication-style claims remain explicitly gated.
