# Public verification commands

```bash
git clone <PUBLIC_GITHUB_URL>
cd CLASS-DEU
git checkout <BOOKED_STAGE3B40_TAG>
sha256sum -c deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_sha256_manifest.csv  # adapt if using CSV parser
source ~/deu_class/deu_boltzmann_start/.venv/bin/activate
export COBAYA_PACKAGES_PATH=~/deu_class/cobaya_packages
python deu_validation/stage3b_40_github_public_verification_release.py
```

For exact reproduction of MCMC chains, use the booked Stage 3B production/native execution YAML files and the command logs in the artifact manifest.