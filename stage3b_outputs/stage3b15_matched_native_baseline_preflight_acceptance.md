# Stage 3B-15 matched native/baseline comparison preflight

Generated UTC: `2026-05-09T01:10:50+00:00`

This stage prepares and validates native/baseline comparison configs. It does not launch MCMC.

## Acceptance

| Check | Status |
|---|---:|
| Stage 3B-14 reference loaded | **PASS** |
| Stage 3B-14 hard guard pass | **PASS** |
| Stage 3B-14 superiority still gated | **PASS** |
| Stage 3B-13 hard guard pass | **PASS** |
| Stage 3B-11 robustness pass | **PASS** |
| Stage 3B-10 posterior summary written | **PASS** |
| Stage 3B-9 readiness gate pass | **PASS** |
| production YAML loaded | **PASS** |
| native fixed YAML written | **PASS** |
| native sampler YAML written | **PASS** |
| native fixed extra args have no DEU keys | **PASS** |
| native sampler extra args have no DEU keys | **PASS** |
| native sampler has native sampled params | **PASS** |
| DEU shape params absent from native sampler | **PASS** |
| native full-objective likelihoods present | **PASS** |
| native TT_lite excluded | **PASS** |
| native fixed reference eval success | **PASS** |
| native sampler ref eval success | **PASS** |
| native reference deltas recorded | **PASS** |
| tri-anchor context retained | **PASS** |
| MCMC launched by this stage | **NO** |
| native MCMC launched by this stage | **NO** |
| model superiority claims allowed | **NO** |
| final publication claims allowed | **NO** |
| hard guard pass | **PASS** |

Diagnostic outcome: `MATCHED_NATIVE_BASELINE_PREFLIGHT_PASS_SUPERIORITY_STILL_GATED`

## Preflight decision

Decision type: `MATCHED_NATIVE_BASELINE_PREFLIGHT_PASS_SUPERIORITY_STILL_GATED`

Recommendation: Book Stage 3B-15. Next run the matched native/baseline sampler or explicit evidence/comparison stage before model-superiority claims.

Next-stage hint: `Stage 3B-16 matched native/baseline sampler execution checkpoint`

## Outputs

- `json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight.json`
- `acceptance_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_acceptance.md`
- `native_fixed_yaml`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_native_fixed_reference.yaml`
- `native_sampler_yaml`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_native_sampler_seed.yaml`
- `native_fixed_eval_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_native_fixed_reference_eval.json`
- `native_sampler_ref_eval_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_native_sampler_ref_eval.json`
- `config_audit_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_native_config_audit.json`
- `native_deu_comparison_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_native_deu_reference_comparison.csv`
- `claim_scope_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_claim_scope.md`
- `blocked_claims_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_blocked_claims.csv`
- `required_followup_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_required_followup_plan.csv`
- `tt_lite_scope_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_tt_lite_scope.md`
- `tri_anchor_context_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_tri_anchor_context.csv`
- `preflight_manifest`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_preflight_manifest.json`

## Booking decision

PASS: bookable as the matched native/baseline preflight stage, provided git status is clean except for these artifacts.
This does not permit model-superiority claims; it prepares the next matched native/baseline sampler execution.

```bash
git add deu_validation/stage3b_15_matched_native_baseline_preflight.py \
        deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight.json \
        deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_acceptance.md \
        deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_native_fixed_reference.yaml \
        deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_native_sampler_seed.yaml \
        deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_native_fixed_reference_eval.json \
        deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_native_sampler_ref_eval.json \
        deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_native_config_audit.json \
        deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_native_deu_reference_comparison.csv \
        deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_claim_scope.md \
        deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_blocked_claims.csv \
        deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_required_followup_plan.csv \
        deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_tt_lite_scope.md \
        deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_tri_anchor_context.csv \
        deu_validation/stage3b_outputs/stage3b15_matched_native_baseline_preflight_preflight_manifest.json
git commit -m "Stage 3B-15 matched native baseline preflight"
git tag deu-stage3b15-matched-native-baseline-preflight-v0
```
