# Stage F A_planck=1 profile audit

Repo root: `/home/merwijas/deu_class/CLASS-DEU`
Output: `/home/merwijas/deu_class/CLASS-DEU/audit_Aplanck_fixed1_profile/20260510T235207Z`

## Scope

This audit fixes `A_planck = 1.0` in both DEU and native configurations.
It profiles the remaining free parameters under both `TTTEEE_lite` and full `TTTEEE`, using posterior-profile and likelihood-profile objectives.
It is not MCMC and not evidence.

The purpose is to test whether the large DEU/native separation depends on the non-unity sampled `A_planck` window.

## Results

- **deu / lite / posterior_profile** exit=`0` result=`audit_Aplanck_fixed1_profile/20260510T235207Z/deu_lite_Aplanck1_posterior_profile.minimum.txt`
  - `minuslogpost` = 1082.5691
  - `minuslogprior` = -26.244727
  - `chi2` = 2217.6277
  - `chi2__CMB` = 2217.6277
  - `chi2__planck_2018_highl_plik.TTTEEE_lite` = 1735.4748
  - `chi2__planck_2018_lowl.TT` = 32.468787
  - `chi2__planck_2018_lowl.EE` = 397.88703
  - `chi2__planck_2018_lensing.native` = 51.797056
  - `deu_damping_envelope_beta` = 0.0305
  - `deu_transfer_polamp_p_vis` = 1.045
  - `omega_b` = 0.0221
  - `n_s` = 0.9805
- **deu / lite / likelihood_profile** exit=`0` result=`audit_Aplanck_fixed1_profile/20260510T235207Z/deu_lite_Aplanck1_likelihood_profile.bestfit.txt`
  - `minuslogpost` = 1082.5691
  - `minuslogprior` = -26.244727
  - `chi2` = 2217.6277
  - `chi2__CMB` = 2217.6277
  - `chi2__planck_2018_highl_plik.TTTEEE_lite` = 1735.4748
  - `chi2__planck_2018_lowl.TT` = 32.468787
  - `chi2__planck_2018_lowl.EE` = 397.88703
  - `chi2__planck_2018_lensing.native` = 51.797056
  - `deu_damping_envelope_beta` = 0.0305
  - `deu_transfer_polamp_p_vis` = 1.045
  - `omega_b` = 0.0221
  - `n_s` = 0.9805
- **deu / full / posterior_profile** exit=`0` result=`audit_Aplanck_fixed1_profile/20260510T235207Z/deu_full_Aplanck1_posterior_profile.minimum.txt`
  - `minuslogpost` = 2024.1272
  - `minuslogprior` = 23.714795
  - `chi2` = 4000.8248
  - `chi2__CMB` = 4000.8248
  - `chi2__planck_2018_highl_plik.TTTEEE` = 3518.6719
  - `chi2__planck_2018_lowl.TT` = 32.468787
  - `chi2__planck_2018_lowl.EE` = 397.88703
  - `chi2__planck_2018_lensing.native` = 51.797056
  - `deu_damping_envelope_beta` = 0.0305
  - `deu_transfer_polamp_p_vis` = 1.045
  - `omega_b` = 0.0221
  - `n_s` = 0.9805
- **deu / full / likelihood_profile** exit=`0` result=`audit_Aplanck_fixed1_profile/20260510T235207Z/deu_full_Aplanck1_likelihood_profile.bestfit.txt`
  - `minuslogpost` = 2051.6925
  - `minuslogprior` = 62.572789
  - `chi2` = 3978.2394
  - `chi2__CMB` = 3978.2394
  - `chi2__planck_2018_highl_plik.TTTEEE` = 3496.0892
  - `chi2__planck_2018_lowl.TT` = 32.468428
  - `chi2__planck_2018_lowl.EE` = 397.88703
  - `chi2__planck_2018_lensing.native` = 51.794714
  - `deu_damping_envelope_beta` = 0.0305
  - `deu_transfer_polamp_p_vis` = 1.045
  - `omega_b` = 0.022099888
  - `n_s` = 0.9805
- **native / lite / posterior_profile** exit=`0` result=`audit_Aplanck_fixed1_profile/20260510T235207Z/native_lite_Aplanck1_posterior_profile.minimum.txt`
  - `minuslogpost` = 518.54581
  - `minuslogprior` = -14.731801
  - `chi2` = 1066.5552
  - `chi2__CMB` = 1066.5552
  - `chi2__planck_2018_highl_plik.TTTEEE_lite` = 638.85002
  - `chi2__planck_2018_lowl.TT` = 20.842013
  - `chi2__planck_2018_lowl.EE` = 396.02782
  - `chi2__planck_2018_lensing.native` = 10.83536
  - `omega_b` = 0.02208743
  - `n_s` = 0.9805
- **native / lite / likelihood_profile** exit=`0` result=`audit_Aplanck_fixed1_profile/20260510T235207Z/native_lite_Aplanck1_likelihood_profile.bestfit.txt`
  - `minuslogpost` = 518.55467
  - `minuslogprior` = -14.731801
  - `chi2` = 1066.5729
  - `chi2__CMB` = 1066.5729
  - `chi2__planck_2018_highl_plik.TTTEEE_lite` = 638.85629
  - `chi2__planck_2018_lowl.TT` = 20.841493
  - `chi2__planck_2018_lowl.EE` = 396.03674
  - `chi2__planck_2018_lensing.native` = 10.838419
  - `omega_b` = 0.0220808
  - `n_s` = 0.9805
