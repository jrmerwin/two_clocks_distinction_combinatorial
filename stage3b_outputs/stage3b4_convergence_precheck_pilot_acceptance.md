# Stage 3B-4 convergence-precheck pilot with tri-anchor monitoring

Generated UTC: `2026-05-08T17:04:03+00:00`

This stage launches a small set of short Cobaya MCMC pilot chains to check multi-chain plumbing.
It records crude split diagnostics and tri-anchor monitoring, but it explicitly does not permit posterior interpretation.

## Acceptance

| Check | Status |
|---|---:|
| Stage 3B-3 reference loaded | **PASS** |
| Stage 3B-3 hard guard pass | **PASS** |
| Stage 3B-3 short pilot pass | **PASS** |
| Stage 3B-3 posterior interpretation false | **PASS** |
| Stage 3B-0 reference loaded | **PASS** |
| Stage 3B-0 hard guard pass | **PASS** |
| fixed-reference YAML loaded | **PASS** |
| minimal sampler YAML loaded | **PASS** |
| precheck sampler YAML written | **PASS** |
| precheck MCMC launched by this stage | **PASS** |
| all sampler runs success | **PASS** |
| chain files found | **PASS** |
| chain has enough total rows | **PASS** |
| chain has enough rows per prefix | **PASS** |
| chain has expected sampled columns | **PASS** |
| chain values finite | **PASS** |
| sampled parameters within prior bounds | **PASS** |
| sampled-parameter motion threshold met | **PASS** |
| split diagnostics recorded | **PASS** |
| tri-anchor monitoring evaluated | **PASS** |
| tri-anchor loglikes match monitoring ledger | **PASS** |
| posterior interpretation allowed | **NO** |
| posterior conclusions written | **NO** |
| precheck manifest written | **PASS** |
| sampler runs JSON written | **PASS** |
| chain audit JSON written | **PASS** |
| chain columns CSV written | **PASS** |
| sample stats JSON written | **PASS** |
| sample stats CSV written | **PASS** |
| split diagnostics JSON written | **PASS** |
| split diagnostics CSV written | **PASS** |
| tri-anchor eval JSON written | **PASS** |
| tri-anchor eval CSV written | **PASS** |
| script completed | **PASS** |
| hard guard pass | **PASS** |

Diagnostic outcome: `CONVERGENCE_PRECHECK_PILOT_PASS`

## Precheck decision

Decision type: `CONVERGENCE_PRECHECK_PILOT_PASS`

Recommendation: Book Stage 3B-4. Next run an extended still-non-interpretive pilot/convergence gate with tri-anchor monitoring; posterior claims remain disallowed.

Next-stage hint: `Stage 3B-5 extended convergence-gate pilot with tri-anchor monitoring`

## Sample stats summary

```json
{
  "all_sampled_parameters_with_motion": true,
  "all_sampled_parameters_within_prior_bounds": true,
  "header": [
    "weight",
    "minuslogpost",
    "deu_damping_envelope_beta",
    "deu_transfer_polamp_p_vis",
    "omega_b",
    "n_s",
    "A_planck",
    "chi2__CMB",
    "minuslogprior",
    "minuslogprior__0",
    "chi2",
    "chi2__planck_2018_highl_plik.TTTEEE_lite",
    "chi2__planck_2018_lowl.TT",
    "chi2__planck_2018_lowl.EE",
    "chi2__planck_2018_lensing.native"
  ],
  "motion_by_parameter": {
    "A_planck": true,
    "deu_damping_envelope_beta": true,
    "deu_transfer_polamp_p_vis": true,
    "n_s": true,
    "omega_b": true
  },
  "motion_count": 5,
  "n_rows": 192
}
```

## Chain audit

