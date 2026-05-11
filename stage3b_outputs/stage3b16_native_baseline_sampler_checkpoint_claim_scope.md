# Stage 3B-16 native/baseline sampler checkpoint claim scope

This stage launches the matched native/baseline sampler checkpoint and audits the resulting chain file.
It is not a model-superiority result and it does not permit final publication-style claims.

Allowed:

- State that a native/baseline sampler checkpoint was run and audited.
- State whether the native checkpoint chain had finite values, expected sampled columns, prior-bound compliance, and sampled-parameter motion.
- Compare native reference reproducibility to the Stage 3B-15 native sampler reference.

Blocked:

- Do not claim DEU is superior to native/baseline from this checkpoint alone.
- Do not claim Bayes-factor/evidence superiority.
- Do not claim final publication readiness.
- Do not claim TT_lite is included in the sampled native or DEU production likelihood.

Decision type: `MATCHED_NATIVE_BASELINE_SAMPLER_CHECKPOINT_PASS_SUPERIORITY_STILL_GATED`
Next-stage hint: `Stage 3B-17 native/baseline readiness and matched comparison gate`
