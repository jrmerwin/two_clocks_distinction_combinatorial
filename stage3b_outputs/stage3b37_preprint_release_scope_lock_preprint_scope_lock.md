# Stage 3B-37 preprint-release scope lock

Generated UTC: `2026-05-09T16:31:17+00:00`

This stage selects an author-led preprint path instead of the external-review intake path.
It does not launch MCMC, execute reviewer commands, or compute new evidence.

## Scope decision

Decision type: `PREPRINT_RELEASE_SCOPE_LOCK_PASS_PUBLICATION_CLAIMS_STILL_GATED`

Recommendation: Book Stage 3B-37 as a preprint-release scope lock. Use only author-led preprint/internal evidence wording with caveats; do not claim external peer review, model superiority, or final publication-grade evidence.

## Evidence lineage allowed for internal/preprint caveated wording

```json
{
  "deu_log_evidence_independent_validation": -542.2974790661433,
  "formal_log_bayes_factor_lineage": 158.76404705020616,
  "log_bayes_factor_independent_validation_deu_minus_native": 169.00640862086107,
  "native_log_evidence_independent_validation": -711.3038876870044,
  "proxy_log_bayes_factor_lineage": 158.76404705020616,
  "source_manifest_key": "handoff_manifest"
}
```

## Allowed preprint statements

- This preprint reports an internally validated DEU posterior analysis and matched native-baseline comparison under the documented Stage 3B pipeline. Caveat: Author-led preprint; not independently peer-reviewed or externally replicated.
- The DEU production posterior is caveated and is based on the full-objective likelihood set used in the production sampler. Caveat: TT_lite was diagnostic-only and was not part of the sampled production likelihood.
- The matched native/baseline comparison is descriptive and readiness-cleared on both sides. Caveat: Descriptive comparison does not by itself establish model superiority.
- An internal independent-validation estimator reported a log-BF-style diagnostic favoring DEU over native within the documented estimator setup. Caveat: This is allowed only as internal estimator language with caveats, not as a peer-reviewed or final Bayes-factor claim.
- The replication package was frozen and checksum-verified for author-led reproducibility and future independent review. Caveat: No external reviewer result has been booked.

## Blocked claims

- Peer-reviewed independent replication has confirmed the result. Reason: No external reviewer result exists; Stage 3B-37 external reviewer intake was intentionally bypassed for a preprint pathway.
- The model is conclusively superior to native/baseline cosmology. Reason: Model-superiority claims remain gated; current evidence language is internal/caveated.
- TT_lite was included in the sampled posterior or evidence likelihood. Reason: TT_lite was diagnostic-only and excluded from the production/native sampled likelihoods.
- The evidence result is final and publication-grade without caveats. Reason: External publication and final-style claims remain blocked.
- External peer review is complete. Reason: The selected path is author-led preprint release, not external reviewer intake.

## Claim lock

External peer-review completion must not be claimed. Model-superiority and final publication-style claims remain blocked.
TT_lite must remain diagnostic-only unless a later sampled/evidence stage explicitly includes it.
