# Stage 3B-34 reproducibility commands

These commands define the minimum command context for an independent replication reviewer.

```bash
cd ~/deu_class/CLASS-DEU
source ~/deu_class/deu_boltzmann_start/.venv/bin/activate
export COBAYA_PACKAGES_PATH=~/deu_class/cobaya_packages
git status --short
git tag --points-at HEAD
python deu_validation/stage3b_33_external_evidence_publication_claim_lock_addendum.py
python deu_validation/stage3b_34_publication_grade_replication_preflight.py
```

A publication-grade replication reviewer must also independently rerun or recompute the evidence validation path; reading archived outputs alone is not sufficient for external/final claims.
