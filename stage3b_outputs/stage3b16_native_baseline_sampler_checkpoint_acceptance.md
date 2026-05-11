# Stage 3B-16 matched native/baseline sampler execution checkpoint

Generated UTC: `2026-05-09T01:56:24+00:00`

This stage launches the matched native/baseline sampler prepared by Stage 3B-15 and audits the native checkpoint chain.
It does not allow model-superiority or final publication-style claims.

## Acceptance

| Check | Status |
|---|---:|
| Stage 3B-15 reference loaded | **PASS** |
| Stage 3B-15 hard guard pass | **PASS** |
| Stage 3B-15 preflight pass | **PASS** |
| Stage 3B-15 superiority still gated | **PASS** |
| native sampler YAML loaded | **PASS** |
| native execution YAML written | **PASS** |
| native prefix clean or force-cleaned | **PASS** |
| native sampler has expected native params | **PASS** |
| DEU shape params absent from native sampler | **PASS** |
| native extra args have no DEU keys | **PASS** |
| native full objective likelihoods present | **PASS** |
| native TT_lite excluded | **PASS** |
| native MCMC launched by this stage | **PASS** |
| native sampler run success | **PASS** |
| native chain files found | **PASS** |
| native chain has enough rows | **PASS** |
| native chain has expected sampled columns | **PASS** |
| native chain values finite | **PASS** |
| native sampled params within prior bounds | **PASS** |
| native sampled motion threshold met | **PASS** |
| native reference eval success | **PASS** |
| native reference matches Stage 3B-15 sampler ref | **PASS** |
| tri-anchor context retained | **PASS** |
| model-superiority claims allowed | **NO** |
| final publication claims allowed | **NO** |
| hard guard pass | **PASS** |

Diagnostic outcome: `MATCHED_NATIVE_BASELINE_SAMPLER_CHECKPOINT_PASS_SUPERIORITY_STILL_GATED`

## Checkpoint decision

Decision type: `MATCHED_NATIVE_BASELINE_SAMPLER_CHECKPOINT_PASS_SUPERIORITY_STILL_GATED`

Recommendation: Book Stage 3B-16. Next run a native/baseline readiness and comparison gate before any model-superiority or final publication claim.

Next-stage hint: `Stage 3B-17 native/baseline readiness and matched comparison gate`

## Native checkpoint summary

```json
{
  "model_superiority_claims_allowed": false,
  "native_chain_rows": 2000,
  "native_motion_count": 3,
  "native_n_chain_files": 1,
  "native_reference_matches_stage3b15_sampler_ref": true,
  "posterior_evidence_status": "native_sampler_checkpoint_passed_superiority_still_gated"
}
```

## Outputs

- `json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint.json`
- `acceptance_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_acceptance.md`
- `execution_yaml`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_execution_sampler.yaml`
- `sampler_run_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_sampler_run.json`
- `chain_audit_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_chain_audit.json`
- `chain_columns_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_chain_columns.csv`
- `sample_stats_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_sample_stats.json`
- `sample_stats_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_sample_stats.csv`
- `native_reference_eval`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_native_reference_eval.json`
- `reference_comparison_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_reference_comparison.csv`
- `native_execution_config_audit`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_native_execution_config_audit.json`
- `claim_scope_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_claim_scope.md`
- `tri_anchor_context_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_tri_anchor_context.csv`
- `checkpoint_manifest`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_checkpoint_manifest.json`
- `native_chain_prefix`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b16_native_baseline_run`

## Booking decision

PASS: bookable as the matched native/baseline sampler checkpoint, provided git status is clean except for these artifacts.
Model-superiority and final-publication claims remain blocked.

```bash
git add deu_validation/stage3b_16_native_baseline_sampler_checkpoint.py \
        deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint.json \
        deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_acceptance.md \
        deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_execution_sampler.yaml \
        deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_sampler_run.json \
        deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_chain_audit.json \
        deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_chain_columns.csv \
        deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_sample_stats.json \
        deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_sample_stats.csv \
        deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_native_reference_eval.json \
        deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_reference_comparison.csv \
        deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_native_execution_config_audit.json \
        deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_claim_scope.md \
        deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_tri_anchor_context.csv \
        deu_validation/stage3b_outputs/stage3b16_native_baseline_sampler_checkpoint_checkpoint_manifest.json \
        deu_validation/stage3b_outputs/chains/stage3b16_native_baseline_run*
git commit -m "Stage 3B-16 native baseline sampler checkpoint"
git tag deu-stage3b16-native-baseline-sampler-checkpoint-v0
```
