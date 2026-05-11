# Stage 3B-18 additional native/baseline chains readiness

Generated UTC: `2026-05-09T03:00:28+00:00`

This stage launches additional native/baseline chain files and reruns native readiness diagnostics.
Model-superiority and final publication-style claims remain gated.

## Acceptance

| Check | Status |
|---|---:|
| Stage 3B-17 reference loaded | **PASS** |
| Stage 3B-17 hard guard pass | **PASS** |
| Stage 3B-17 requested more native chains | **PASS** |
| Stage 3B-17 native readiness false | **PASS** |
| Stage 3B-16 checkpoint pass | **PASS** |
| Stage 3B-15 preflight pass | **PASS** |
| native execution YAML loaded | **PASS** |
| additional native sampler YAML written | **PASS** |
| additional native MCMC launched | **PASS** |
| all additional native sampler runs success | **PASS** |
| combined native chain files found | **PASS** |
| combined native chain file count meets readiness minimum | **PASS** |
| combined native chain has enough rows | **PASS** |
| combined native chain has expected columns | **PASS** |
| combined native chain values finite | **PASS** |
| native sampled params within prior bounds | **PASS** |
| native sampled-parameter motion threshold met | **PASS** |
| native segment diagnostics recorded | **PASS** |
| native tail diagnostics recorded | **PASS** |
| native autocorr/ESS diagnostics recorded | **PASS** |
| native reference eval success | **PASS** |
| native reference matches Stage 3B-15 sampler ref | **PASS** |
| native reference matches Stage 3B-16 checkpoint | **PASS** |
| native config has no DEU keys | **PASS** |
| DEU shape params absent from native sampler | **PASS** |
| native TT_lite excluded | **PASS** |
| tri-anchor context retained | **PASS** |
| native readiness gate pass | **PASS** |
| model superiority claims allowed | **NO** |
| final publication claims allowed | **NO** |
| hard guard pass | **PASS** |

Diagnostic outcome: `ADDITIONAL_NATIVE_BASELINE_CHAINS_READINESS_GATE_PASS_COMPARISON_READY_SUPERIORITY_STILL_GATED`

## Readiness decision

Decision type: `ADDITIONAL_NATIVE_BASELINE_CHAINS_READINESS_GATE_PASS_COMPARISON_READY_SUPERIORITY_STILL_GATED`

Recommendation: Book Stage 3B-18. Next write a matched DEU/native comparison summary and claim-lock preflight; model-superiority claims remain gated until that stage.

Next-stage hint: `Stage 3B-19 matched DEU/native comparison summary and claim-lock preflight`

## Summary

```json
{
  "additional_native_chain_prefixes": [
    "/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b16_native_baseline_run_additional_chain01"
  ],
  "base_native_output_prefix": "/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b16_native_baseline_run",
  "native_n_chain_files": 2,
  "native_readiness_gate_pass": true,
  "native_total_chain_rows": 4000,
  "posterior_evidence_status": "native_readiness_passed_comparison_ready_superiority_still_gated"
}
```

## Outputs

- `json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness.json`
- `acceptance_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_acceptance.md`
- `additional_sampler_yaml`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_additional_sampler.yaml`
- `sampler_runs_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_sampler_runs.json`
- `native_chain_audit_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_chain_audit.json`
- `native_chain_columns_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_chain_columns.csv`
- `native_sample_stats_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_sample_stats.json`
- `native_sample_stats_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_sample_stats.csv`
- `native_segment_split_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_segment_split_diagnostics.json`
- `native_segment_split_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_segment_split_diagnostics.csv`
- `native_tail_diagnostics_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_tail_diagnostics.json`
- `native_tail_diagnostics_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_tail_diagnostics.csv`
- `native_autocorr_ess_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_autocorr_ess.json`
- `native_autocorr_ess_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_autocorr_ess.csv`
- `native_reference_eval`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_reference_eval.json`
- `native_reference_comparison_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_reference_comparison.csv`
- `native_config_audit`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_config_audit.json`
- `native_deu_context_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_deu_context.csv`
- `matched_comparison_scope_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_matched_comparison_scope.md`
- `blocked_claims_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_blocked_claims.csv`
- `tri_anchor_context_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_tri_anchor_context.csv`
- `readiness_manifest`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_readiness_manifest.json`
- `base_native_output_prefix`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b16_native_baseline_run`
- `additional_native_chain_prefixes`: `['/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b16_native_baseline_run_additional_chain01']`

## Booking decision

PASS: bookable as the additional native/baseline readiness stage, provided git status is clean except for these artifacts.
If native readiness passed, the next stage may write a matched DEU/native comparison summary and claim-lock preflight; model-superiority claims remain blocked until then.

```bash
git add deu_validation/stage3b_18_additional_native_baseline_chains_readiness.py \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness.json \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_acceptance.md \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_additional_sampler.yaml \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_sampler_runs.json \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_chain_audit.json \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_chain_columns.csv \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_sample_stats.json \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_sample_stats.csv \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_segment_split_diagnostics.json \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_segment_split_diagnostics.csv \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_tail_diagnostics.json \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_tail_diagnostics.csv \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_autocorr_ess.json \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_autocorr_ess.csv \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_reference_eval.json \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_reference_comparison.csv \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_config_audit.json \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_native_deu_context.csv \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_matched_comparison_scope.md \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_blocked_claims.csv \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_tri_anchor_context.csv \
        deu_validation/stage3b_outputs/stage3b18_additional_native_baseline_chains_readiness_readiness_manifest.json \
        deu_validation/stage3b_outputs/chains/stage3b16_native_baseline_run_additional_chain*
git commit -m "Stage 3B-18 additional native baseline chains readiness"
git tag deu-stage3b18-additional-native-baseline-chains-readiness-v0
```
