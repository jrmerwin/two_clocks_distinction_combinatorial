# Stage 3B-2 tiny sampler smoke test with tri-anchor monitoring

Generated UTC: `2026-05-08T16:15:17+00:00`

This stage launches a deliberately tiny Cobaya MCMC smoke test to verify sampler execution and chain plumbing.
It evaluates the tri-anchor monitoring sentinels and explicitly does not permit posterior interpretation.

## Acceptance

| Check | Status |
|---|---:|
| Stage 3B-1 reference loaded | **PASS** |
| Stage 3B-1 hard guard pass | **PASS** |
| Stage 3B-1 dry guard pass | **PASS** |
| Stage 3B-1 did not launch MCMC | **PASS** |
| Stage 3B-0 reference loaded | **PASS** |
| Stage 3B-0 hard guard pass | **PASS** |
| fixed-reference YAML loaded | **PASS** |
| minimal sampler YAML loaded | **PASS** |
| smoke sampler YAML written | **PASS** |
| tiny MCMC launched by this stage | **PASS** |
| sampler run success | **PASS** |
| chain files found | **PASS** |
| chain has enough rows for smoke | **PASS** |
| chain has expected sampled columns | **PASS** |
| chain values finite | **PASS** |
| tri-anchor monitoring evaluated | **PASS** |
| tri-anchor loglikes match monitoring ledger | **PASS** |
| posterior interpretation allowed | **NO** |
| posterior conclusions written | **NO** |
| smoke manifest written | **PASS** |
| sampler run JSON written | **PASS** |
| chain audit JSON written | **PASS** |
| chain columns CSV written | **PASS** |
| tri-anchor eval JSON written | **PASS** |
| tri-anchor eval CSV written | **PASS** |
| script completed | **PASS** |
| hard guard pass | **PASS** |

Diagnostic outcome: `TINY_SAMPLER_SMOKE_TEST_PASS`

## Smoke-test decision

Decision type: `TINY_SAMPLER_SMOKE_TEST_PASS`

Recommendation: Book Stage 3B-2. Next run a short non-interpretive pilot chain with the same tri-anchor monitoring; still do not claim posterior evidence.

Next-stage hint: `Stage 3B-3 short non-interpretive pilot chain with tri-anchor monitoring`

## Chain audit

```json
{
  "all_chain_values_finite": true,
  "all_expected_sampled_columns_present": true,
  "chain_files": [
    "/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b2_tiny_sampler_smoke_test.1.txt"
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
      "n_rows": 16,
      "path": "/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b2_tiny_sampler_smoke_test.1.txt",
      "raw_header_lines_tail": [
        "#        weight    minuslogpost deu_damping_envelope_beta deu_transfer_polamp_p_vis         omega_b             n_s        A_planck       chi2__CMB   minuslogprior minuslogprior__0            chi2 chi2__planck_2018_highl_plik.TTTEEE_lite chi2__planck_2018_lowl.TT chi2__planck_2018_lowl.EE chi2__planck_2018_lensing.native"
      ],
      "rows_preview": [
        [
          1.0,
          575.72006,
          0.030483485,
          1.0469429,
          0.022005169,
          0.98141659,
          1.0264,
          1213.1399,
          -30.849897,
          -30.849897,
          1213.1399,
          771.39522,
          26.288638,
          397.80932,
          17.646727
        ],
        [
          1.0,
          577.36895,
          0.029818753,
          1.046831,
          0.022051309,
          0.98080153,
          1.0267496,
          1216.4377,
          -30.849897,
          -30.849897,
          1216.4377,
          774.74116,
          26.391871,
          397.8151,
          17.48957
        ],
        [
          2.0,
          574.35914,
          0.029794079,
          1.0466877,
          0.022052123,
          0.98074302,
          1.0253645,
          1210.4181,
          -30.849897,
          -30.849897,
          1210.4181,
          767.60096,
          26.663321,
          397.84866,
          18.305123
        ]
      ]
    }
  ],
  "chain_prefix": "/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b2_tiny_sampler_smoke_test",
  "enough_rows_for_smoke": true,
  "expected_sampled_columns_present": {
    "A_planck": true,
    "deu_damping_envelope_beta": true,
    "deu_transfer_polamp_p_vis": true,
    "n_s": true,
    "omega_b": true
  },
  "min_required_rows": 4,
  "n_chain_files": 1,
  "special_columns_present": {
    "minuslogpost": true,
    "weight": true
  },
  "total_rows": 16,
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

- `json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b2_tiny_sampler_smoke_test.json`
- `acceptance_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b2_tiny_sampler_smoke_test_acceptance.md`
- `smoke_sampler_yaml`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b2_tiny_sampler_smoke_test_smoke_sampler.yaml`
- `sampler_run_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b2_tiny_sampler_smoke_test_sampler_run.json`
- `chain_audit_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b2_tiny_sampler_smoke_test_chain_audit.json`
- `chain_columns_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b2_tiny_sampler_smoke_test_chain_columns.csv`
- `tri_anchor_eval_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b2_tiny_sampler_smoke_test_tri_anchor_eval.json`
- `tri_anchor_eval_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b2_tiny_sampler_smoke_test_tri_anchor_eval.csv`
- `smoke_manifest`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b2_tiny_sampler_smoke_test_smoke_manifest.json`
- `chain_prefix`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/chains/stage3b2_tiny_sampler_smoke_test`

## Booking decision

PASS: bookable as the tiny sampler smoke-test stage, provided git status is clean except for these artifacts.
This is not posterior evidence; do not use the smoke chain for scientific inference.

```bash
git add deu_validation/stage3b_2_tiny_sampler_smoke_test.py \
        deu_validation/stage3b_outputs/stage3b2_tiny_sampler_smoke_test.json \
        deu_validation/stage3b_outputs/stage3b2_tiny_sampler_smoke_test_acceptance.md \
        deu_validation/stage3b_outputs/stage3b2_tiny_sampler_smoke_test_smoke_sampler.yaml \
        deu_validation/stage3b_outputs/stage3b2_tiny_sampler_smoke_test_sampler_run.json \
        deu_validation/stage3b_outputs/stage3b2_tiny_sampler_smoke_test_chain_audit.json \
        deu_validation/stage3b_outputs/stage3b2_tiny_sampler_smoke_test_chain_columns.csv \
        deu_validation/stage3b_outputs/stage3b2_tiny_sampler_smoke_test_tri_anchor_eval.json \
        deu_validation/stage3b_outputs/stage3b2_tiny_sampler_smoke_test_tri_anchor_eval.csv \
        deu_validation/stage3b_outputs/stage3b2_tiny_sampler_smoke_test_smoke_manifest.json \
        deu_validation/stage3b_outputs/chains/stage3b2_tiny_sampler_smoke_test*
git commit -m "Stage 3B-2 tiny sampler smoke test"
git tag deu-stage3b2-tiny-sampler-smoke-test-v0
```
