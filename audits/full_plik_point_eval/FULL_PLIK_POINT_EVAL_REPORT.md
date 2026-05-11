# Stage D full-Plik point-evaluate audit

Repo root: `/home/merwijas/deu_class/CLASS-DEU`
Output: `/home/merwijas/deu_class/CLASS-DEU/audit_full_plik_point_eval/20260510T222827Z`

## Scope

This is a paired point-evaluation audit, not MCMC and not evidence.
It re-evaluates DEU/native MAP and posterior-mean points under the existing `TTTEEE_lite` setup and under a full `TTTEEE` replacement.

## Evaluate results

- **deu / lite / map** exit=`0` chain=`audit_full_plik_point_eval/20260510T222827Z/deu_lite_map.1.txt`
  - `minuslogpost` = 572.97188
  - `minuslogprior` = -30.849897
  - `chi2` = 1207.6436
  - `chi2__CMB` = 1207.6436
  - `chi2__planck_2018_highl_plik.TTTEEE_lite` = 764.41175
  - `chi2__planck_2018_lowl.TT` = 26.588767
  - `chi2__planck_2018_lowl.EE` = 397.8372
  - `chi2__planck_2018_lensing.native` = 18.805833
- **deu / full / map** exit=`0` chain=`audit_full_plik_point_eval/20260510T222827Z/deu_full_map.1.txt`
  - `minuslogpost` = 1566.6086
  - `minuslogprior` = -0.59648932
  - `chi2` = 3134.4102
  - `chi2__CMB` = 3134.4102
  - `chi2__planck_2018_highl_plik.TTTEEE` = 2691.1784
  - `chi2__planck_2018_lowl.TT` = 26.588767
  - `chi2__planck_2018_lowl.EE` = 397.8372
  - `chi2__planck_2018_lensing.native` = 18.805833
- **deu / lite / mean** exit=`0` chain=`audit_full_plik_point_eval/20260510T222827Z/deu_lite_mean.1.txt`
  - `minuslogpost` = 573.04212
  - `minuslogprior` = -30.849897
  - `chi2` = 1207.784
  - `chi2__CMB` = 1207.784
  - `chi2__planck_2018_highl_plik.TTTEEE_lite` = 764.53672
  - `chi2__planck_2018_lowl.TT` = 26.50205
  - `chi2__planck_2018_lowl.EE` = 397.87563
  - `chi2__planck_2018_lensing.native` = 18.869631
- **deu / full / mean** exit=`0` chain=`audit_full_plik_point_eval/20260510T222827Z/deu_full_mean.1.txt`
  - `minuslogpost` = 2148.3964
  - `minuslogprior` = 10.197576
  - `chi2` = 4276.3977
  - `chi2__CMB` = 4276.3977
  - `chi2__planck_2018_highl_plik.TTTEEE` = 3833.1504
  - `chi2__planck_2018_lowl.TT` = 26.50205
  - `chi2__planck_2018_lowl.EE` = 397.87563
  - `chi2__planck_2018_lensing.native` = 18.869631
- **native / lite / map** exit=`0` chain=`audit_full_plik_point_eval/20260510T222827Z/native_lite_map.1.txt`
  - `minuslogpost` = 729.78807
  - `minuslogprior` = -19.336971
  - `chi2` = 1498.2501
  - `chi2__CMB` = 1498.2501
  - `chi2__planck_2018_highl_plik.TTTEEE_lite` = 1066.52
  - `chi2__planck_2018_lowl.TT` = 19.775841
  - `chi2__planck_2018_lowl.EE` = 395.99407
  - `chi2__planck_2018_lensing.native` = 15.960124
- **native / full / map** exit=`0` chain=`audit_full_plik_point_eval/20260510T222827Z/native_full_map.1.txt`
  - `minuslogpost` = 1979.1186
  - `minuslogprior` = 19.652777
  - `chi2` = 3918.9317
  - `chi2__CMB` = 3918.9317
  - `chi2__planck_2018_highl_plik.TTTEEE` = 3487.2017
  - `chi2__planck_2018_lowl.TT` = 19.775841
  - `chi2__planck_2018_lowl.EE` = 395.99407
  - `chi2__planck_2018_lensing.native` = 15.960124
