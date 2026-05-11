# Stage 3B-1 fixed-reference and sampler-plumbing dry guard

Generated UTC: `2026-05-08T15:46:31+00:00`

This stage evaluates the fixed-reference YAML and evaluates the minimal sampler seed at its reference point only.
It does not launch MCMC and does not interpret chains as posterior evidence.

## Acceptance

| Check | Status |
|---|---:|
| Stage 3B-0 reference loaded | **PASS** |
| Stage 3B-0 hard guard pass | **PASS** |
| Stage 3B-0 did not launch MCMC | **PASS** |
| fixed-reference YAML loaded | **PASS** |
| minimal sampler YAML loaded | **PASS** |
| fixed-reference evaluation success | **PASS** |
| sampler ref-point evaluation success | **PASS** |
| expected sampled params present | **PASS** |
| full-objective likelihoods present in sampler YAML | **PASS** |
| sampler YAML excludes TT_lite | **PASS** |
| fixed reference matches working-lock loglikes | **PASS** |
| sampler ref matches working-lock loglikes | **PASS** |
| sampler ref matches fixed reference on full objective | **PASS** |
| dry guard manifest written | **PASS** |
| fixed eval JSON written | **PASS** |
| sampler ref eval JSON written | **PASS** |
| comparison CSV written | **PASS** |
| script completed | **PASS** |
| MCMC launched by this stage | **NO** |
| hard guard pass | **PASS** |

Diagnostic outcome: `SAMPLER_PLUMBING_DRY_GUARD_PASS`

## Dry-guard decision

Decision type: `SAMPLER_PLUMBING_DRY_GUARD_PASS`

Recommendation: Book Stage 3B-1, then run a tiny non-interpretive sampler smoke test. Do not interpret chains as posterior evidence yet.

Next-stage hint: `Stage 3B-2 tiny sampler smoke test with tri-anchor monitoring`

Working-lock point:

```json
{
  "A_planck": 1.025,
  "beta": 0.03,
  "deu_lensed_phase_profile": 2,
  "n_s": 0.981875,
  "omega_b": 0.022,
  "p_vis": 1.0475
}
```

## Outputs

- `json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b1_fixed_reference_sampler_plumbing_guard.json`
- `acceptance_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b1_fixed_reference_sampler_plumbing_guard_acceptance.md`
- `fixed_eval_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b1_fixed_reference_sampler_plumbing_guard_fixed_reference_eval.json`
- `sampler_ref_eval_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b1_fixed_reference_sampler_plumbing_guard_sampler_ref_eval.json`
- `comparison_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b1_fixed_reference_sampler_plumbing_guard_comparison.csv`
- `dry_guard_manifest`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b1_fixed_reference_sampler_plumbing_guard_dry_guard_manifest.json`

## Booking decision

PASS: bookable as the Stage 3B sampler-plumbing dry guard, provided git status is clean except for these artifacts.

```bash
git add deu_validation/stage3b_1_fixed_reference_sampler_plumbing_guard.py \
        deu_validation/stage3b_outputs/stage3b1_fixed_reference_sampler_plumbing_guard.json \
        deu_validation/stage3b_outputs/stage3b1_fixed_reference_sampler_plumbing_guard_acceptance.md \
        deu_validation/stage3b_outputs/stage3b1_fixed_reference_sampler_plumbing_guard_fixed_reference_eval.json \
        deu_validation/stage3b_outputs/stage3b1_fixed_reference_sampler_plumbing_guard_sampler_ref_eval.json \
        deu_validation/stage3b_outputs/stage3b1_fixed_reference_sampler_plumbing_guard_comparison.csv \
        deu_validation/stage3b_outputs/stage3b1_fixed_reference_sampler_plumbing_guard_dry_guard_manifest.json
git commit -m "Stage 3B-1 fixed-reference sampler-plumbing dry guard"
git tag deu-stage3b1-fixed-reference-sampler-plumbing-guard-v0
```