- **native / full / posterior_profile** exit=`0` result=`audit_Aplanck_fixed1_profile/20260510T235207Z/native_full_Aplanck1_posterior_profile.minimum.txt`
  - `minuslogpost` = 1422.591
  - `minuslogprior` = 11.315939
  - `chi2` = 2822.5501
  - `chi2__CMB` = 2822.5501
  - `chi2__planck_2018_highl_plik.TTTEEE` = 2394.8492
  - `chi2__planck_2018_lowl.TT` = 20.843215
  - `chi2__planck_2018_lowl.EE` = 396.02782
  - `chi2__planck_2018_lensing.native` = 10.829802
  - `omega_b` = 0.0221
  - `n_s` = 0.9805
- **native / full / likelihood_profile** exit=`0` result=`audit_Aplanck_fixed1_profile/20260510T235207Z/native_full_Aplanck1_likelihood_profile.bestfit.txt`
  - `minuslogpost` = 1480.848
  - `minuslogprior` = 71.477995
  - `chi2` = 2818.7401
  - `chi2__CMB` = 2818.7401
  - `chi2__planck_2018_highl_plik.TTTEEE` = 2391.0393
  - `chi2__planck_2018_lowl.TT` = 20.843215
  - `chi2__planck_2018_lowl.EE` = 396.02782
  - `chi2__planck_2018_lensing.native` = 10.829802
  - `omega_b` = 0.0221
  - `n_s` = 0.9805

## Pairwise native-minus-DEU deltas

- **lite / posterior_profile / A_planck=1**
  - `native_minus_deu_chi2` = -1151.0725
  - `native_minus_deu_chi2__CMB` = -1151.0725
  - `native_minus_deu_chi2__planck_2018_highl_plik.TTTEEE_lite` = -1096.62478
  - `native_minus_deu_chi2__planck_2018_lensing.native` = -40.961695999999996
  - `native_minus_deu_chi2__planck_2018_lowl.EE` = -1.8592099999999618
  - `native_minus_deu_chi2__planck_2018_lowl.TT` = -11.626773999999997
  - `native_minus_deu_minuslogpost` = -564.02329
  - `native_minus_deu_minuslogprior` = 11.512926
- **lite / likelihood_profile / A_planck=1**
  - `native_minus_deu_chi2` = -1151.0548000000001
  - `native_minus_deu_chi2__CMB` = -1151.0548000000001
  - `native_minus_deu_chi2__planck_2018_highl_plik.TTTEEE_lite` = -1096.61851
  - `native_minus_deu_chi2__planck_2018_lensing.native` = -40.958636999999996
  - `native_minus_deu_chi2__planck_2018_lowl.EE` = -1.8502899999999727
  - `native_minus_deu_chi2__planck_2018_lowl.TT` = -11.627294
  - `native_minus_deu_minuslogpost` = -564.01443
  - `native_minus_deu_minuslogprior` = 11.512926
- **full / posterior_profile / A_planck=1**
  - `native_minus_deu_chi2` = -1178.2747
  - `native_minus_deu_chi2__CMB` = -1178.2747
  - `native_minus_deu_chi2__planck_2018_highl_plik.TTTEEE` = -1123.8226999999997
  - `native_minus_deu_chi2__planck_2018_lensing.native` = -40.967254
  - `native_minus_deu_chi2__planck_2018_lowl.EE` = -1.8592099999999618
  - `native_minus_deu_chi2__planck_2018_lowl.TT` = -11.625571999999998
  - `native_minus_deu_minuslogpost` = -601.5362
  - `native_minus_deu_minuslogprior` = -12.398855999999999
- **full / likelihood_profile / A_planck=1**
  - `native_minus_deu_chi2` = -1159.4993
  - `native_minus_deu_chi2__CMB` = -1159.4993
  - `native_minus_deu_chi2__planck_2018_highl_plik.TTTEEE` = -1105.0499
  - `native_minus_deu_chi2__planck_2018_lensing.native` = -40.964912
  - `native_minus_deu_chi2__planck_2018_lowl.EE` = -1.8592099999999618
  - `native_minus_deu_chi2__planck_2018_lowl.TT` = -11.625213000000002
  - `native_minus_deu_minuslogpost` = -570.8445000000002
  - `native_minus_deu_minuslogprior` = 8.905206000000007

## Decision guide

- If DEU still wins by a large high-l `chi2` gap with `A_planck=1`, the high-l advantage is not simply an `A_planck≈1.025` amplitude artifact.
- If the DEU/native gap collapses when `A_planck=1`, the current comparison depends strongly on the non-unity calibration window and the manuscript must treat `A_planck` as a central unresolved issue.
- If full `TTTEEE` and `TTTEEE_lite` disagree sharply, a full posterior run is needed before any high-l conclusion.
- Passing this audit still does not solve the restricted-native-baseline issue; it only addresses the most direct `A_planck` criticism.
- The next step after this is either a broad-`A_planck` profile/MCMC branch or a less restricted native baseline.
