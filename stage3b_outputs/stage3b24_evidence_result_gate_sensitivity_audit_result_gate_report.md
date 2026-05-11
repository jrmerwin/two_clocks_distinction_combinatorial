# Stage 3B-24 evidence-result gate and sensitivity audit

Generated UTC: `2026-05-09T04:40:09+00:00`

This stage audits the Stage 3B-23 matched diagnostic evidence proxy. It does not launch MCMC and does not compute new evidence.

## Decision

Decision type: `EVIDENCE_RESULT_SENSITIVITY_AUDIT_PASS_PROXY_ONLY_FORMAL_CLAIMS_STILL_GATED`

Recommendation: Book Stage 3B-24. Proxy-only evidence-result language is allowed with caveats; formal Bayes-factor, model-superiority, and final publication claims remain gated.

Next-stage hint: `Stage 3B-25 formal evidence-estimator cross-check or publication-claim lock preflight`

## Proxy result summary

| Quantity | Value | Claim status |
|---|---:|---|
| deu_log_evidence_proxy | -576.0487181 | diagnostic_proxy_only_not_formal_evidence |
| native_log_evidence_proxy | -734.8127652 | diagnostic_proxy_only_not_formal_evidence |
| log_bayes_factor_proxy_deu_minus_native | 158.7640471 | proxy_result_may_be_reported_only_with_proxy_caveat |

## Allowed proxy-only statements

- A matched diagnostic evidence proxy was recorded, with log-BF-proxy direction positive for DEU. Caveat: Call it a diagnostic proxy, not a Bayes factor or final evidence.
- The Stage 3B-23 proxy robustness gate passed and Stage 3B-24 audited the result. Caveat: Robustness here is internal to the diagnostic proxy estimator.
- The scoped, caveated DEU/native posterior comparison remains allowed. Caveat: Do not convert descriptive posterior differences into model evidence.

## Blocked claims

- Do not call the diagnostic proxy value a formal Bayes factor. Required unlock: Run and book a formal evidence estimator or independent cross-check with an explicit claim gate.
- Do not claim DEU is superior to native/baseline from the proxy alone. Required unlock: Pass a model-selection claim gate with validated evidence methodology.
- Do not claim TT_lite was included in the sampled posterior or evidence comparison. Required unlock: Run a matched sampler/evidence design that explicitly includes TT_lite.
- Do not make final publication-style claims from this proxy audit. Required unlock: Book a publication-claim lock after formal evidence and external robustness stages.

## Claim lock

Formal Bayes-factor/evidence claims, model-superiority claims, TT_lite sampled-posterior/evidence claims, and final publication-style claims remain blocked.