```json
{
  "all_chain_values_finite": true,
  "all_expected_sampled_columns_present": true,
  "chain_files": [
    "/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b4_convergence_precheck_pilot_chain01.1.txt",
    "/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b4_convergence_precheck_pilot_chain02.1.txt"
  ],
  "chain_files_found": true,
  "chain_infos": [
    {
      "all_numeric_finite": true,
      "header": [
        "weight",
        "minuslogpost",
        "deu_damping_envelope_beta",
        "deu_transfer_polamp_p_vis",
        "omega_b",
        "n_s",
        "A_planck",
        "chi2__CMB",
        "minuslogprior",
        "minuslogprior__0",
        "chi2",
        "chi2__planck_2018_highl_plik.TTTEEE_lite",
        "chi2__planck_2018_lowl.TT",
        "chi2__planck_2018_lowl.EE",
        "chi2__planck_2018_lensing.native"
      ],
      "n_columns": 15,
      "n_rows": 96,
      "path": "/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b4_convergence_precheck_pilot_chain01.1.txt",
      "raw_header_lines_tail": [
        "#        weight    minuslogpost deu_damping_envelope_beta deu_transfer_polamp_p_vis         omega_b             n_s        A_planck       chi2__CMB   minuslogprior minuslogprior__0            chi2 chi2__planck_2018_highl_plik.TTTEEE_lite chi2__planck_2018_lowl.TT chi2__planck_2018_lowl.EE chi2__planck_2018_lensing.native"
      ],
      "rows_preview": [
        [
          1.0,
          572.97896,
          0.030232623,
          1.0474716,
          0.021964775,
          0.98179941,
          1.025,
          1207.6577,
          -30.849897,
          -30.849897,
          1207.6577,
          764.6266,
          26.438526,
          397.87538,
          18.717202
        ],
        [
          2.0,
          572.87477,
          0.029955289,
          1.0469339,
          0.02195113,
          0.9816323,
          1.025,
          1207.4493,
          -30.849897,
          -30.849897,
          1207.4493,
          764.34012,
          26.482111,
          397.87538,
          18.751724
        ],
        [
          1.0,
          572.97953,
          0.030193983,
          1.0473562,
          0.021950487,
          0.98241182,
          1.025,
          1207.6589,
          -30.849897,
          -30.849897,
          1207.6589,
          764.71836,
          26.276564,
          397.84712,
          18.81682
        ]
      ]
    },
    {
      "all_numeric_finite": true,
      "header": [
        "weight",
        "minuslogpost",
        "deu_damping_envelope_beta",
        "deu_transfer_polamp_p_vis",
        "omega_b",
        "n_s",
        "A_planck",
        "chi2__CMB",
        "minuslogprior",
        "minuslogprior__0",
        "chi2",
        "chi2__planck_2018_highl_plik.TTTEEE_lite",
        "chi2__planck_2018_lowl.TT",
        "chi2__planck_2018_lowl.EE",
        "chi2__planck_2018_lensing.native"
      ],
      "n_columns": 15,
      "n_rows": 96,
      "path": "/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b4_convergence_precheck_pilot_chain02.1.txt",
      "raw_header_lines_tail": [
        "#        weight    minuslogpost deu_damping_envelope_beta deu_transfer_polamp_p_vis         omega_b             n_s        A_planck       chi2__CMB   minuslogprior minuslogprior__0            chi2 chi2__planck_2018_highl_plik.TTTEEE_lite chi2__planck_2018_lowl.TT chi2__planck_2018_lowl.EE chi2__planck_2018_lensing.native"
      ],
      "rows_preview": [
        [
          1.0,
          573.39108,
          0.028916941,
          1.047365,
          0.022015982,
          0.98147422,
          1.025,
          1208.4819,
          -30.849897,
          -30.849897,
          1208.4819,
          765.0535,
          26.530767,
          397.85086,
          19.046827
        ],
        [
          2.0,
          573.27622,
          0.0288959,
          1.0488855,
          0.021948972,
          0.98113586,
          1.0255438,
          1208.2522,
          -30.849897,
          -30.849897,
          1208.2522,
          765.02926,
          26.510709,
          397.83042,
          18.881839
        ],
        [
          1.0,
          574.36405,
          0.028750303,
          1.0497484,
          0.021994786,
          0.98137254,
          1.0265535,
          1210.4279,
          -30.849897,
          -30.849897,
          1210.4279,
          767.99128,
          26.270186,
          397.8233,
          18.343137
        ]
      ]
    }
  ],
  "enough_rows_per_prefix": true,
  "enough_total_rows_for_precheck": true,
  "expected_sampled_columns_present": {
    "A_planck": true,
    "deu_damping_envelope_beta": true,
    "deu_transfer_polamp_p_vis": true,
    "n_s": true,
    "omega_b": true
  },
  "min_rows_per_chain": 24,
  "min_total_rows": 96,
  "n_chain_files": 2,
  "prefix_reports": [
    {
      "chain_files": [
        "/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b4_convergence_precheck_pilot_chain01.1.txt"
      ],
      "enough_rows": true,
      "n_chain_files": 1,
      "prefix": "/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b4_convergence_precheck_pilot_chain01",
      "rows": 96
    },
    {
      "chain_files": [
        "/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b4_convergence_precheck_pilot_chain02.1.txt"
      ],
      "enough_rows": true,
      "n_chain_files": 1,
      "prefix": "/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b4_convergence_precheck_pilot_chain02",
      "rows": 96
    }
  ],
  "prefixes": [
    "/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b4_convergence_precheck_pilot_chain01",
    "/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b4_convergence_precheck_pilot_chain02"
  ],
  "special_columns_present": {
    "minuslogpost": true,
    "weight": true
  },
  "total_rows": 192,
  "unique_columns": [
    "A_planck",
    "chi2",
    "chi2__CMB",
    "chi2__planck_2018_highl_plik.TTTEEE_lite",
    "chi2__planck_2018_lensing.native",
    "chi2__planck_2018_lowl.EE",
    "chi2__planck_2018_lowl.TT",
    "deu_damping_envelope_beta",
    "deu_transfer_polamp_p_vis",
    "minuslogpost",
    "minuslogprior",
    "minuslogprior__0",
    "n_s",
    "omega_b",
    "weight"
  ]
}
```

