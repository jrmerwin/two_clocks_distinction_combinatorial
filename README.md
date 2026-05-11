# Boltzmann follow-up verification capsule: DEU graph-index branch

This folder contains the follow-up Boltzmann/Cobaya audit artifacts for the
DEU graph-index amplitude branch.

Central audited claim:

- Exact graph index:
  A_G = 41/40 = 1.025
- Measured posterior branch:
  A_planck = 1.02505572438
- Continuum-normalized branch:
  A = 1.0

Stage I shows that exact 41/40 occupies the same DEU CMB basin as the measured
posterior branch and remains strongly separated from the continuum branch.

Headline Stage I values:

- logBF[41/40 - 1.02505572438] ≈ 0.0696
- logBF[41/40 - 1] ≈ 511.46
- mean chi2 gap [A=1 minus A=41/40] ≈ 1017.35
- high-l TTTEEE_lite chi2 gap [A=1 minus A=41/40] ≈ 978.32

Stage H independently compares the measured graph branch A=1.02505572438
against A=1 inside DEU.

This folder also includes the focused chain/prior audit, prior-normalization
audit, native-vs-native sanity check, full-Plik point-evaluation audit,
full-Plik nuisance-profile audit, A_planck=1 profile audit, broad-A profile
audit, and original production/native chain inputs.

Scope:

- Author-led public verification artifacts.
- Not peer-reviewed confirmation.
- Chain-local posterior-Laplace diagnostics are reported as internal audit
  diagnostics, not as final publication-grade marginal likelihoods.
- DEU/native model-superiority claims are not the headline here.
- The central result is DEU-internal graph-index branch closure.
