# Stage 3B-22 evidence/model-selection estimator preflight acceptance

Generated UTC: `2026-05-09T04:14:34+00:00`

This stage prepares matched evidence/model-selection inputs only. It does not launch MCMC or compute evidence.

## Acceptance

| Check | Status |
|---|---:|
| Stage 3B-21 design pass | **PASS** |
| Stage 3B-20 final scoped report pass | **PASS** |
| Stage 3B-19 matched comparison pass | **PASS** |
| Stage 3B-18 native readiness pass | **PASS** |
| Stage 3B-9 DEU readiness pass | **PASS** |
| DEU sampler YAML loaded | **PASS** |
| native sampler YAML loaded | **PASS** |
| DEU chain inputs found | **PASS** |
| native chain inputs found | **PASS** |
| DEU expected params present | **PASS** |
| native expected params present | **PASS** |
| shared prior match | **PASS** |
| matched likelihoods and TT_lite scope | **PASS** |
| evidence/Bayes factor computed by this stage | **NO** |
| model-superiority claims allowed | **NO** |
| final publication claims allowed | **NO** |
| hard guard pass | **PASS** |

Diagnostic outcome: `EVIDENCE_ESTIMATOR_PREFLIGHT_PASS_EXECUTION_REQUIRED`

## Preflight decision

Decision type: `EVIDENCE_ESTIMATOR_PREFLIGHT_PASS_EXECUTION_REQUIRED`

Recommendation: Book Stage 3B-22. Next run a matched evidence-estimator execution checkpoint; model-superiority and Bayes-factor claims remain blocked until that execution and result gate pass.

Next-stage hint: `Stage 3B-23 matched evidence-estimator execution checkpoint`

## Outputs

- `json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight.json`
- `acceptance_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_acceptance.md`
- `protocol_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_estimator_setup_protocol.md`
- `execution_plan_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_estimator_execution_plan.md`
- `design_matrix_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_estimator_design_matrix.csv`
- `deu_input_manifest`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_deu_evidence_input_manifest.json`
- `native_input_manifest`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_native_evidence_input_manifest.json`
- `chain_input_audit_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_chain_input_audit.csv`
- `prior_matching_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_prior_matching_audit.csv`
- `likelihood_matching_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_likelihood_matching_audit.csv`
- `estimator_configs_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_candidate_estimator_configs.json`
- `blocked_claims_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_blocked_claims.csv`
- `allowed_current_claims_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_allowed_current_claims.csv`
- `tt_lite_scope_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_tt_lite_scope.md`
- `tri_anchor_context_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_tri_anchor_context.csv`
- `preflight_manifest`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_preflight_manifest.json`

## Booking decision

PASS: bookable as the evidence/model-selection estimator preflight, provided git status is clean except for these artifacts.
This stage does not compute evidence and does not permit model-superiority or Bayes-factor claims.

```bash
git add deu_validation/stage3b_22_evidence_estimator_preflight.py \
        deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight.json \
        deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_acceptance.md \
        deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_estimator_setup_protocol.md \
        deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_estimator_execution_plan.md \
        deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_estimator_design_matrix.csv \
        deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_deu_evidence_input_manifest.json \
        deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_native_evidence_input_manifest.json \
        deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_chain_input_audit.csv \
        deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_prior_matching_audit.csv \
        deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_likelihood_matching_audit.csv \
        deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_candidate_estimator_configs.json \
        deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_blocked_claims.csv \
        deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_allowed_current_claims.csv \
        deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_tt_lite_scope.md \
        deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_tri_anchor_context.csv \
        deu_validation/stage3b_outputs/stage3b22_evidence_estimator_preflight_preflight_manifest.json
git commit -m "Stage 3B-22 evidence estimator preflight"
git tag deu-stage3b22-evidence-estimator-preflight-v0
```
