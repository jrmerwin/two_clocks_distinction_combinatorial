# Stage 3B-13 scoped final-claim lock

## Allowed scoped statements

- **allowed_001**: A caveated posterior summary exists for the DEU full-objective working-lock production sampler.  
  Caveat: This is not a final publication claim and not a model-superiority claim.
- **allowed_002**: The production posterior used the full-objective likelihood set and the guarded working-lock configuration.  
  Caveat: The statement is scoped to the production YAML and chain family only.
- **allowed_003**: The readiness and robustness gates passed on two production chain files and 4000 combined rows.  
  Caveat: This does not by itself establish external model comparison or publication-grade superiority.
- **allowed_004**: The tri-anchor context is retained as a monitoring caveat around the full-objective posterior.  
  Caveat: Do not erase the high-l/lowl/full-objective split from the narrative.
- **allowed_005**: TT_lite may be described as diagnostic-only monitoring context, not part of the sampled posterior likelihood.  
  Caveat: Do not claim the production posterior includes TT_lite.
- **param_beta**: Posterior summary for beta: mean=0.02949121724807528, median=0.029503285, q16=0.028849905, q84=0.030128599.  
  Caveat: Report as chain-summary posterior under the production sampler, not as final external cosmological truth.
- **param_p_vis**: Posterior summary for p_vis: mean=1.0474182267750214, median=1.0473475, q16=1.0459375, q84=1.048932.  
  Caveat: Report as chain-summary posterior under the production sampler, not as final external cosmological truth.
- **param_omega_b**: Posterior summary for omega_b: mean=0.021980020954662106, median=0.021972856, q16=0.021927323, q84=0.0220347.  
  Caveat: Report as chain-summary posterior under the production sampler, not as final external cosmological truth.
- **param_n_s**: Posterior summary for n_s: mean=0.9815232201591104, median=0.9815207, q16=0.98086835, q84=0.98217567.  
  Caveat: Report as chain-summary posterior under the production sampler, not as final external cosmological truth.
- **param_A_planck**: Posterior summary for A_planck: mean=1.0250557243798117, median=1.0250715, q16=1.0242044, q84=1.0259026.  
  Caveat: Report as chain-summary posterior under the production sampler, not as final external cosmological truth.

## Blocked statements

- **blocked_001**: DEU is superior to ΛCDM or the native baseline.  
  Reason: No explicit baseline/native model-comparison evidence stage has been booked.
- **blocked_002**: The production posterior includes TT_lite.  
  Reason: TT_lite was diagnostic-only and excluded from the production sampler likelihood.
- **blocked_003**: Final publication-style claim or external robustness claim.  
  Reason: Stage 3B-12 explicitly kept final publication claims blocked.
- **blocked_004**: All Planck likelihood components prefer the same DEU anchor.  
  Reason: The tri-anchor split is retained and must remain visible.
- **blocked_005**: The MAP-like chain row is an optimizer result or independent best fit.  
  Reason: Stage 3B-10 records it as a chain diagnostic only.

## Required extensions

- **ext_001**: Explicit native/baseline model-comparison extension — Compare DEU scoped posterior/fit context against native/baseline under matched likelihood scope.
- **ext_002**: Final publication-claim lock — Review all caveats, TT_lite scope, tri-anchor context, and model-comparison evidence before external claims.
- **ext_003**: TT_lite-inclusive sensitivity sampler or fixed diagnostic — Clarify whether diagnostic TT_lite behavior changes the production posterior story.
- **ext_004**: Best-fit optimizer check at/near posterior summary — Avoid overinterpreting chain MAP-like rows as optimizer outputs.

## Stage 3B-12 model-comparison scope snapshot

# Stage 3B-12 model-comparison scope note

The production posterior is a DEU full-objective posterior. It is not by itself a Bayes factor, evidence calculation, or sampled native/LambdaCDM comparison.

## Baseline/native context rows

| Context | Bundle | Metric | Value | Interpretation |
|---|---|---|---:|---|
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_baseline | -118.7767874187623 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_same_shape | -109.63734343550323 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_baseline | -114.7542343348315 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_same_shape | -105.83758406300996 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_baseline | -110.92316996822484 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_same_shape | -101.24186769892259 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_baseline | -62.564861832602006 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_same_shape | -55.80310943666697 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_baseline | -4.022553083930789 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_same_shape | -3.7997593724932406 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_baseline | -3.831064366606739 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_same_shape | -4.595716364087423 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_baseline | -118.7767874187623 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_same_shape | -109.63734343550323 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_baseline | -114.7542343348315 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_same_shape | -105.83758406300996 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_baseline | -110.92316996822484 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_same_shape | -101.24186769892259 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_baseline | -62.564861832602006 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| stage3a_fixed_regression_gap | None | final_profile2_minus_native_same_shape | -55.80310943666697 | diagnostic loglike gap/context only; not a Bayes factor or posterior model comparison |
| model_comparison_scope | production_full_objective | posterior_scope | None | Production posterior samples the DEU full-objective configuration; it is not a sampled native/LambdaCDM posterior comparison. |
| tri_anchor_decision_scope | primary_objectives | MIXED_PRIMARY_TIEBREAK_RECORDED | None | Primary objectives remain split; prefer the full-objective anchor for full Planck work and preserve a tri-anchor ledger. |

## Scope rule

Native/baseline numbers may be used to explain diagnostic trajectory and motivation. They must not be stated as posterior odds, Bayes factors, or final model-comparison evidence unless a later explicit comparison stage books that claim.
