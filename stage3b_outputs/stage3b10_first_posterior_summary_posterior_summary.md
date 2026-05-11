# Stage 3B-10 first posterior summary with tri-anchor caveats

Generated UTC: `2026-05-08T20:29:57+00:00`

This is the first posterior-language summary after the Stage 3B-9 readiness gate passed. It does not launch MCMC.

## Readiness context

- Readiness decision: `ADDITIONAL_PRODUCTION_CHAINS_READINESS_GATE_PASS`
- Combined chain rows: `4000`
- Chain files: `2`
- Segment gate pass: `True`
- Tail gate pass: `True`
- ESS gate pass: `True`
- Tri-anchor monitoring pass: `True`

## Working lock

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

## Parameter posterior summary

| Parameter | Mean | SD | q2.5 | q16 | q50 | q84 | q97.5 | Working lock |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| beta | 0.029491217 | 0.00055247252 | 0.028567552 | 0.028849905 | 0.029503285 | 0.030128599 | 0.030423268 | 0.03 |
| p_vis | 1.0474182 | 0.0013180231 | 1.0452071 | 1.0459375 | 1.0473475 | 1.048932 | 1.0498123 | 1.0475 |
| omega_b | 0.021980021 | 4.9536282e-05 | 0.021905925 | 0.021927323 | 0.021972856 | 0.0220347 | 0.022084005 | 0.022 |
| n_s | 0.98152322 | 0.00056806878 | 0.98056612 | 0.98086835 | 0.9815207 | 0.98217567 | 0.98247175 | 0.981875 |
| A_planck | 1.0250557 | 0.00084646128 | 1.0233787 | 1.0242044 | 1.0250715 | 1.0259026 | 1.0267361 | 1.025 |

## MAP-like chain row

This is the chain row with the smallest `minuslogpost` when that column exists. It is a chain diagnostic, not a separate optimizer result.

```json
{
  "display_values": {
    "A_planck": 1.0250579,
    "beta": 0.029595717,
    "n_s": 0.98118992,
    "omega_b": 0.021959556,
    "p_vis": 1.0473467
  },
  "found": true,
  "parameter_values": {
    "A_planck": 1.0250579,
    "deu_damping_envelope_beta": 0.029595717,
    "deu_transfer_polamp_p_vis": 1.0473467,
    "n_s": 0.98118992,
    "omega_b": 0.021959556
  },
  "row_index_zero_based": 1681,
  "selection_column": "minuslogpost",
  "selection_value": 572.83932
}
```

## Chain files summarized

| Chain file | Rows | Columns | Finite | min(minuslogpost) |
|---|---:|---:|---:|---:|
| `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b6_first_production_run.1.txt` | 2000 | 15 | True | 572.83932 |
| `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b6_first_production_run_additional_chain01.1.txt` | 2000 | 15 | True | 572.86331 |

## Tri-anchor context retained

| Anchor | beta | p_vis | omega_b | n_s | A_planck | profile | full loglike |
|---|---:|---:|---:|---:|---:|---:|---:|
| highl_anchor | 0.029 | 1.0475 | 0.02195 | 0.98 | 1.025 | 2 | -603.9366549798966 |
| lowl_plus_anchor | 0.0295 | 1.0475 | 0.02195 | 0.98125 | 1.025 | 2 | -603.8525238512426 |
| full_objective_working_lock | 0.03 | 1.0475 | 0.022 | 0.981875 | 1.025 | 2 | -603.8280689556785 |

## Caveats

- This is the first posterior-language summary after the Stage 3B-9 readiness gate, not a final publication claim.
- The sampled posterior is for the DEU full-objective working-lock configuration and the likelihood set used in the production YAML.
- The TT_lite likelihood remains excluded from the production sampler by the Stage 3B preflight design; TT_lite stays a monitoring/diagnostic object, not part of the sampled full-objective posterior.
- The tri-anchor split is retained as context: high-l, lowl+TTTEEE, and full-objective anchors are monitored even though the full-objective working lock is used for the production posterior.
- The readiness gate passing means this summary is allowed to be written; it does not by itself establish external robustness, model comparison, or a final cosmological result.
- Any scientific claim beyond this internal posterior summary still needs the next booked robustness/comparison stage.
