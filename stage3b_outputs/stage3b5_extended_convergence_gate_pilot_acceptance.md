# Stage 3B-5 extended convergence-gate pilot with tri-anchor monitoring

Generated UTC: `2026-05-08T17:32:08+00:00`

This stage launches a modest multi-chain Cobaya MCMC pilot beyond Stage 3B-4.
It records crude split/tail diagnostics and tri-anchor monitoring, but explicitly does not permit posterior interpretation.

## Acceptance

| Check | Status |
|---|---:|
| Stage 3B-4 reference loaded | **PASS** |
| Stage 3B-4 hard guard pass | **PASS** |
| Stage 3B-4 precheck pass | **PASS** |
| Stage 3B-4 posterior interpretation false | **PASS** |
| Stage 3B-0 reference loaded | **PASS** |
| Stage 3B-0 hard guard pass | **PASS** |
| fixed-reference YAML loaded | **PASS** |
| minimal sampler YAML loaded | **PASS** |
| extended gate sampler YAML written | **PASS** |
| extended gate MCMC launched by this stage | **PASS** |
| all sampler runs success | **PASS** |
| chain files found | **PASS** |
| chain has enough total rows | **PASS** |
| chain has enough rows per prefix | **PASS** |
| chain has expected sampled columns | **PASS** |
| chain values finite | **PASS** |
| sampled parameters within prior bounds | **PASS** |
| sampled-parameter motion threshold met | **PASS** |
| split diagnostics recorded | **PASS** |
| split gate pass | **PASS** |
| tail diagnostics recorded | **PASS** |
| tail gate pass | **PASS** |
| tri-anchor monitoring evaluated | **PASS** |
| tri-anchor loglikes match monitoring ledger | **PASS** |
| posterior interpretation allowed | **NO** |
| posterior conclusions written | **NO** |
| hard guard pass | **PASS** |

Diagnostic outcome: `EXTENDED_CONVERGENCE_GATE_PILOT_PASS`

## Gate decision

Decision type: `EXTENDED_CONVERGENCE_GATE_PILOT_PASS`

Recommendation: Book Stage 3B-5. Next prepare the first production-run config/preflight, but keep posterior claims gated until a separately booked production run converges.

Next-stage hint: `Stage 3B-6 production-run configuration and preflight, no posterior claim yet`

## Summary snippets

```json
{
  "chain_rows": 384,
  "max_split_normalized_mean_range_seen": 1.4681199893182455,
  "max_tail_normalized_shift_seen": 1.3995932676433631,
  "motion_count": 5,
  "tri_anchor_monitoring_pass": true
}
```

## Outputs

- `json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot.json`
- `acceptance_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_acceptance.md`
- `extended_gate_sampler_yaml`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_pilot_sampler.yaml`
- `sampler_runs_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_sampler_runs.json`
- `chain_audit_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_chain_audit.json`
- `chain_columns_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_chain_columns.csv`
- `sample_stats_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_sample_stats.json`
- `sample_stats_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_sample_stats.csv`
- `split_diagnostics_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_split_diagnostics.json`
- `split_diagnostics_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_split_diagnostics.csv`
- `tail_diagnostics_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_tail_diagnostics.json`
- `tail_diagnostics_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_tail_diagnostics.csv`
- `tri_anchor_eval_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_tri_anchor_eval.json`
- `tri_anchor_eval_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_tri_anchor_eval.csv`
- `convergence_gate_manifest`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_convergence_gate_manifest.json`
- `chain_prefixes`: `['/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b5_extended_convergence_gate_pilot_chain01', '/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b5_extended_convergence_gate_pilot_chain02', '/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b5_extended_convergence_gate_pilot_chain03']`

## Booking decision

PASS: bookable as the extended convergence-gate pilot stage, provided git status is clean except for these artifacts.
This is still not posterior evidence; do not use these chains for scientific inference.

```bash
git add deu_validation/stage3b_5_extended_convergence_gate_pilot.py \
        deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot.json \
        deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_acceptance.md \
        deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_pilot_sampler.yaml \
        deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_sampler_runs.json \
        deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_chain_audit.json \
        deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_chain_columns.csv \
        deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_sample_stats.json \
        deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_sample_stats.csv \
        deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_split_diagnostics.json \
        deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_split_diagnostics.csv \
        deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_tail_diagnostics.json \
        deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_tail_diagnostics.csv \
        deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_tri_anchor_eval.json \
        deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_tri_anchor_eval.csv \
        deu_validation/stage3b_outputs/stage3b5_extended_convergence_gate_pilot_convergence_gate_manifest.json \
        deu_validation/stage3b_outputs/chains/stage3b5_extended_convergence_gate_pilot_chain*
git commit -m "Stage 3B-5 extended convergence-gate pilot"
git tag deu-stage3b5-extended-convergence-gate-pilot-v0
```
