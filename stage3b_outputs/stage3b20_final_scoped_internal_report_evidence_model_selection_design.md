# Stage 3B-20 evidence/model-selection design note

This design note records what remains required before any model-superiority, Bayes-factor/evidence, or final publication-style claim can be made.

| Step | Purpose | Blocks |
|---|---|---|
| Define explicit model-selection criterion | Choose evidence/Bayes-factor, predictive scoring, information criterion, or scoped non-superiority report path. | model-superiority claims |
| Prepare matched evidence/model-selection configs | Ensure DEU and native/baseline are compared under matched likelihood, nuisance, prior, and sampling assumptions. | evidence or Bayes-factor claims |
| Decide whether TT_lite enters a later sampled likelihood | Current production posterior excludes TT_lite; any TT_lite posterior claim requires a new sampler stage. | TT_lite-in-posterior claims |
| Run publication-style external robustness preflight | Assess sensitivity to data choices, priors, chain length, and external validation before public claims. | final publication-style claims |

No evidence calculation is performed by Stage 3B-20. The current DEU/native comparison remains descriptive.
