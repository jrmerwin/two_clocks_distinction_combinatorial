# Stage 3B-11 caveat check

The Stage 3B-10 caveats are retained as active constraints:

- This is the first posterior-language summary after the Stage 3B-9 readiness gate, not a final publication claim.
- The sampled posterior is for the DEU full-objective working-lock configuration and the likelihood set used in the production YAML.
- The TT_lite likelihood remains excluded from the production sampler by the Stage 3B preflight design; TT_lite stays a monitoring/diagnostic object, not part of the sampled full-objective posterior.
- The tri-anchor split is retained as context: high-l, lowl+TTTEEE, and full-objective anchors are monitored even though the full-objective working lock is used for the production posterior.
- The readiness gate passing means this summary is allowed to be written; it does not by itself establish external robustness, model comparison, or a final cosmological result.
- Any scientific claim beyond this internal posterior summary still needs the next booked robustness/comparison stage.

Stage 3B-11 adds robustness/comparison checks, but still does not allow final publication claims.