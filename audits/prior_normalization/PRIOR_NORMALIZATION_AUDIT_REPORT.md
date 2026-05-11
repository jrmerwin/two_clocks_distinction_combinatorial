# Stage C1 prior-normalization audit

Repo root: `/home/merwijas/deu_class/CLASS-DEU`
Output: `/home/merwijas/deu_class/CLASS-DEU/audit_prior_norm/20260510T213740Z`

## Why this audit was run

The native-vs-native null test passed strongly, but the reconstructed DEU/native full-covariance logBF was 147.2511216 whereas the official Stage 3B-26 value was 158.7640471.
The difference is 11.5129255, which equals ln(100000), the density of the two DEU-only priors beta width 0.002 and p_vis width 0.005.

## Headline full-covariance variants

- Standard posterior-Laplace DEU logZ: `-606.8986151`
- Standard posterior-Laplace native logZ: `-754.1497367`
- Standard posterior-Laplace logBF: `147.2511216`

- Posterior-plus-prior-again DEU logZ: `-576.0487181`
- Posterior-plus-prior-again native logZ: `-734.8127657`
- Posterior-plus-prior-again logBF: `158.7640476`

## Prior-density constants

- DEU log prior density at MAP: `30.849897`
- Native log prior density at MAP: `19.336971`
- Difference DEU-native: `11.512926`
- Expected ln[1/(0.002*0.005)]: `11.51292546`
- Difference minus expected: `5.350297716e-07`

## Official Stage 3B-26 match

- Best-matching official variant: `posterior_plus_prior_again_laplace` under `full_covariance_laplace`
- Official estimator id: `formal_laplace_full_covariance_crosscheck`
- Official logBF: `158.7640471`
- Best-variant logBF: `158.7640476`
- Official minus variant logBF: `-5.279709967e-07`
- Total absolute logZ mismatch: `5.279709967e-07`

## Interpretation

- If the best match is `posterior_plus_prior_again_laplace`, then the official formal estimator is offset from the standard posterior-Laplace reconstruction by an extra application of the uniform prior-density constants.
- The native-vs-native null can still pass under such a convention because identical native splits carry the same prior constant.
- The DEU/native comparison is affected because DEU has two additional narrow priors, beta and p_vis.
- This does not erase the large likelihood/posterior separation, but it means the official 158.764 value should not be cited as a final Bayes factor without resolving prior accounting.

## Manuscript-safe wording after this audit

Use: `The chain-local estimator passes native-vs-native null checks, but the formal Stage 3B-26 value differs from a standard posterior-Laplace reconstruction by exactly the DEU-only prior-density factor. We therefore report the evidence line as an internal diagnostic pending prior-normalization and full-likelihood ablation.`

Avoid: `The final Bayes factor is 158.764.`
