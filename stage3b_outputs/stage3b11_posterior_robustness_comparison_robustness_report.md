# Stage 3B-11 posterior robustness and comparison checks

Generated UTC: `2026-05-08T20:55:40+00:00`

This stage does not launch MCMC. It recomputes the Stage 3B-10 posterior summary, compares chain splits, evaluates diagnostic points, and retains the caveats.

## Decision

- Decision type: `POSTERIOR_ROBUSTNESS_COMPARISON_PASS`
- Recommendation: Book Stage 3B-11. Next run an external/model-comparison framing stage before any final publication-style claim.
- Next-stage hint: `Stage 3B-12 external/model-comparison framing and final-claim preflight`
- Final publication claims allowed: `False`

## Recomputed posterior summary

| Parameter | Mean | SD | q16 | q50 | q84 |
|---|---:|---:|---:|---:|---:|
| beta | 0.029491217 | 0.00055247252 | 0.028849905 | 0.029503285 | 0.030128599 |
| p_vis | 1.0474182 | 0.0013180231 | 1.0459375 | 1.0473475 | 1.048932 |
| omega_b | 0.021980021 | 4.9536282e-05 | 0.021927323 | 0.021972856 | 0.0220347 |
| n_s | 0.98152322 | 0.00056806878 | 0.98086835 | 0.9815207 | 0.98217567 |
| A_planck | 1.0250557 | 0.00084646128 | 1.0242044 | 1.0250715 | 1.0259026 |

## Diagnostic point deltas versus working lock

| Point | Bundle | Δ loglike vs working lock |
|---|---|---:|
| posterior_mean | plik_TT_lite | 0.21347307 |
| posterior_mean | plik_TTTEEE_lite | 0.03365289 |
| posterior_mean | lowl_available | -0.050846933 |
| posterior_mean | lensing_native | -0.046750963 |
| posterior_mean | lowl_plus_plik_TTTEEE_lite | -0.017194043 |
| posterior_mean | lowl_plik_TTTEEE_lite_lensing_native | -0.063945006 |
| posterior_median | plik_TT_lite | 0.33302366 |
| posterior_median | plik_TTTEEE_lite | 0.053242862 |
| posterior_median | lowl_available | -0.049811953 |
| posterior_median | lensing_native | -0.039339428 |
| posterior_median | lowl_plus_plik_TTTEEE_lite | 0.0034309087 |
| posterior_median | lowl_plik_TTTEEE_lite_lensing_native | -0.03590852 |
| map_like_chain_row | plik_TT_lite | 0.58152478 |
| map_like_chain_row | plik_TTTEEE_lite | 0.096137233 |
| map_like_chain_row | lowl_available | -0.074991605 |
| map_like_chain_row | lensing_native | -0.014852212 |
| map_like_chain_row | lowl_plus_plik_TTTEEE_lite | 0.021145627 |
| map_like_chain_row | lowl_plik_TTTEEE_lite_lensing_native | 0.0062934152 |
| tri_anchor_highl | plik_TT_lite | 0.85938684 |
| tri_anchor_highl | plik_TTTEEE_lite | 0.20556256 |
| tri_anchor_highl | lowl_available | -0.24719804 |
| tri_anchor_highl | lensing_native | -0.066950536 |
| tri_anchor_highl | lowl_plus_plik_TTTEEE_lite | -0.041635488 |
| tri_anchor_highl | lowl_plik_TTTEEE_lite_lensing_native | -0.10858602 |
| tri_anchor_lowl_plus | plik_TT_lite | 0.76278854 |
| tri_anchor_lowl_plus | plik_TTTEEE_lite | 0.11892903 |
| tri_anchor_lowl_plus | lowl_available | -0.077913851 |
| tri_anchor_lowl_plus | lensing_native | -0.065470069 |
| tri_anchor_lowl_plus | lowl_plus_plik_TTTEEE_lite | 0.041015174 |
| tri_anchor_lowl_plus | lowl_plik_TTTEEE_lite_lensing_native | -0.024454896 |
| tri_anchor_full_objective | plik_TT_lite | 0 |
| tri_anchor_full_objective | plik_TTTEEE_lite | 0 |
| tri_anchor_full_objective | lowl_available | 0 |
| tri_anchor_full_objective | lensing_native | 0 |
| tri_anchor_full_objective | lowl_plus_plik_TTTEEE_lite | 0 |
| tri_anchor_full_objective | lowl_plik_TTTEEE_lite_lensing_native | 0 |

## Caveats retained

- This is the first posterior-language summary after the Stage 3B-9 readiness gate, not a final publication claim.
- The sampled posterior is for the DEU full-objective working-lock configuration and the likelihood set used in the production YAML.
- The TT_lite likelihood remains excluded from the production sampler by the Stage 3B preflight design; TT_lite stays a monitoring/diagnostic object, not part of the sampled full-objective posterior.
- The tri-anchor split is retained as context: high-l, lowl+TTTEEE, and full-objective anchors are monitored even though the full-objective working lock is used for the production posterior.
- The readiness gate passing means this summary is allowed to be written; it does not by itself establish external robustness, model comparison, or a final cosmological result.
- Any scientific claim beyond this internal posterior summary still needs the next booked robustness/comparison stage.
