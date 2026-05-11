#!/usr/bin/env bash
set -euo pipefail
cd ~/deu_class/CLASS-DEU
source ~/deu_class/deu_boltzmann_start/.venv/bin/activate
export COBAYA_PACKAGES_PATH=~/deu_class/cobaya_packages

# Stage 3B-6 wrote this production config, but did not run it.
# Run only after Stage 3B-6 is booked and git status is clean.
cobaya-run /home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b6_production_preflight_production_sampler.yaml
