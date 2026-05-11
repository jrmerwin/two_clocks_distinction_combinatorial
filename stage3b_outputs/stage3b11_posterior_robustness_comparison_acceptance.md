# Stage 3B-11 posterior robustness and comparison acceptance

Generated UTC: `2026-05-08T20:55:40+00:00`

This stage is a non-MCMC robustness/comparison assessment of the booked Stage 3B-10 posterior summary.

## Acceptance

| Check | Status |
|---|---:|
| Stage 3B-10 reference loaded | **PASS** |
| Stage 3B-10 hard guard pass | **PASS** |
| Stage 3B-10 summary written | **PASS** |
| Stage 3B-10 final publication claims not allowed | **PASS** |
| Stage 3B-9 posterior readiness gate pass | **PASS** |
| chain files found | **PASS** |
| chain files count at least two | **PASS** |
| expected sampled columns present | **PASS** |
| chain values finite | **PASS** |
| Stage 3B-10 summary reproduced | **PASS** |
| split robustness gate recorded | **PASS** |
| point evaluations success | **PASS** |
| TT_lite diagnostic recorded | **PASS** |
| tri-anchor context retained | **PASS** |
| MCMC launched by this stage | **NO** |
| posterior robustness gate pass | **PASS** |
| final publication claims allowed | **NO** |
| hard guard pass | **PASS** |

Diagnostic outcome: `POSTERIOR_ROBUSTNESS_COMPARISON_PASS`

## Robustness decision

Decision type: `POSTERIOR_ROBUSTNESS_COMPARISON_PASS`

Recommendation: Book Stage 3B-11. Next run an external/model-comparison framing stage before any final publication-style claim.

Next-stage hint: `Stage 3B-12 external/model-comparison framing and final-claim preflight`

## Outputs

- `json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison.json`
- `acceptance_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_acceptance.md`
- `robustness_report_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_robustness_report.md`
- `recomputed_summary_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_recomputed_parameter_summary.csv`
- `summary_reproduction_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_summary_reproduction.csv`
- `per_chain_summary_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_per_chain_summary.csv`
- `leave_one_out_summary_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_leave_one_out_summary.csv`
- `split_robustness_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_split_robustness.csv`
- `point_eval_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_point_evaluations.json`
- `point_eval_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_point_evaluations.csv`
- `tt_lite_diagnostic_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_tt_lite_diagnostic.csv`
- `tri_anchor_context_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_tri_anchor_context.csv`
- `caveat_check_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_caveat_check.md`
- `robustness_manifest`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_robustness_manifest.json`

## Booking decision

PASS: bookable as the posterior robustness/comparison stage, provided git status is clean except for these artifacts.
Final publication-style claims remain blocked by this stage.

```bash
git add deu_validation/stage3b_11_posterior_robustness_comparison.py \
        deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison.json \
        deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_acceptance.md \
        deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_robustness_report.md \
        deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_recomputed_parameter_summary.csv \
        deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_summary_reproduction.csv \
        deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_per_chain_summary.csv \
        deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_leave_one_out_summary.csv \
        deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_split_robustness.csv \
        deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_point_evaluations.json \
        deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_point_evaluations.csv \
        deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_tt_lite_diagnostic.csv \
        deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_tri_anchor_context.csv \
        deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_caveat_check.md \
        deu_validation/stage3b_outputs/stage3b11_posterior_robustness_comparison_robustness_manifest.json
git commit -m "Stage 3B-11 posterior robustness comparison"
git tag deu-stage3b11-posterior-robustness-comparison-v0
```