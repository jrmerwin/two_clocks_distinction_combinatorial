# Stage 3B-15 matched native/baseline comparison preflight scope

Generated UTC: `2026-05-09T01:10:50+00:00`

This stage preflights a native/baseline comparison scaffold. It does not launch MCMC.

Decision: `MATCHED_NATIVE_BASELINE_PREFLIGHT_PASS_SUPERIORITY_STILL_GATED`

## Allowed scoped claims

- A caveated DEU full-objective posterior summary has been produced after readiness and robustness gates. Caveat: Internal staged result; not final publication claim.
- The native/baseline comparison scaffold has been preflighted. Caveat: Preflight only; no native baseline sampler was launched by this stage.
- TT_lite was monitored diagnostically but excluded from production posterior likelihood. Caveat: Do not describe TT_lite as sampled likelihood context.

## Blocked claims

- DEU is superior to native/baseline cosmology — No matched native/baseline posterior or evidence comparison has been booked.
- Bayes factor/evidence favors DEU — Current chain summaries are posterior samples, not evidence estimates.
- TT_lite is included in the production posterior — TT_lite remained diagnostic-only and excluded from production likelihood.
- Final publication-style cosmological result — Stage 3B-14 and 3B-13 keep final claims gated.

## Required follow-up extensions

- `matched_native_baseline_sampler`: Generate native/baseline posterior samples with the matched full-objective likelihood family.
- `explicit_model_evidence_or_information_criterion_plan`: Define a valid model-comparison statistic before superiority claims.
- `tt_lite_inclusive_sampler_optional`: If TT_lite production claims are desired, run a sampler that actually includes TT_lite.
