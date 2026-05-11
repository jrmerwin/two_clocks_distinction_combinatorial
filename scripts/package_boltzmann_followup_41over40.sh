#!/usr/bin/env bash
set -euo pipefail

CLASS_ROOT="${CLASS_DEU_ROOT:-$HOME/deu_class/CLASS-DEU}"

# Set BOLTZ_OUT to your GitHub repo location if needed, for example:
# export BOLTZ_OUT=/mnt/c/Users/<YOU>/path/to/github_repo/public_verification/boltzmann_followup_41over40
OUT="${BOLTZ_OUT:-$CLASS_ROOT/public_verification/boltzmann_followup_41over40}"

mkdir -p "$OUT"/{checksums,environment,production_inputs/deu_original,production_inputs/native_original,audits,derived_tables,scripts}

echo "[package] CLASS_ROOT=$CLASS_ROOT"
echo "[package] OUT=$OUT"

copy_file() {
  local src="$1"
  local dst="$2"
  if [ -f "$src" ]; then
    mkdir -p "$(dirname "$dst")"
    cp -a "$src" "$dst"
    echo "[copy] $src -> $dst"
  else
    echo "[warn] missing file: $src" >&2
  fi
}

copy_glob() {
  local pattern="$1"
  local dst_dir="$2"
  mkdir -p "$dst_dir"
  shopt -s nullglob
  local files=( $pattern )
  shopt -u nullglob
  if [ "${#files[@]}" -eq 0 ]; then
    echo "[warn] no matches: $pattern" >&2
    return 0
  fi
  for f in "${files[@]}"; do
    cp -a "$f" "$dst_dir/"
    echo "[copy] $f -> $dst_dir/"
  done
}

copy_latest_dir() {
  local src_base="$1"
  local dst_subdir="$2"
  local latest="$CLASS_ROOT/$src_base/latest"

  if [ ! -e "$latest" ]; then
    echo "[warn] missing latest link/dir: $latest" >&2
    return 0
  fi

  local resolved
  resolved="$(readlink -f "$latest")"

  if [ ! -d "$resolved" ]; then
    echo "[warn] latest does not resolve to directory: $latest -> $resolved" >&2
    return 0
  fi

  mkdir -p "$OUT/$dst_subdir"
  rsync -a --copy-links "$resolved/" "$OUT/$dst_subdir/"
  echo "[copy-dir] $resolved -> $OUT/$dst_subdir/"
}

# -------------------------------------------------------------------
# Environment / provenance
# -------------------------------------------------------------------
(
  cd "$CLASS_ROOT"
  git rev-parse HEAD 2>/dev/null || true
) > "$OUT/environment/git_head.txt"

(
  cd "$CLASS_ROOT"
  git status --short 2>/dev/null || true
) > "$OUT/environment/git_status.txt"

python --version > "$OUT/environment/python_version.txt" 2>&1 || true
pip freeze > "$OUT/environment/pip_freeze.txt" 2>/dev/null || true
uname -a > "$OUT/environment/uname.txt" 2>/dev/null || true
wsl.exe --version > "$OUT/environment/wsl_version.txt" 2>/dev/null || true

# -------------------------------------------------------------------
# Original production/native chain inputs and configs
# -------------------------------------------------------------------
copy_glob "$CLASS_ROOT/deu_validation/stage3b_outputs/chains/stage3b6_first_production_run*.txt" \
          "$OUT/production_inputs/deu_original"
copy_glob "$CLASS_ROOT/deu_validation/stage3b_outputs/chains/stage3b6_first_production_run*.yaml" \
          "$OUT/production_inputs/deu_original"

copy_glob "$CLASS_ROOT/deu_validation/stage3b_outputs/chains/stage3b16_native_baseline_run*.txt" \
          "$OUT/production_inputs/native_original"
copy_glob "$CLASS_ROOT/deu_validation/stage3b_outputs/chains/stage3b16_native_baseline_run*.yaml" \
          "$OUT/production_inputs/native_original"

# -------------------------------------------------------------------
# Follow-up audit folders
# -------------------------------------------------------------------
copy_latest_dir "audit_out/latest_focused/.." "audits/stage_b_focused_chain_prior_audit"
copy_latest_dir "audit_native_null" "audits/native_native_null"
copy_latest_dir "audit_prior_norm" "audits/prior_normalization"
copy_latest_dir "audit_full_plik_point_eval" "audits/full_plik_point_eval"
copy_latest_dir "audit_full_plik_nuisance_profile" "audits/full_plik_nuisance_profile"
copy_latest_dir "audit_Aplanck_fixed1_profile" "audits/Aplanck_fixed1_profile"
copy_latest_dir "audit_Aplanck_broad_profile" "audits/Aplanck_broad_profile"
copy_latest_dir "audit_deu_Aplanck_delta" "audits/deu_Aplanck_delta_stage_H"
copy_latest_dir "audit_deu_Aplanck_exact41over40" "audits/exact_41over40_stage_I"

