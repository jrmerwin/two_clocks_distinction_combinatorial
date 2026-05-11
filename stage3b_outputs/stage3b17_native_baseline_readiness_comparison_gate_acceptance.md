# Stage 3B-17 native/baseline readiness and matched comparison gate

Generated UTC: `2026-05-09T02:26:18+00:00`

This stage reads the Stage 3B-16 native/baseline checkpoint chain and records native-side readiness diagnostics.
It does not launch MCMC and does not permit model-superiority or final publication-style claims.

## Acceptance

| Check | Status |
|---|---:|
| Stage 3B-16 reference loaded | **PASS** |
| Stage 3B-16 hard guard pass | **PASS** |
| Stage 3B-16 checkpoint pass | **PASS** |
| Stage 3B-16 superiority still gated | **PASS** |
| Stage 3B-15 preflight pass | **PASS** |
| native execution YAML loaded | **PASS** |
| native config has expected sampled params | **PASS** |
| native config has no DEU keys | **PASS** |
| DEU shape params absent from native sampler | **PASS** |
| native full-objective likelihoods present | **PASS** |
| native TT_lite excluded | **PASS** |
| MCMC launched by this stage | **NO** |
| native chain files found | **PASS** |
| native chain has enough rows for assessment | **PASS** |
| native chain has expected sampled columns | **PASS** |
| native chain values finite | **PASS** |
| native sampled params within prior bounds | **PASS** |
| native sampled-parameter motion threshold met | **PASS** |
| native segment split diagnostics recorded | **PASS** |
| native tail diagnostics recorded | **PASS** |
| native autocorr/ESS diagnostics recorded | **PASS** |
| native reference eval success | **PASS** |
| native reference matches Stage 3B-15 sampler ref | **PASS** |
| native reference matches Stage 3B-16 checkpoint | **PASS** |
| tri-anchor context retained | **PASS** |
| native readiness gate pass | **FAIL** |
| model superiority claims allowed | **NO** |
| final publication claims allowed | **NO** |
| hard guard pass | **PASS** |

Diagnostic outcome: `NATIVE_BASELINE_READINESS_RECORDED_MORE_CHAINS_NEEDED`

## Readiness decision

Decision type: `NATIVE_BASELINE_READINESS_RECORDED_MORE_CHAINS_NEEDED`

Recommendation: Book Stage 3B-17 as a readiness diagnostic, but do not make model-superiority claims. Run an additional native/baseline chain stage.

Next-stage hint: `Stage 3B-18 additional native/baseline chains for readiness gate`

## Summary

```json
{
  "min_chain_files_for_readiness": 2,
  "native_ess_gate_pass": true,
  "native_motion_count": 3,
  "native_n_chain_files": 1,
  "native_output_prefix": "/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b16_native_baseline_run",
  "native_readiness_gate_pass": false,
  "native_segment_gate_pass": true,
  "native_tail_gate_pass": true,
  "native_total_chain_rows": 2000,
  "posterior_evidence_status": "not_allowed_native_single_chain_or_insufficient_chain_files"
}
```

## Outputs

- `json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate.json`
- `acceptance_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_acceptance.md`
- `native_chain_audit_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_chain_audit.json`
- `native_chain_columns_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_chain_columns.csv`
- `native_sample_stats_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_sample_stats.json`
- `native_sample_stats_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_sample_stats.csv`
- `native_segment_split_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_segment_split_diagnostics.json`
- `native_segment_split_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_segment_split_diagnostics.csv`
- `native_tail_diagnostics_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_tail_diagnostics.json`
- `native_tail_diagnostics_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_tail_diagnostics.csv`
- `native_autocorr_ess_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_autocorr_ess.json`
- `native_autocorr_ess_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_autocorr_ess.csv`
- `native_reference_eval`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_reference_eval.json`
- `native_reference_comparison_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_reference_comparison.csv`
- `native_config_audit`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_config_audit.json`
- `native_deu_context_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_deu_context.csv`
- `matched_comparison_scope_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_matched_comparison_scope.md`
- `blocked_claims_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_blocked_claims.csv`
- `tri_anchor_context_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_tri_anchor_context.csv`
- `readiness_manifest`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_readiness_manifest.json`

## Booking decision

PASS: bookable as the native/baseline readiness diagnostic, provided git status is clean except for these artifacts.
If the readiness gate did not pass, model-superiority claims remain blocked and the next stage should add native/baseline chain files or repair diagnostics.

```bash
git add deu_validation/stage3b_17_native_baseline_readiness_comparison_gate.py \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate.json \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_acceptance.md \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_chain_audit.json \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_chain_columns.csv \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_sample_stats.json \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_sample_stats.csv \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_segment_split_diagnostics.json \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_segment_split_diagnostics.csv \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_tail_diagnostics.json \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_tail_diagnostics.csv \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_autocorr_ess.json \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_autocorr_ess.csv \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_reference_eval.json \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_reference_comparison.csv \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_config_audit.json \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_native_deu_context.csv \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_matched_comparison_scope.md \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_blocked_claims.csv \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_tri_anchor_context.csv \
        deu_validation/stage3b_outputs/stage3b17_native_baseline_readiness_comparison_gate_readiness_manifest.json
git commit -m "Stage 3B-17 native baseline readiness comparison gate"
git tag deu-stage3b17-native-baseline-readiness-comparison-gate-v0
```