- **native / lite / mean** exit=`0` chain=`audit_full_plik_point_eval/20260510T222827Z/native_lite_mean.1.txt`
  - `minuslogpost` = 732.0476
  - `minuslogprior` = -19.336971
  - `chi2` = 1502.7692
  - `chi2__CMB` = 1502.7692
  - `chi2__planck_2018_highl_plik.TTTEEE_lite` = 1071.12
  - `chi2__planck_2018_lowl.TT` = 19.78351
  - `chi2__planck_2018_lowl.EE` = 395.96794
  - `chi2__planck_2018_lensing.native` = 15.89767
- **native / full / mean** exit=`0` chain=`audit_full_plik_point_eval/20260510T222827Z/native_full_mean.1.txt`
  - `minuslogpost` = 2103.6874
  - `minuslogprior` = 17.40804
  - `chi2` = 4172.5587
  - `chi2__CMB` = 4172.5587
  - `chi2__planck_2018_highl_plik.TTTEEE` = 3740.9096
  - `chi2__planck_2018_lowl.TT` = 19.78351
  - `chi2__planck_2018_lowl.EE` = 395.96794
  - `chi2__planck_2018_lensing.native` = 15.89767

## Pairwise native-minus-DEU deltas

- **lite / map**
  - `native_minus_deu_chi2` = 290.60649999999987
  - `native_minus_deu_chi2__CMB` = 290.60649999999987
  - `native_minus_deu_chi2__planck_2018_highl_plik.TTTEEE_lite` = 302.10825
  - `native_minus_deu_chi2__planck_2018_lensing.native` = -2.8457089999999994
  - `native_minus_deu_chi2__planck_2018_lowl.EE` = -1.8431299999999737
  - `native_minus_deu_chi2__planck_2018_lowl.TT` = -6.812926000000001
  - `native_minus_deu_minuslogpost` = 156.8161899999999
  - `native_minus_deu_minuslogprior` = 11.512926
- **full / map**
  - `native_minus_deu_chi2` = 784.5215000000003
  - `native_minus_deu_chi2__CMB` = 784.5215000000003
  - `native_minus_deu_chi2__planck_2018_highl_plik.TTTEEE` = 796.0233000000003
  - `native_minus_deu_chi2__planck_2018_lensing.native` = -2.8457089999999994
  - `native_minus_deu_chi2__planck_2018_lowl.EE` = -1.8431299999999737
  - `native_minus_deu_chi2__planck_2018_lowl.TT` = -6.812926000000001
  - `native_minus_deu_minuslogpost` = 412.51
  - `native_minus_deu_minuslogprior` = 20.24926632
- **lite / mean**
  - `native_minus_deu_chi2` = 294.98519999999985
  - `native_minus_deu_chi2__CMB` = 294.98519999999985
  - `native_minus_deu_chi2__planck_2018_highl_plik.TTTEEE_lite` = 306.58327999999995
  - `native_minus_deu_chi2__planck_2018_lensing.native` = -2.9719609999999985
  - `native_minus_deu_chi2__planck_2018_lowl.EE` = -1.9076900000000023
  - `native_minus_deu_chi2__planck_2018_lowl.TT` = -6.718540000000001
  - `native_minus_deu_minuslogpost` = 159.00548000000003
  - `native_minus_deu_minuslogprior` = 11.512926
- **full / mean**
  - `native_minus_deu_chi2` = -103.83900000000085
  - `native_minus_deu_chi2__CMB` = -103.83900000000085
  - `native_minus_deu_chi2__planck_2018_highl_plik.TTTEEE` = -92.24080000000004
  - `native_minus_deu_chi2__planck_2018_lensing.native` = -2.9719609999999985
  - `native_minus_deu_chi2__planck_2018_lowl.EE` = -1.9076900000000023
  - `native_minus_deu_chi2__planck_2018_lowl.TT` = -6.718540000000001
  - `native_minus_deu_minuslogpost` = -44.70900000000029
  - `native_minus_deu_minuslogprior` = 7.210464

## Decision guide

- First check that `lite / map` reproduces the old chain MAP minuslogpost values near DEU `572.83932` and native `729.84925`.
- If the lite re-evaluation does not reproduce the chain values, the evaluate configs are not equivalent and the full-Plik result should not be interpreted.
- If full Plik fails, paste the failure tails; likely causes are missing `clik` support or missing full-Plik nuisance parameter references.
- If full Plik succeeds and the native-minus-DEU high-l gap remains of order hundreds in chi2, the separation is not merely a `TTTEEE_lite` compression artifact.
- If full Plik shrinks the high-l gap to ordinary size, the old evidence line should be treated as a `TTTEEE_lite`/nuisance-marginalization artifact.
- Even a successful full-Plik point evaluation does not replace full-Plik MCMC or a true evidence calculation.