# -------------------------------------------------------------------
# Derived headline tables copied into one easy-to-find place
# -------------------------------------------------------------------
copy_file "$CLASS_ROOT/audit_deu_Aplanck_exact41over40/latest/deu_Aplanck_exact41over40_chain_summary.csv" \
          "$OUT/derived_tables/stage_i_exact41over40_chain_summary.csv"

copy_file "$CLASS_ROOT/audit_deu_Aplanck_exact41over40/latest/deu_Aplanck_exact41over40_pairwise.csv" \
          "$OUT/derived_tables/stage_i_exact41over40_pairwise.csv"

copy_file "$CLASS_ROOT/audit_deu_Aplanck_delta/latest/deu_Aplanck_delta_pairwise.csv" \
          "$OUT/derived_tables/stage_h_deu_Aplanck_delta_pairwise.csv"

copy_file "$CLASS_ROOT/audit_out/latest_focused/focused_chain_summary.csv" \
          "$OUT/derived_tables/stage_b_focused_chain_summary.csv"

copy_file "$CLASS_ROOT/audit_out/latest_focused/focused_likelihood_scope.csv" \
          "$OUT/derived_tables/stage_b_focused_likelihood_scope.csv"

copy_file "$CLASS_ROOT/audit_out/latest_focused/focused_prior_summary.csv" \
          "$OUT/derived_tables/stage_b_focused_prior_summary.csv"

copy_file "$CLASS_ROOT/audit_prior_norm/latest/prior_normalization_pairwise.csv" \
          "$OUT/derived_tables/prior_normalization_pairwise.csv"

copy_file "$CLASS_ROOT/audit_prior_norm/latest/prior_normalization_official_match.csv" \
          "$OUT/derived_tables/prior_normalization_official_match.csv"

copy_file "$CLASS_ROOT/audit_full_plik_point_eval/latest/full_plik_point_eval_deltas.csv" \
          "$OUT/derived_tables/full_plik_point_eval_deltas.csv"

copy_file "$CLASS_ROOT/audit_full_plik_nuisance_profile/latest/full_plik_nuisance_profile_deltas.csv" \
          "$OUT/derived_tables/full_plik_nuisance_profile_deltas.csv"

copy_file "$CLASS_ROOT/audit_Aplanck_fixed1_profile/latest/Aplanck_fixed1_profile_deltas.csv" \
          "$OUT/derived_tables/Aplanck_fixed1_profile_deltas.csv"

copy_file "$CLASS_ROOT/audit_Aplanck_broad_profile/latest/Aplanck_broad_profile_best_deltas.csv" \
          "$OUT/derived_tables/Aplanck_broad_profile_best_deltas.csv"

# Preserve this script inside the release.
cp -a "$0" "$OUT/scripts/package_boltzmann_followup_41over40.sh"

# -------------------------------------------------------------------
# README
# -------------------------------------------------------------------
cat > "$OUT/README.md" <<'EOF'
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
EOF

# -------------------------------------------------------------------
# Manifest, size report, and checksums
# -------------------------------------------------------------------
(
  cd "$OUT"
  find . -type f | sort | while read -r f; do
    size="$(stat -c%s "$f")"
    printf "%s\t%s\n" "$size" "$f"
  done
) > "$OUT/MANIFEST.tsv"

sort -nr "$OUT/MANIFEST.tsv" > "$OUT/MANIFEST_by_size.tsv"

(
  cd "$OUT"
  find . -type f ! -path "./checksums/*" -print0 \
    | sort -z \
    | xargs -0 sha256sum
) > "$OUT/checksums/SHA256SUMS.txt"

(
  cd "$OUT"
  sha256sum checksums/SHA256SUMS.txt
) > "$OUT/checksums/SHA256SUMS.txt.sha256"

echo
echo "[package] done: $OUT"
echo
echo "[package] largest files:"
head -20 "$OUT/MANIFEST_by_size.tsv"
echo
echo "[package] files over 50 MiB:"
find "$OUT" -type f -size +50M -print || true
echo
echo "[package] files over 100 MiB:"
find "$OUT" -type f -size +100M -print || true
echo
echo "[package] verify checksums with:"
echo "  cd \"$OUT\" && sha256sum -c checksums/SHA256SUMS.txt"
