# Stage 3B-30 independent evidence-validation protocol

Generated UTC: `2026-05-09T13:59:03+00:00`

This stage does not launch MCMC and does not compute new evidence.
It defines the independent validation work required before any external publication, model-superiority, or final-style evidence claim can be made.

## Current formal cross-check value

```json
{
  "deu_log_evidence_formal_crosscheck": -576.0487181192134,
  "log_bayes_factor_formal_crosscheck_deu_minus_native": 158.76404705020616,
  "native_log_evidence_formal_crosscheck": -734.8127651694195
}
```

The value above is already claim-locked only for internal, caveated discussion. It is not yet independently validated for external model-selection language.

## Requirements

- **R1_independent_estimator_family**: At least one evidence estimator must be independent of the chain-local Laplace proxy/formal cross-check lineage.
- **R2_matched_likelihood_scope**: DEU and native sides must use the same full-objective likelihood set; TT_lite remains excluded unless a separate matched TT_lite-inclusive branch is run.
- **R3_prior_volume_sensitivity**: Evidence/BF result must be tested against predeclared prior-volume variants.
- **R4_reproducible_input_manifests**: Input chain files, parameter columns, priors, likelihood scope, and reference values must be frozen in manifests.
- **R5_result_gate**: Independent validation execution must be followed by a separate result gate before any claim language is upgraded.
- **R6_publication_guardrails**: Publication-style language must remain blocked until independent validation and final claim-lock stages are booked.

## Required independent-validation sequence

1. Freeze DEU/native input manifests and likelihood scope.
2. Execute at least one independent evidence estimator family.
3. Record raw estimator diagnostics and uncertainties.
4. Run prior-volume and estimator-family sensitivity audits.
5. Run a separate result gate before changing claim language.
6. Keep TT_lite diagnostic-only unless a separate matched TT_lite-inclusive branch is explicitly run.
