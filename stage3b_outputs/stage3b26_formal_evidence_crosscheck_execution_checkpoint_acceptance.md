# Stage 3B-26 formal evidence-estimator cross-check execution checkpoint

Generated UTC: `2026-05-09T05:21:38+00:00`

This stage executes formal/cross-check estimator diagnostics over matched DEU/native inputs. It does not launch MCMC and does not permit Bayes-factor/model-superiority/final publication claims.

## Acceptance

| Check | Status |
|---|---:|
| Stage 3B-25 preflight pass | **PASS** |
| Stage 3B-24 proxy-only gate pass | **PASS** |
| Stage 3B-23 proxy execution pass | **PASS** |
| DEU/native formal input manifests loaded | **PASS** |
| DEU/native chains found | **PASS** |
| DEU/native chain values finite | **PASS** |
| formal estimator results finite | **PASS** |
| formal consistency gate pass | **PASS** |
| prior-volume sensitivity recorded | **PASS** |
| proxy/formal cross-check recorded | **PASS** |
| tri-anchor context retained | **PASS** |
| formal evidence cross-check launched by this stage | **PASS** |
| MCMC launched by this stage | **NO** |
| Bayes-factor/evidence claims allowed | **NO** |
| model superiority claims allowed | **NO** |
| final publication claims allowed | **NO** |
| hard guard pass | **PASS** |

Diagnostic outcome: `FORMAL_EVIDENCE_CROSSCHECK_EXECUTION_CHECKPOINT_PASS_RESULT_GATE_REQUIRED`

## Execution decision

Decision type: `FORMAL_EVIDENCE_CROSSCHECK_EXECUTION_CHECKPOINT_PASS_RESULT_GATE_REQUIRED`

Recommendation: Book Stage 3B-26. Next run a formal evidence result gate/sensitivity audit before any formal Bayes-factor or model-superiority wording.

Next-stage hint: `Stage 3B-27 formal evidence result gate and sensitivity audit`

## Representative formal cross-check values

```json
{
  "claim_status": "formal_crosscheck_executed_result_gate_required",
  "deu_log_evidence_formal_crosscheck": -576.0487181192134,
  "log_bayes_factor_formal_crosscheck_deu_minus_native": 158.76404705020616,
  "native_log_evidence_formal_crosscheck": -734.8127651694195,
  "stage3b24_log_bayes_factor_proxy_deu_minus_native": 158.76404705020616
}
```

## Outputs

- `json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint.json`
- `acceptance_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_acceptance.md`
- `formal_estimator_results_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_formal_estimator_results.json`
- `formal_estimator_results_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_formal_estimator_results.csv`
- `per_chain_formal_estimator_results_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_per_chain_formal_estimator_results.csv`
- `formal_estimator_consistency_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_formal_estimator_consistency.csv`
- `prior_volume_sensitivity_results_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_prior_volume_sensitivity_results.csv`
- `proxy_formal_crosscheck_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_proxy_formal_crosscheck.csv`
- `formal_evidence_claim_scope_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_formal_evidence_claim_scope.md`
- `blocked_claims_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_blocked_claims.csv`
- `allowed_current_claims_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_allowed_current_claims.csv`
- `tt_lite_scope_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_tt_lite_scope.md`
- `tri_anchor_context_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_tri_anchor_context.csv`
- `execution_manifest`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_execution_manifest.json`

## Booking decision

PASS: bookable as the formal evidence-estimator cross-check execution checkpoint, provided git status is clean except for these artifacts.
The next stage must gate/sensitivity-audit these results before formal Bayes-factor or model-superiority language is allowed.

```bash
git add deu_validation/stage3b_26_formal_evidence_crosscheck_execution_checkpoint.py \
        deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint.json \
        deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_acceptance.md \
        deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_formal_estimator_results.json \
        deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_formal_estimator_results.csv \
        deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_per_chain_formal_estimator_results.csv \
        deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_formal_estimator_consistency.csv \
        deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_prior_volume_sensitivity_results.csv \
        deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_proxy_formal_crosscheck.csv \
        deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_formal_evidence_claim_scope.md \
        deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_blocked_claims.csv \
        deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_allowed_current_claims.csv \
        deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_tt_lite_scope.md \
        deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_tri_anchor_context.csv \
        deu_validation/stage3b_outputs/stage3b26_formal_evidence_crosscheck_execution_checkpoint_execution_manifest.json
git commit -m "Stage 3B-26 formal evidence crosscheck execution"
git tag deu-stage3b26-formal-evidence-crosscheck-execution-v0
```
