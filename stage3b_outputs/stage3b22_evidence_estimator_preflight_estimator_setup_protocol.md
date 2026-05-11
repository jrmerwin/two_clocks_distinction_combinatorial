# Stage 3B-22 evidence/model-selection estimator setup protocol

Generated UTC: `2026-05-09T04:14:34+00:00`

This stage prepares matched DEU/native evidence-model-selection inputs only. It does not run an estimator and does not compute evidence.

## Current claim state

- Scoped DEU posterior and descriptive DEU/native posterior comparison remain allowed with caveats.
- Model-superiority, Bayes-factor/evidence, TT_lite-in-posterior, and final publication-style claims remain blocked.

## Required before evidence claims

1. Execute a matched estimator on both DEU and native/baseline inputs.
2. Report estimator uncertainty and numerical stability.
3. Verify shared priors and full-objective likelihood matching remain unchanged.
4. Keep TT_lite diagnostic-only unless a separate matched TT_lite-inclusive sampler is booked.
5. Book a separate evidence/result gate before any model-superiority wording.

## Decision

Decision type: `EVIDENCE_ESTIMATOR_PREFLIGHT_PASS_EXECUTION_REQUIRED`

Recommendation: Book Stage 3B-22. Next run a matched evidence-estimator execution checkpoint; model-superiority and Bayes-factor claims remain blocked until that execution and result gate pass.

Next stage: `Stage 3B-23 matched evidence-estimator execution checkpoint`
