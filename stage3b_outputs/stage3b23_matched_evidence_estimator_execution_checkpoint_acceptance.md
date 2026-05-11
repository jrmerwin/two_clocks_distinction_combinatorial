# Stage 3B-23 matched evidence-estimator execution checkpoint

Generated UTC: `2026-05-09T04:28:20+00:00`

This stage executes a matched diagnostic evidence proxy. It does not launch MCMC and it does not unlock Bayes-factor/model-superiority claims.

## Acceptance

| Check | Status |
|---|---:|
| Stage 3B-22 reference loaded | **PASS** |
| Stage 3B-22 hard guard pass | **PASS** |
| Stage 3B-22 preflight pass | **PASS** |
| DEU estimator success | **PASS** |
| native estimator success | **PASS** |
| matched log-BF proxy recorded | **PASS** |
| per-chain estimator results recorded | **PASS** |
| estimator robustness gate pass | **PASS** |
| tri-anchor context retained | **PASS** |
| evidence estimator execution launched by this stage | **PASS** |
| evidence proxy computed by this stage | **PASS** |
| Bayes-factor/evidence claims allowed | **NO** |
| model-superiority claims allowed | **NO** |
| final publication claims allowed | **NO** |
| MCMC launched by this stage | **NO** |
| hard guard pass | **PASS** |

Diagnostic outcome: `MATCHED_EVIDENCE_ESTIMATOR_EXECUTION_CHECKPOINT_PASS_RESULT_GATE_REQUIRED`

## Estimator decision

Decision type: `MATCHED_EVIDENCE_ESTIMATOR_EXECUTION_CHECKPOINT_PASS_RESULT_GATE_REQUIRED`

Recommendation: Book Stage 3B-23. Next run an evidence-result gate/sensitivity stage before any model-superiority or Bayes-factor wording.

Next-stage hint: `Stage 3B-24 evidence result gate and sensitivity audit`

## Proxy result summary

```json
{
  "deu_log_evidence_proxy": -576.0487181192134,
  "estimator_kind": "diagnostic_proxy_not_final_evidence",
  "log_bayes_factor_proxy_deu_minus_native": 158.76404705020616,
  "native_log_evidence_proxy": -734.8127651694195,
  "posterior_evidence_status": "diagnostic_proxy_executed_result_gate_required"
}
```

## Outputs

- `json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint.json`
- `acceptance_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_acceptance.md`
- `estimator_results_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_estimator_results.json`
- `estimator_results_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_estimator_results.csv`
- `per_chain_estimator_results_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_per_chain_estimator_results.csv`
- `estimator_robustness_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_estimator_robustness.csv`
- `logpost_summary_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_logpost_summary.csv`
- `evidence_claim_scope_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_evidence_claim_scope.md`
- `blocked_claims_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_blocked_claims.csv`
- `allowed_current_claims_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_allowed_current_claims.csv`
- `tt_lite_scope_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_tt_lite_scope.md`
- `tri_anchor_context_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_tri_anchor_context.csv`
- `execution_manifest`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_execution_manifest.json`

## Booking decision

PASS: bookable as the matched evidence-estimator execution checkpoint, provided git status is clean except for these artifacts.
The proxy result is not a final evidence/Bayes-factor claim. Run the result gate/sensitivity audit next.

```bash
git add deu_validation/stage3b_23_matched_evidence_estimator_execution_checkpoint.py \
        deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint.json \
        deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_acceptance.md \
        deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_estimator_results.json \
        deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_estimator_results.csv \
        deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_per_chain_estimator_results.csv \
        deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_estimator_robustness.csv \
        deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_logpost_summary.csv \
        deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_evidence_claim_scope.md \
        deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_blocked_claims.csv \
        deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_allowed_current_claims.csv \
        deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_tt_lite_scope.md \
        deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_tri_anchor_context.csv \
        deu_validation/stage3b_outputs/stage3b23_matched_evidence_estimator_execution_checkpoint_execution_manifest.json
git commit -m "Stage 3B-23 matched evidence estimator execution checkpoint"
git tag deu-stage3b23-matched-evidence-estimator-execution-checkpoint-v0
```
