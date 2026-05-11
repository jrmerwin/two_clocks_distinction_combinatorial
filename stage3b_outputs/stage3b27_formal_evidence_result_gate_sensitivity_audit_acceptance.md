# Stage 3B-27 formal evidence result gate and sensitivity audit acceptance

Generated UTC: `2026-05-09T05:44:47+00:00`

This stage audits the Stage 3B-26 formal evidence cross-check result. It does not launch MCMC or run a new estimator.

## Acceptance

| Check | Status |
|---|---:|
| Stage 3B-26 reference loaded | **PASS** |
| Stage 3B-26 hard guard pass | **PASS** |
| Stage 3B-26 execution checkpoint pass | **PASS** |
| Stage 3B-26 result gate required | **PASS** |
| Stage 3B-25 preflight pass | **PASS** |
| Stage 3B-24 proxy gate pass | **PASS** |
| formal cross-check gate pass | **PASS** |
| formal evidence values recorded | **PASS** |
| prior-volume sensitivity recorded | **PASS** |
| sensitivity gate pass | **PASS** |
| formal estimator consistency recorded | **PASS** |
| formal estimator consistency gate pass | **PASS** |
| proxy/formal agreement recorded | **PASS** |
| proxy/formal agreement gate pass | **PASS** |
| formal evidence result gate pass | **PASS** |
| formal evidence language allowed with caveats | **PASS** |
| Bayes-factor/evidence claims allowed with internal caveats | **PASS** |
| model superiority claims allowed | **NO** |
| final publication claims allowed | **NO** |
| TT_lite posterior/evidence claims allowed | **NO** |
| new evidence computed by this stage | **NO** |
| MCMC launched by this stage | **NO** |
| hard guard pass | **PASS** |

Diagnostic outcome: `FORMAL_EVIDENCE_RESULT_GATE_PASS_CAVEATED_EVIDENCE_ALLOWED_SUPERIORITY_STILL_GATED`

## Gate decision

Decision type: `FORMAL_EVIDENCE_RESULT_GATE_PASS_CAVEATED_EVIDENCE_ALLOWED_SUPERIORITY_STILL_GATED`

Recommendation: Book Stage 3B-27. Formal cross-check evidence/BF language is allowed only with internal caveats; model-superiority and final publication claims remain gated.

Next-stage hint: `Stage 3B-28 formal evidence claim lock and final scoped report addendum`

## Key values

```json
{
  "deu_log_evidence_formal_crosscheck": -576.0487181192134,
  "final_publication_claims_allowed": false,
  "formal_evidence_result_gate_pass": true,
  "log_bayes_factor_formal_crosscheck_deu_minus_native": 158.76404705020616,
  "model_superiority_claims_allowed": false,
  "native_log_evidence_formal_crosscheck": -734.8127651694195
}
```

## Outputs

- `json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit.json`
- `acceptance_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_acceptance.md`
- `result_gate_report_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_result_gate_report.md`
- `formal_evidence_summary_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_formal_evidence_summary.csv`
- `formal_sensitivity_audit_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_formal_sensitivity_audit.csv`
- `formal_estimator_consistency_audit_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_formal_estimator_consistency_audit.csv`
- `proxy_formal_agreement_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_proxy_formal_agreement.csv`
- `claim_matrix_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_claim_matrix.csv`
- `allowed_formal_evidence_statements_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_allowed_formal_evidence_statements.csv`
- `blocked_claims_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_blocked_claims.csv`
- `required_next_steps_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_required_next_steps.csv`
- `estimator_status_context_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_estimator_status_context.csv`
- `tt_lite_scope_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_tt_lite_scope.md`
- `tri_anchor_context_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_tri_anchor_context.csv`
- `gate_manifest`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_gate_manifest.json`

## Booking decision

PASS: bookable as the formal evidence result gate/sensitivity audit, provided git status is clean except for these artifacts.
Formal evidence/BF language is allowed only as a scoped internal cross-check result with caveats; model-superiority and final-publication claims remain gated.

```bash
git add deu_validation/stage3b_27_formal_evidence_result_gate_sensitivity_audit.py \
        deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit.json \
        deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_acceptance.md \
        deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_result_gate_report.md \
        deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_formal_evidence_summary.csv \
        deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_formal_sensitivity_audit.csv \
        deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_formal_estimator_consistency_audit.csv \
        deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_proxy_formal_agreement.csv \
        deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_claim_matrix.csv \
        deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_allowed_formal_evidence_statements.csv \
        deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_blocked_claims.csv \
        deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_required_next_steps.csv \
        deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_estimator_status_context.csv \
        deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_tt_lite_scope.md \
        deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_tri_anchor_context.csv \
        deu_validation/stage3b_outputs/stage3b27_formal_evidence_result_gate_sensitivity_audit_gate_manifest.json
git commit -m "Stage 3B-27 formal evidence result gate"
git tag deu-stage3b27-formal-evidence-result-gate-v0
```
