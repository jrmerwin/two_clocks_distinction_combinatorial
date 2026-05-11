# Stage 3B-6 production-run configuration and preflight

Generated UTC: `2026-05-08T17:52:22+00:00`

This stage writes the first production-run Cobaya YAML and preflights it at the guarded working-lock reference point.
It does not launch production MCMC and does not permit posterior interpretation.

## Acceptance

| Check | Status |
|---|---:|
| Stage 3B-5 reference loaded | **PASS** |
| Stage 3B-5 hard guard pass | **PASS** |
| Stage 3B-5 convergence gate pass | **PASS** |
| Stage 3B-5 posterior interpretation false | **PASS** |
| Stage 3B-0 reference loaded | **PASS** |
| Stage 3B-0 hard guard pass | **PASS** |
| Stage 3B-1 reference loaded | **PASS** |
| Stage 3B-1 hard guard pass | **PASS** |
| minimal sampler YAML loaded | **PASS** |
| fixed reference YAML loaded | **PASS** |
| production sampler YAML written | **PASS** |
| production run script written | **PASS** |
| production reference evaluation success | **PASS** |
| production config has expected sampled params | **PASS** |
| production config refs match working lock | **PASS** |
| production config has full-objective likelihoods | **PASS** |
| production config excludes TT_lite | **PASS** |
| production config has MCMC sampler | **PASS** |
| production output prefix matches expected | **PASS** |
| production chain prefix clean | **PASS** |
| production ref matches Stage 3B-0 working lock | **PASS** |
| production ref matches Stage 3B-1 sampler ref | **PASS** |
| tri-anchor monitoring evaluated | **PASS** |
| tri-anchor loglikes match monitoring ledger | **PASS** |
| production MCMC launched by this stage | **NO** |
| posterior interpretation allowed | **NO** |
| posterior conclusions written | **NO** |
| hard guard pass | **PASS** |

Diagnostic outcome: `PRODUCTION_PREFLIGHT_PASS`

## Preflight decision

Decision type: `PRODUCTION_PREFLIGHT_PASS`

Recommendation: Book Stage 3B-6. Next run Stage 3B-7 first production execution/checkpoint. Posterior claims remain gated until a separately booked convergence assessment passes.

Next-stage hint: `Stage 3B-7 first production execution/checkpoint, posterior still gated`

Production output prefix:

`/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b6_first_production_run`

Working lock:

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

- `json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b6_production_preflight.json`
- `acceptance_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b6_production_preflight_acceptance.md`
- `production_sampler_yaml`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b6_production_preflight_production_sampler.yaml`
- `production_run_script`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b6_production_preflight_run_production.sh`
- `production_ref_eval`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b6_production_preflight_production_ref_eval.json`
- `comparison_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b6_production_preflight_comparison.csv`
- `config_audit`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b6_production_preflight_config_audit.json`
- `tri_anchor_eval_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b6_production_preflight_tri_anchor_eval.json`
- `tri_anchor_eval_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b6_production_preflight_tri_anchor_eval.csv`
- `preflight_manifest`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b6_production_preflight_preflight_manifest.json`
- `production_output_prefix`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b6_first_production_run`

## Booking decision

PASS: bookable as the production preflight stage, provided git status is clean except for these artifacts.
This is still not posterior evidence; production MCMC has not been launched by this stage.

```bash
git add deu_validation/stage3b_6_production_preflight.py \
        deu_validation/stage3b_outputs/stage3b6_production_preflight.json \
        deu_validation/stage3b_outputs/stage3b6_production_preflight_acceptance.md \
        deu_validation/stage3b_outputs/stage3b6_production_preflight_production_sampler.yaml \
        deu_validation/stage3b_outputs/stage3b6_production_preflight_run_production.sh \
        deu_validation/stage3b_outputs/stage3b6_production_preflight_production_ref_eval.json \
        deu_validation/stage3b_outputs/stage3b6_production_preflight_comparison.csv \
        deu_validation/stage3b_outputs/stage3b6_production_preflight_config_audit.json \
        deu_validation/stage3b_outputs/stage3b6_production_preflight_tri_anchor_eval.json \
        deu_validation/stage3b_outputs/stage3b6_production_preflight_tri_anchor_eval.csv \
        deu_validation/stage3b_outputs/stage3b6_production_preflight_preflight_manifest.json
git commit -m "Stage 3B-6 production preflight"
git tag deu-stage3b6-production-preflight-v0
```
