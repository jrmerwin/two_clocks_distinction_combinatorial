# Stage 3B-22 evidence estimator execution plan

No estimator is launched by Stage 3B-22. The next execution stage should choose one of the following paths:

## Preferred path: matched nested/evidence run

- Use the DEU production likelihood set and priors from the evidence input manifest.
- Use the native/baseline likelihood set and matched shared priors from the evidence input manifest.
- Report log-evidence estimates and numerical uncertainties for both sides.
- Do not include TT_lite unless both sides are rebuilt with TT_lite explicitly in the sampled likelihood.

## Secondary path: bridge estimator over readiness-cleared chains

- Validate bridge-estimator assumptions separately.
- Treat any bridge output as provisional until uncertainty/stability checks are booked.

## Blocked shortcuts

- Do not treat reference loglike deltas as Bayes factors.
- Do not treat AIC/BIC-like context as model evidence unless explicitly framed as descriptive only.
- Do not make final-publication claims from this setup stage.
