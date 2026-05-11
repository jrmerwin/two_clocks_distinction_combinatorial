# Stage 3B-3 short non-interpretive pilot chain with tri-anchor monitoring

Generated UTC: `2026-05-08T16:42:43+00:00`

This stage launches a short Cobaya MCMC pilot to verify sampler mechanics beyond the tiny smoke test.
It checks chain files, expected sampled columns, finite values, basic sampled-parameter motion, prior bounds, and tri-anchor monitoring.
It explicitly does not permit posterior interpretation.

## Acceptance

| Check | Status |
|---|---:|
| Stage 3B-2 reference loaded | **PASS** |
| Stage 3B-2 hard guard pass | **PASS** |
| Stage 3B-2 smoke pass | **PASS** |
| Stage 3B-2 posterior interpretation false | **PASS** |
| Stage 3B-0 reference loaded | **PASS** |
| Stage 3B-0 hard guard pass | **PASS** |
| fixed-reference YAML loaded | **PASS** |
| minimal sampler YAML loaded | **PASS** |
| pilot sampler YAML written | **PASS** |
| pilot MCMC launched by this stage | **PASS** |
| sampler run success | **PASS** |
| chain files found | **PASS** |
| chain has enough rows for pilot | **PASS** |
| chain has expected sampled columns | **PASS** |
| chain values finite | **PASS** |
| sampled parameters within prior bounds | **PASS** |
| sampled-parameter motion recorded | **PASS** |
| tri-anchor monitoring evaluated | **PASS** |
| tri-anchor loglikes match monitoring ledger | **PASS** |
| posterior interpretation allowed | **NO** |
| posterior conclusions written | **NO** |
| pilot manifest written | **PASS** |
| sampler run JSON written | **PASS** |
| chain audit JSON written | **PASS** |
| chain columns CSV written | **PASS** |
| sample stats JSON written | **PASS** |
| sample stats CSV written | **PASS** |
| tri-anchor eval JSON written | **PASS** |
| tri-anchor eval CSV written | **PASS** |
| script completed | **PASS** |
| hard guard pass | **PASS** |

Diagnostic outcome: `SHORT_PILOT_CHAIN_PASS`

## Pilot decision

Decision type: `SHORT_PILOT_CHAIN_PASS`

Recommendation: Book Stage 3B-3. Next run a longer still-non-interpretive pilot/convergence-precheck; do not claim posterior evidence yet.

Next-stage hint: `Stage 3B-4 convergence-precheck pilot with tri-anchor monitoring`

## Sample stats summary

```json
{
  "all_sampled_parameters_within_prior_bounds": true,
  "any_sampled_parameter_motion_recorded": true,
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
  "n_rows": 64
}
```

## Chain audit

```json
{
  "all_chain_values_finite": true,
  "all_expected_sampled_columns_present": true,
  "chain_files": [
    "/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b3_short_pilot_chain.1.txt"
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
      "n_rows": 64,
      "path": "/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b3_short_pilot_chain.1.txt",
      "raw_header_lines_tail": [
        "#        weight    minuslogpost deu_damping_envelope_beta deu_transfer_polamp_p_vis         omega_b             n_s        A_planck       chi2__CMB   minuslogprior minuslogprior__0            chi2 chi2__planck_2018_highl_plik.TTTEEE_lite chi2__planck_2018_lowl.TT chi2__planck_2018_lowl.EE chi2__planck_2018_lensing.native"
      ],
      "rows_preview": [
        [
          1.0,
          573.44776,
          0.030464961,
          1.047042,
          0.022020122,
          0.98147409,
          1.025,
          1208.5953,
          -30.849897,
          -30.849897,
          1208.5953,
          765.71383,
          26.532063,
          397.85086,
          18.498553
        ],
        [
          3.0,
          573.45388,
          0.03044803,
          1.0470202,
          0.022019968,
          0.98145992,
          1.025,
          1208.6076,
          -30.849897,
          -30.849897,
          1208.6076,
          765.72097,
          26.535739,
          397.85086,
          18.49999
        ],
        [
          2.0,
          573.9405,
          0.03044803,
          1.0470202,
          0.022019968,
          0.98145992,
          1.0237373,
          1209.5808,
          -30.849897,
          -30.849897,
          1209.5808,
          765.57931,
          26.77166,
          397.87667,
          19.353157
        ]
      ]
    }
  ],
  "chain_prefix": "/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b3_short_pilot_chain",
  "enough_rows_for_pilot": true,
  "expected_sampled_columns_present": {
    "A_planck": true,
    "deu_damping_envelope_beta": true,
    "deu_transfer_polamp_p_vis": true,
    "n_s": true,
    "omega_b": true
  },
  "min_required_rows": 32,
  "n_chain_files": 1,
  "special_columns_present": {
    "minuslogpost": true,
    "weight": true
  },
  "total_rows": 64,
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

- `json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b3_short_pilot_chain.json`
- `acceptance_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_acceptance.md`
- `pilot_sampler_yaml`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_pilot_sampler.yaml`
- `sampler_run_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_sampler_run.json`
- `chain_audit_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_chain_audit.json`
- `chain_columns_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_chain_columns.csv`
- `sample_stats_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_sample_stats.json`
- `sample_stats_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_sample_stats.csv`
- `tri_anchor_eval_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_tri_anchor_eval.json`
- `tri_anchor_eval_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_tri_anchor_eval.csv`
- `pilot_manifest`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_pilot_manifest.json`
- `chain_prefix`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b3_short_pilot_chain`

## Booking decision

PASS: bookable as the short pilot-chain stage, provided git status is clean except for these artifacts.
This is still not posterior evidence; do not use the pilot chain for scientific inference.

```bash
git add deu_validation/stage3b_3_short_pilot_chain.py \
        deu_validation/stage3b_outputs/stage3b3_short_pilot_chain.json \
        deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_acceptance.md \
        deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_pilot_sampler.yaml \
        deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_sampler_run.json \
        deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_chain_audit.json \
        deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_chain_columns.csv \
        deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_sample_stats.json \
        deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_sample_stats.csv \
        deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_tri_anchor_eval.json \
        deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_tri_anchor_eval.csv \
        deu_validation/stage3b_outputs/stage3b3_short_pilot_chain_pilot_manifest.json \
        deu_validation/stage3b_outputs/chains/stage3b3_short_pilot_chain*
git commit -m "Stage 3B-3 short pilot chain"
git tag deu-stage3b3-short-pilot-chain-v0
```