## Split diagnostics summary

```json
{
  "diagnostics_recorded": true,
  "n_prefixes": 2,
  "note": "Crude short-chain split diagnostics only; not a convergence claim and not posterior evidence."
}
```

## Tri-anchor monitoring

```json
{
  "all_tri_anchor_loglikes_match_monitoring_ledger": true,
  "all_tri_anchors_evaluated": true,
  "expected_tri_anchor_count": 3,
  "tolerance": 1e-05,
  "tri_anchor_count": 3
}
```

## Outputs

- `json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot.json`
- `acceptance_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_acceptance.md`
- `precheck_sampler_yaml`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_pilot_sampler.yaml`
- `sampler_runs_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_sampler_runs.json`
- `chain_audit_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_chain_audit.json`
- `chain_columns_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_chain_columns.csv`
- `sample_stats_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_sample_stats.json`
- `sample_stats_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_sample_stats.csv`
- `split_diagnostics_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_split_diagnostics.json`
- `split_diagnostics_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_split_diagnostics.csv`
- `tri_anchor_eval_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_tri_anchor_eval.json`
- `tri_anchor_eval_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_tri_anchor_eval.csv`
- `precheck_manifest`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_precheck_manifest.json`
- `chain_prefixes`: `['/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b4_convergence_precheck_pilot_chain01', '/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b4_convergence_precheck_pilot_chain02']`

## Booking decision

PASS: bookable as the convergence-precheck pilot stage, provided git status is clean except for these artifacts.
This is still not posterior evidence; do not use these chains for scientific inference.

```bash
git add deu_validation/stage3b_4_convergence_precheck_pilot.py \
        deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot.json \
        deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_acceptance.md \
        deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_pilot_sampler.yaml \
        deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_sampler_runs.json \
        deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_chain_audit.json \
        deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_chain_columns.csv \
        deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_sample_stats.json \
        deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_sample_stats.csv \
        deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_split_diagnostics.json \
        deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_split_diagnostics.csv \
        deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_tri_anchor_eval.json \
        deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_tri_anchor_eval.csv \
        deu_validation/stage3b_outputs/stage3b4_convergence_precheck_pilot_precheck_manifest.json \
        deu_validation/stage3b_outputs/chains/stage3b4_convergence_precheck_pilot_chain*
git commit -m "Stage 3B-4 convergence-precheck pilot"
git tag deu-stage3b4-convergence-precheck-pilot-v0
```
