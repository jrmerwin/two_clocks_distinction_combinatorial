# Stage 3B-0 full-objective working-lock note

Generated UTC: `2026-05-08T15:20:50+00:00`

Stage 3A-10 closed the fixed-grid diagnostic search with the full-objective working lock stable and the tri-anchor ledger retained.
No MCMC was launched by this setup stage.

## Working lock for Stage 3B seed

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

## Stage 3A-10 decision

Decision type: `FULL_OBJECTIVE_WORKING_LOCK_GUARD_STABLE_TRI_LEDGER_RETAINED`

Recommendation: Use the full-objective working lock as the Stage 3B seed, retaining the tri-anchor ledger for monitoring.

Next-stage hint: `Stage 3B minimal sampler setup with tri-anchor monitoring, after writing a lock note`

## Tri-anchor monitoring ledger

| Anchor | beta | p_vis | omega_b | n_s | A_planck | profile | TTTEEE | lowl+TTTEEE | full |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| highl_anchor | 0.029 | 1.0475 | 0.02195 | 0.98 | 1.025 | 2 | -382.09644863724304 | -594.4816399067552 | -603.9366549798966 |
| lowl_plus_anchor | 0.0295 | 1.0475 | 0.02195 | 0.98125 | 1.025 | 2 | -382.1830821680578 | -594.3989892447191 | -603.8525238512426 |
| full_objective_working_lock | 0.03 | 1.0475 | 0.022 | 0.981875 | 1.025 | 2 | -382.30201119323436 | -594.440004418515 | -603.8280689556785 |

## Stage 3B setup artifacts

- Fixed reference check YAML: fixed diagnostic only.
- Minimal sampler seed YAML: full-objective sampler scaffold only; review before running.
- Monitoring points JSON: tri-anchor sentinels for post-setup checks.

## Acceptance

Hard guard pass: `True`

