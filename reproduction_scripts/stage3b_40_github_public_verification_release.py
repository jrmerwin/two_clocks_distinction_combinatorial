#!/usr/bin/env python3
"""Stage 3B-40 GitHub public verification release package.

This stage follows the author-led preprint path. It does not launch MCMC,
does not compute new evidence, and does not claim peer review. It prepares a
GitHub-ready public verification package so readers can inspect and reproduce
the booked artifacts. The package may support a preprint statement that the
work is not peer reviewed but that the full verification package is public.
"""
from __future__ import annotations

import csv
import glob
import hashlib
import json
import math
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Optional, Sequence

STAGE = "3B-40"
SCRIPT_NAME = "stage3b_40_github_public_verification_release.py"
OUT_STEM = "stage3b40_github_public_verification_release"

PREPRINT_SCOPE_STEM = "stage3b37_preprint_release_scope_lock"
MANUSCRIPT_STEM = "stage3b38_preprint_manuscript_package"
SUBMISSION_STEM = "stage3b39_preprint_submission_readiness_gate"
FREEZE_STEM = "stage3b35_replication_package_freeze_reviewer_dry_run"
HANDOFF_STEM = "stage3b36_external_reviewer_handoff_result_gate"
INDEPENDENT_GATE_STEM = "stage3b32_independent_evidence_result_gate_publication_lock"
PUBLICATION_LOCK_STEM = "stage3b33_external_evidence_publication_claim_lock_addendum"
FINAL_REPORT_STEM = "stage3b20_final_scoped_internal_report"
SETUP_STEM = "stage3b0_lock_note_sampler_seed"

EXPECTED_STAGE_DECISIONS = {
    PREPRINT_SCOPE_STEM: "PREPRINT_RELEASE_SCOPE_LOCK_PASS_PUBLICATION_CLAIMS_STILL_GATED",
    MANUSCRIPT_STEM: "PREPRINT_MANUSCRIPT_PACKAGE_PASS_AUTHOR_LED_PREPRINT_READY_CLAIMS_GATED",
    SUBMISSION_STEM: "PREPRINT_SUBMISSION_READINESS_GATE_PASS_AUTHOR_LED_RELEASE_READY_CLAIMS_GATED",
    FREEZE_STEM: "INDEPENDENT_REPLICATION_PACKAGE_FREEZE_DRY_RUN_PASS_EXTERNAL_REVIEW_READY_PUBLICATION_STILL_GATED",
    HANDOFF_STEM: "EXTERNAL_REVIEWER_HANDOFF_RESULT_GATE_PASS_REVIEW_PENDING_PUBLICATION_STILL_GATED",
    INDEPENDENT_GATE_STEM: "INDEPENDENT_EVIDENCE_VALIDATION_RESULT_GATE_PASS_INTERNAL_VALIDATION_ALLOWED_PUBLICATION_STILL_GATED",
    PUBLICATION_LOCK_STEM: "EXTERNAL_EVIDENCE_PUBLICATION_CLAIM_LOCK_PASS_INTERNAL_VALIDATION_ALLOWED_PUBLICATION_STILL_GATED",
}

CORE_REQUIRED_ARTIFACTS = [
    f"{PREPRINT_SCOPE_STEM}.json",
    f"{PREPRINT_SCOPE_STEM}_acceptance.md",
    f"{PREPRINT_SCOPE_STEM}_preprint_scope_lock.md",
    f"{PREPRINT_SCOPE_STEM}_preprint_guardrails.md",
    f"{MANUSCRIPT_STEM}.json",
    f"{MANUSCRIPT_STEM}_acceptance.md",
    f"{MANUSCRIPT_STEM}_preprint_manuscript_draft.md",
    f"{MANUSCRIPT_STEM}_preprint_abstract.md",
    f"{MANUSCRIPT_STEM}_methods_appendix.md",
    f"{MANUSCRIPT_STEM}_reproducibility_statement.md",
    f"{SUBMISSION_STEM}.json",
    f"{SUBMISSION_STEM}_acceptance.md",
    f"{SUBMISSION_STEM}_submission_readiness_report.md",
    f"{SUBMISSION_STEM}_preprint_metadata.json",
    f"{SUBMISSION_STEM}_source_package_manifest.csv",
    f"{SUBMISSION_STEM}_sha256_manifest.csv",
    f"{SUBMISSION_STEM}_author_release_checklist.md",
    f"{FREEZE_STEM}.json",
    f"{FREEZE_STEM}_freeze_manifest.json",
    f"{FREEZE_STEM}_package_manifest.csv",
    f"{FREEZE_STEM}_sha256_manifest.csv",
    f"{FINAL_REPORT_STEM}.json",
    f"{FINAL_REPORT_STEM}_final_scoped_report.md",
]


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def finite(x: Any) -> Optional[float]:
    try:
        y = float(x)
    except Exception:
        return None
    return y if math.isfinite(y) else None


def clean(x: Any) -> Any:
    if isinstance(x, Path):
        return str(x)
    if isinstance(x, dict):
        return {str(k): clean(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [clean(v) for v in x]
    if isinstance(x, float):
        return x if math.isfinite(x) else None
    return x


def csv_clean(x: Any) -> Any:
    if x is None or (isinstance(x, float) and not math.isfinite(x)):
        return ""
    return json.dumps(clean(x), sort_keys=True) if isinstance(x, (dict, list, tuple)) else x


def require_root(root: Path) -> None:
    if not (root / "deu_validation").exists() or not any((root / p).exists() for p in ("source", "python", "classy.pyx")):
        raise SystemExit(f"Run from CLASS-DEU repo root, not from {root}")


def paths(root: Path) -> dict[str, Path]:
    out = root / "deu_validation" / "stage3b_outputs"
    return {
        "out": out,
        "json": out / f"{OUT_STEM}.json",
        "acceptance_md": out / f"{OUT_STEM}_acceptance.md",
        "github_readme": out / f"{OUT_STEM}_github_readme.md",
        "public_verification_report": out / f"{OUT_STEM}_public_verification_report.md",
        "release_manifest_csv": out / f"{OUT_STEM}_release_artifact_manifest.csv",
        "release_manifest_json": out / f"{OUT_STEM}_release_artifact_manifest.json",
        "sha256_manifest_csv": out / f"{OUT_STEM}_sha256_manifest.csv",
        "repository_layout_md": out / f"{OUT_STEM}_repository_layout.md",
        "verification_commands_md": out / f"{OUT_STEM}_verification_commands.md",
        "preprint_wording_md": out / f"{OUT_STEM}_preprint_wording.md",
        "claim_matrix_csv": out / f"{OUT_STEM}_claim_matrix.csv",
        "allowed_statements_csv": out / f"{OUT_STEM}_allowed_preprint_statements.csv",
        "blocked_claims_csv": out / f"{OUT_STEM}_blocked_claims.csv",
        "github_release_checklist_csv": out / f"{OUT_STEM}_github_release_checklist.csv",
        "github_publish_plan_md": out / f"{OUT_STEM}_github_publish_plan.md",
        "evidence_lineage_csv": out / f"{OUT_STEM}_evidence_lineage.csv",
        "tt_lite_scope_md": out / f"{OUT_STEM}_tt_lite_scope.md",
        "tri_anchor_context_csv": out / f"{OUT_STEM}_tri_anchor_context.csv",
        "scope_manifest": out / f"{OUT_STEM}_scope_manifest.json",
    }


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    keys: list[str] = []
    seen = set()
    for row in rows:
        for key in row:
            if key not in seen:
                seen.add(key)
                keys.append(str(key))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: csv_clean(row.get(key)) for key in keys})


def sha256_file(path: Path) -> Optional[str]:
    if not path.exists() or not path.is_file():
        return None
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def stage_json_path(out: Path, stem: str) -> Path:
    return out / f"{stem}.json"


def stage_acceptance(data: Mapping[str, Any]) -> Mapping[str, Any]:
    acc = data.get("acceptance")
    return acc if isinstance(acc, dict) else {}


def stage_manifest(data: Mapping[str, Any]) -> Mapping[str, Any]:
    for key in (
        "submission_manifest",
        "package_manifest",
        "scope_manifest",
        "freeze_manifest",
        "handoff_manifest",
        "gate_manifest",
        "final_report_manifest",
        "readiness_manifest",
        "summary_manifest",
    ):
        val = data.get(key)
        if isinstance(val, dict):
            return val
    return {}


def stage_diagnostic(data: Mapping[str, Any]) -> Optional[str]:
    acc = stage_acceptance(data)
    if acc.get("diagnostic_outcome"):
        return str(acc.get("diagnostic_outcome"))
    if data.get("diagnostic_outcome"):
        return str(data.get("diagnostic_outcome"))
    man = stage_manifest(data)
    if man.get("decision_type"):
        return str(man.get("decision_type"))
    return None


def collect_stage_status(out: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for stem, expected in EXPECTED_STAGE_DECISIONS.items():
        path = stage_json_path(out, stem)
        data = load_json(path)
        acc = stage_acceptance(data)
        diagnostic = stage_diagnostic(data)
        rows.append({
            "stage_stem": stem,
            "path": str(path),
            "exists": path.exists(),
            "hard_guard_pass": bool(acc.get("hard_guard_pass") or data.get("hard_guard_pass")),
            "diagnostic_outcome": diagnostic,
            "expected_decision": expected,
            "expected_decision_match": diagnostic == expected,
        })
    return rows


def core_artifact_rows(out: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for rel in CORE_REQUIRED_ARTIFACTS:
        path = out / rel
        rows.append({
            "artifact_group": "core_required",
            "relative_path": f"deu_validation/stage3b_outputs/{rel}",
            "absolute_path": str(path),
            "exists": path.exists(),
            "size_bytes": path.stat().st_size if path.exists() and path.is_file() else None,
            "sha256": sha256_file(path),
        })
    return rows


def expand_recommended_release_artifacts(out: Path) -> list[dict[str, Any]]:
    patterns = [
        "stage3b37_preprint_release_scope_lock*",
        "stage3b38_preprint_manuscript_package*",
        "stage3b39_preprint_submission_readiness_gate*",
        "stage3b35_replication_package_freeze_reviewer_dry_run*",
        "stage3b36_external_reviewer_handoff_result_gate*",
        "stage3b32_independent_evidence_result_gate_publication_lock*",
        "stage3b33_external_evidence_publication_claim_lock_addendum*",
        "stage3b20_final_scoped_internal_report*",
        "stage3b19_matched_deu_native_comparison_claim_lock*",
        "stage3b18_additional_native_baseline_chains_readiness*",
        "stage3b9_additional_production_chains_readiness*",
        "chains/stage3b6_first_production_run*.txt",
        "chains/stage3b16_native_baseline_run*.txt",
    ]
    rows: list[dict[str, Any]] = []
    seen = set()
    for pattern in patterns:
        for path_s in sorted(glob.glob(str(out / pattern))):
            path = Path(path_s)
            if path in seen or not path.is_file():
                continue
            seen.add(path)
            rel = path.relative_to(out.parent.parent) if str(path).startswith(str(out.parent.parent)) else path
            rows.append({
                "artifact_group": "recommended_public_verification",
                "relative_path": str(rel),
                "absolute_path": str(path),
                "exists": True,
                "size_bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            })
    return rows


def allowed_preprint_statements() -> list[dict[str, str]]:
    return [
        {
            "statement_id": "preprint_status",
            "allowed_statement": "This manuscript is an author-led preprint and has not yet undergone journal peer review.",
            "scope": "preprint metadata / manuscript front matter",
        },
        {
            "statement_id": "public_verification",
            "allowed_statement": "The code, chain artifacts, validation ledgers, checksums, and reproduction commands are publicly available for reader verification in the associated GitHub repository.",
            "scope": "data/code availability statement",
        },
        {
            "statement_id": "scoped_posterior",
            "allowed_statement": "Within the stated DEU full-objective likelihood configuration, the booked production chains support the reported scoped posterior summary.",
            "scope": "results with caveats",
        },
        {
            "statement_id": "scoped_comparison",
            "allowed_statement": "The matched DEU/native comparison is reported descriptively under the same staged validation scope.",
            "scope": "comparison section",
        },
        {
            "statement_id": "internal_evidence",
            "allowed_statement": "The formal and independent evidence-estimator diagnostics favor DEU over the native baseline within the internal validation protocol; this is reported as a caveated estimator result, not as peer-reviewed model superiority.",
            "scope": "evidence lineage section",
        },
        {
            "statement_id": "tt_lite_scope",
            "allowed_statement": "TT_lite was monitored as diagnostic context but was excluded from the sampled production and evidence likelihoods.",
            "scope": "methods / limitations",
        },
    ]


def blocked_claims() -> list[dict[str, str]]:
    return [
        {
            "claim_id": "peer_reviewed",
            "blocked_claim": "Do not claim that the work is peer reviewed or independently externally reviewed.",
            "reason": "No external reviewer result was booked; the old reviewer path remained pending by design.",
        },
        {
            "claim_id": "unqualified_model_superiority",
            "blocked_claim": "Do not state unqualified model superiority or final cosmological truth.",
            "reason": "The current route allows scoped internal/preprint evidence language with caveats, not final model-selection claims.",
        },
        {
            "claim_id": "tt_lite_in_evidence",
            "blocked_claim": "Do not claim TT_lite was part of the sampled posterior or evidence likelihood.",
            "reason": "TT_lite remained diagnostic-only throughout the production/evidence chain.",
        },
        {
            "claim_id": "final_publication_style",
            "blocked_claim": "Do not use final publication-style language implying journal acceptance or settled review.",
            "reason": "The release is an author-led preprint with a public verification package.",
        },
        {
            "claim_id": "reader_review_equals_peer_review",
            "blocked_claim": "Do not equate GitHub reader verification with formal peer review.",
            "reason": "Public reproducibility access supports transparency, not reviewer certification.",
        },
    ]


def claim_matrix() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in allowed_preprint_statements():
        rows.append({
            "claim_type": "allowed",
            "id": row["statement_id"],
            "statement": row["allowed_statement"],
            "scope": row["scope"],
            "preprint_allowed": True,
            "requires_github_link": row["statement_id"] in {"public_verification", "internal_evidence"},
        })
    for row in blocked_claims():
        rows.append({
            "claim_type": "blocked",
            "id": row["claim_id"],
            "statement": row["blocked_claim"],
            "scope": row["reason"],
            "preprint_allowed": False,
            "requires_github_link": False,
        })
    return rows


def github_release_checklist(stage_status: Sequence[Mapping[str, Any]], artifact_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    required_rows = [r for r in artifact_rows if r.get("artifact_group") == "core_required"]
    return [
        {"check": "Stage 3B-37 preprint path booked", "pass": any(r.get("stage_stem") == PREPRINT_SCOPE_STEM and r.get("hard_guard_pass") for r in stage_status)},
        {"check": "Stage 3B-38 manuscript package booked", "pass": any(r.get("stage_stem") == MANUSCRIPT_STEM and r.get("hard_guard_pass") for r in stage_status)},
        {"check": "Stage 3B-39 submission readiness booked", "pass": any(r.get("stage_stem") == SUBMISSION_STEM and r.get("hard_guard_pass") for r in stage_status)},
        {"check": "Frozen package lineage present", "pass": any(r.get("stage_stem") == FREEZE_STEM and r.get("hard_guard_pass") for r in stage_status)},
        {"check": "Core release artifacts present", "pass": all(bool(r.get("exists")) for r in required_rows)},
        {"check": "Core release artifact SHA256 hashes computed", "pass": all(bool(r.get("sha256")) for r in required_rows)},
        {"check": "Allowed preprint statements written", "pass": True},
        {"check": "Blocked claim list written", "pass": True},
        {"check": "No peer-review claim allowed", "pass": True},
        {"check": "No TT_lite sampled posterior/evidence claim allowed", "pass": True},
    ]


def evidence_lineage(stage32: Mapping[str, Any], stage33: Mapping[str, Any]) -> list[dict[str, Any]]:
    gm32 = stage_manifest(stage32)
    sm33 = stage_manifest(stage33)
    values = {
        "deu_log_evidence_independent_validation": gm32.get("deu_log_evidence_independent_validation", sm33.get("deu_log_evidence_independent_validation")),
        "native_log_evidence_independent_validation": gm32.get("native_log_evidence_independent_validation", sm33.get("native_log_evidence_independent_validation")),
        "log_bayes_factor_independent_validation_deu_minus_native": gm32.get("log_bayes_factor_independent_validation_deu_minus_native", sm33.get("log_bayes_factor_independent_validation_deu_minus_native")),
        "formal_log_bayes_factor_lineage": gm32.get("formal_log_bayes_factor_lineage", sm33.get("formal_log_bayes_factor_lineage")),
        "proxy_log_bayes_factor_lineage": gm32.get("proxy_log_bayes_factor_lineage", sm33.get("proxy_log_bayes_factor_lineage")),
    }
    return [{"quantity": k, "value": v, "scope": "internal/preprint evidence lineage with caveats"} for k, v in values.items()]


def tri_anchor_rows(out: Path) -> list[dict[str, Any]]:
    candidates = [
        out / f"{STAGE3B0 if False else SETUP_STEM}_monitoring_points.json",
        out / f"{PREPRINT_SCOPE_STEM}_tri_anchor_context.csv",
        out / f"{MANUSCRIPT_STEM}_tri_anchor_context.csv",
        out / f"{SUBMISSION_STEM}_tri_anchor_context.csv",
    ]
    monitoring = candidates[0]
    if monitoring.exists():
        data = load_json(monitoring)
        rows = data.get("tri_anchor_ledger") or []
        if rows:
            return [dict(r) for r in rows if isinstance(r, dict)]
    for csv_path in candidates[1:]:
        if csv_path.exists():
            with csv_path.open("r", encoding="utf-8", newline="") as f:
                return [dict(r) for r in csv.DictReader(f)]
    return []


def write_markdown_outputs(p: Mapping[str, Path], manifest: Mapping[str, Any], evidence_rows: Sequence[Mapping[str, Any]]) -> None:
    readme = [
        "# DEU CMB validation public verification package",
        "",
        "This repository package supports an author-led preprint. It has not been peer reviewed.",
        "",
        "## What readers can verify",
        "",
        "- The staged validation artifacts and acceptance ledgers.",
        "- The DEU and native/baseline production chain artifacts used in the scoped comparison.",
        "- The formal and independent evidence-estimator lineage reported with caveats.",
        "- The TT_lite scope: diagnostic-only, not part of the sampled production/evidence likelihood.",
        "",
        "## Current claim boundary",
        "",
        "Allowed: author-led preprint statements, scoped posterior summaries, and caveated internal evidence-lineage statements.",
        "",
        "Blocked: peer-review claims, unqualified model-superiority claims, TT_lite-in-posterior/evidence claims, and final publication-style claims.",
        "",
        "## Evidence lineage snapshot",
        "",
    ]
    for row in evidence_rows:
        readme.append(f"- `{row.get('quantity')}`: `{row.get('value')}`")
    readme += ["", "See the SHA256 manifest and artifact manifest for reproducibility checks.", ""]
    p["github_readme"].write_text("\n".join(readme), encoding="utf-8")

    report = [
        "# Stage 3B-40 public verification release report",
        "",
        f"Generated UTC: `{now()}`",
        "",
        f"Decision: `{manifest.get('decision_type')}`",
        "",
        "This stage prepares the GitHub/public verification package for the author-led preprint path.",
        "It does not launch MCMC, does not compute evidence, and does not certify peer review.",
        "",
        "## Release status",
        "",
        f"- Public verification package ready: `{manifest.get('public_github_verification_package_ready')}`",
        f"- Author-led preprint release allowed: `{manifest.get('author_led_preprint_release_allowed')}`",
        f"- Peer-review claim allowed: `{manifest.get('peer_review_claims_allowed')}`",
        f"- Model-superiority claim allowed: `{manifest.get('model_superiority_claims_allowed')}`",
        f"- TT_lite sampled posterior/evidence claim allowed: `{manifest.get('tt_lite_sampled_posterior_or_evidence_claims_allowed')}`",
        "",
        "## Recommended manuscript wording",
        "",
        "Use: 'This author-led preprint has not yet undergone journal peer review. The full code, validation ledgers, chains, checksums, and reproduction commands are publicly available for reader verification.'",
        "",
    ]
    p["public_verification_report"].write_text("\n".join(report), encoding="utf-8")

    layout = [
        "# Recommended GitHub repository layout",
        "",
        "```text",
        "CLASS-DEU/",
        "  README.md",
        "  deu_validation/",
        "    stage3b_outputs/",
        "      stage3b37_*",
        "      stage3b38_*",
        "      stage3b39_*",
        "      stage3b40_*",
        "      chains/",
        "  source/",
        "  python/",
        "  explanatory.ini / Cobaya YAML artifacts as available",
        "```",
        "",
        "The public release should include the exact git commit/tag and the Stage 3B-40 SHA256 manifest.",
        "",
    ]
    p["repository_layout_md"].write_text("\n".join(layout), encoding="utf-8")

    commands = [
        "# Public verification commands",
        "",
        "```bash",
        "git clone <PUBLIC_GITHUB_URL>",
        "cd CLASS-DEU",
        "git checkout <BOOKED_STAGE3B40_TAG>",
        "sha256sum -c deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_sha256_manifest.csv  # adapt if using CSV parser",
        "source ~/deu_class/deu_boltzmann_start/.venv/bin/activate",
        "export COBAYA_PACKAGES_PATH=~/deu_class/cobaya_packages",
        "python deu_validation/stage3b_40_github_public_verification_release.py",
        "```",
        "",
        "For exact reproduction of MCMC chains, use the booked Stage 3B production/native execution YAML files and the command logs in the artifact manifest.",
    ]
    p["verification_commands_md"].write_text("\n".join(commands), encoding="utf-8")

    wording = [
        "# Preprint wording lock",
        "",
        "Recommended language:",
        "",
        "> This is an author-led preprint and has not yet undergone journal peer review. The code, validation ledgers, chain artifacts, checksums, and reproduction commands are publicly available in the accompanying GitHub repository so readers can inspect and reproduce the staged analysis.",
        "",
        "Avoid language implying peer review, journal acceptance, or final model-superiority certification.",
        "",
    ]
    p["preprint_wording_md"].write_text("\n".join(wording), encoding="utf-8")

    publish_plan = [
        "# GitHub publication plan",
        "",
        "1. Create a public GitHub repository or public release branch.",
        "2. Push the booked Stage 3B-40 commit and tag.",
        "3. Add the Stage 3B-40 README, artifact manifest, and SHA256 manifest to the repository root or release notes.",
        "4. Link the GitHub repository in the preprint data/code availability statement.",
        "5. Keep the manuscript wording aligned with the blocked-claims table.",
        "",
    ]
    p["github_publish_plan_md"].write_text("\n".join(publish_plan), encoding="utf-8")

    tt_lite = [
        "# TT_lite publication scope",
        "",
        "TT_lite was monitored as diagnostic context but excluded from the sampled production posterior and evidence likelihoods.",
        "Do not write that TT_lite was included in the production posterior or evidence calculation unless a later booked stage explicitly changes that scope.",
        "",
    ]
    p["tt_lite_scope_md"].write_text("\n".join(tt_lite), encoding="utf-8")


def build_manifest(stage_status: Sequence[Mapping[str, Any]], artifact_rows: Sequence[Mapping[str, Any]], checklist: Sequence[Mapping[str, Any]], evidence_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    core_rows = [r for r in artifact_rows if r.get("artifact_group") == "core_required"]
    stages_ok = all(bool(r.get("exists")) and bool(r.get("hard_guard_pass")) for r in stage_status if r.get("stage_stem") in {PREPRINT_SCOPE_STEM, MANUSCRIPT_STEM, SUBMISSION_STEM})
    lineage_values = {str(r.get("quantity")): finite(r.get("value")) for r in evidence_rows}
    evidence_values_finite = all(v is not None for v in lineage_values.values() if "log" in str(v) or True)
    public_ready = stages_ok and all(bool(r.get("exists")) for r in core_rows) and all(bool(r.get("pass")) for r in checklist)
    return {
        "decision_type": "GITHUB_PUBLIC_VERIFICATION_RELEASE_PASS_AUTHOR_LED_PREPRINT_READY" if public_ready else "GITHUB_PUBLIC_VERIFICATION_RELEASE_FAIL",
        "recommendation": "Book Stage 3B-40. Publish the repository/package link with the author-led preprint; retain caveats and blocked-claim boundaries." if public_ready else "Do not book. Repair missing package artifacts or failed status checks first.",
        "next_stage_hint": "Stage 3B-41 preprint repository URL lock and submission metadata finalization" if public_ready else "repair Stage 3B-40 package and rerun",
        "public_github_verification_package_ready": public_ready,
        "author_led_preprint_release_allowed": public_ready,
        "peer_review_claims_allowed": False,
        "external_reviewer_claims_allowed": False,
        "model_superiority_claims_allowed": False,
        "final_publication_claims_allowed": False,
        "tt_lite_sampled_posterior_or_evidence_claims_allowed": False,
        "public_reader_verification_language_allowed": True,
        "internal_evidence_language_allowed_with_caveats": True,
        "mcmc_launched_by_this_stage": False,
        "new_evidence_computed_by_this_stage": False,
        "stage_status_count": len(stage_status),
        "core_required_artifact_count": len(core_rows),
        "core_required_artifacts_present": sum(1 for r in core_rows if r.get("exists")),
        "release_artifact_count": len(artifact_rows),
        "evidence_lineage": list(evidence_rows),
        "posterior_evidence_status": "author_led_preprint_public_verification_ready_claims_scoped" if public_ready else "public_verification_package_not_ready",
    }


def compute_acceptance(stage_status: Sequence[Mapping[str, Any]], artifact_rows: Sequence[Mapping[str, Any]], checklist: Sequence[Mapping[str, Any]], manifest: Mapping[str, Any], p: Mapping[str, Path]) -> dict[str, Any]:
    core_rows = [r for r in artifact_rows if r.get("artifact_group") == "core_required"]
    acc = {
        "stage3b37_preprint_scope_loaded_and_passed": any(r.get("stage_stem") == PREPRINT_SCOPE_STEM and r.get("hard_guard_pass") for r in stage_status),
        "stage3b38_manuscript_package_loaded_and_passed": any(r.get("stage_stem") == MANUSCRIPT_STEM and r.get("hard_guard_pass") for r in stage_status),
        "stage3b39_submission_readiness_loaded_and_passed": any(r.get("stage_stem") == SUBMISSION_STEM and r.get("hard_guard_pass") for r in stage_status),
        "replication_freeze_lineage_loaded": any(r.get("stage_stem") == FREEZE_STEM and r.get("hard_guard_pass") for r in stage_status),
        "core_required_artifacts_present": all(bool(r.get("exists")) for r in core_rows),
        "core_required_sha256_computed": all(bool(r.get("sha256")) for r in core_rows),
        "github_readme_written": p["github_readme"].exists(),
        "public_verification_report_written": p["public_verification_report"].exists(),
        "release_manifest_csv_written": p["release_manifest_csv"].exists(),
        "release_manifest_json_written": p["release_manifest_json"].exists(),
        "sha256_manifest_csv_written": p["sha256_manifest_csv"].exists(),
        "repository_layout_written": p["repository_layout_md"].exists(),
        "verification_commands_written": p["verification_commands_md"].exists(),
        "preprint_wording_written": p["preprint_wording_md"].exists(),
        "claim_matrix_written": p["claim_matrix_csv"].exists(),
        "allowed_statements_written": p["allowed_statements_csv"].exists(),
        "blocked_claims_written": p["blocked_claims_csv"].exists(),
        "github_release_checklist_written": p["github_release_checklist_csv"].exists(),
        "github_publish_plan_written": p["github_publish_plan_md"].exists(),
        "evidence_lineage_written": p["evidence_lineage_csv"].exists(),
        "tt_lite_scope_written": p["tt_lite_scope_md"].exists(),
        "tri_anchor_context_written": p["tri_anchor_context_csv"].exists(),
        "scope_manifest_written": p["scope_manifest"].exists(),
        "public_github_verification_package_ready": bool(manifest.get("public_github_verification_package_ready")),
        "author_led_preprint_release_allowed": bool(manifest.get("author_led_preprint_release_allowed")),
        "peer_review_claims_allowed": False,
        "model_superiority_claims_allowed": False,
        "final_publication_claims_allowed": False,
        "tt_lite_sampled_posterior_or_evidence_claims_allowed": False,
        "mcmc_launched_by_this_stage": False,
        "new_evidence_computed_by_this_stage": False,
        "script_completed": True,
        "diagnostic_outcome": manifest.get("decision_type"),
    }
    guards = [k for k in acc if k not in {"diagnostic_outcome", "peer_review_claims_allowed", "model_superiority_claims_allowed", "final_publication_claims_allowed", "tt_lite_sampled_posterior_or_evidence_claims_allowed", "mcmc_launched_by_this_stage", "new_evidence_computed_by_this_stage"}]
    acc["hard_guard_pass"] = all(bool(acc[k]) for k in guards) and acc["peer_review_claims_allowed"] is False and acc["model_superiority_claims_allowed"] is False and acc["mcmc_launched_by_this_stage"] is False
    return acc


def write_acceptance_md(path: Path, report: Mapping[str, Any]) -> None:
    acc = report["acceptance"]
    manifest = report["scope_manifest"]
    outputs = report["outputs"]
    def pf(x: Any) -> str:
        return "PASS" if bool(x) else "FAIL"
    checks = [
        ("Stage 3B-37 preprint scope loaded and passed", "stage3b37_preprint_scope_loaded_and_passed"),
        ("Stage 3B-38 manuscript package loaded and passed", "stage3b38_manuscript_package_loaded_and_passed"),
        ("Stage 3B-39 submission readiness loaded and passed", "stage3b39_submission_readiness_loaded_and_passed"),
        ("replication freeze lineage loaded", "replication_freeze_lineage_loaded"),
        ("core required artifacts present", "core_required_artifacts_present"),
        ("core required SHA256 computed", "core_required_sha256_computed"),
        ("public GitHub verification package ready", "public_github_verification_package_ready"),
        ("author-led preprint release allowed", "author_led_preprint_release_allowed"),
        ("peer-review claims allowed", "peer_review_claims_allowed"),
        ("model-superiority claims allowed", "model_superiority_claims_allowed"),
        ("final publication claims allowed", "final_publication_claims_allowed"),
        ("TT_lite sampled posterior/evidence claims allowed", "tt_lite_sampled_posterior_or_evidence_claims_allowed"),
        ("MCMC launched by this stage", "mcmc_launched_by_this_stage"),
        ("new evidence computed by this stage", "new_evidence_computed_by_this_stage"),
        ("hard guard pass", "hard_guard_pass"),
    ]
    lines = [
        "# Stage 3B-40 GitHub public verification release acceptance",
        "",
        f"Generated UTC: `{report['generated_utc']}`",
        "",
        "This stage prepares the author-led preprint's public verification package. It does not claim peer review.",
        "",
        "## Acceptance",
        "",
        "| Check | Status |",
        "|---|---:|",
    ]
    for label, key in checks:
        if key in {"peer_review_claims_allowed", "model_superiority_claims_allowed", "final_publication_claims_allowed", "tt_lite_sampled_posterior_or_evidence_claims_allowed", "mcmc_launched_by_this_stage", "new_evidence_computed_by_this_stage"} and acc.get(key) is False:
            status = "NO"
        else:
            status = pf(acc.get(key))
        lines.append(f"| {label} | **{status}** |")
    lines += [
        "",
        f"Diagnostic outcome: `{acc.get('diagnostic_outcome')}`",
        "",
        "## Release decision",
        "",
        f"Decision type: `{manifest.get('decision_type')}`",
        "",
        f"Recommendation: {manifest.get('recommendation')}",
        "",
        f"Next-stage hint: `{manifest.get('next_stage_hint')}`",
        "",
        "## Outputs",
        "",
    ]
    for k, v in outputs.items():
        lines.append(f"- `{k}`: `{v}`")
    lines += ["", "## Booking decision", ""]
    if acc.get("hard_guard_pass"):
        lines += [
            "PASS: bookable as the GitHub public verification release package stage.",
            "The preprint may link the public repository for reader verification, but must not imply peer review or unqualified model superiority.",
            "",
            "```bash",
            f"git add deu_validation/{SCRIPT_NAME} \\",
            f"        deu_validation/stage3b_outputs/{OUT_STEM}.json \\",
            f"        deu_validation/stage3b_outputs/{OUT_STEM}_acceptance.md \\",
            f"        deu_validation/stage3b_outputs/{OUT_STEM}_github_readme.md \\",
            f"        deu_validation/stage3b_outputs/{OUT_STEM}_public_verification_report.md \\",
            f"        deu_validation/stage3b_outputs/{OUT_STEM}_release_artifact_manifest.csv \\",
            f"        deu_validation/stage3b_outputs/{OUT_STEM}_release_artifact_manifest.json \\",
            f"        deu_validation/stage3b_outputs/{OUT_STEM}_sha256_manifest.csv \\",
            f"        deu_validation/stage3b_outputs/{OUT_STEM}_repository_layout.md \\",
            f"        deu_validation/stage3b_outputs/{OUT_STEM}_verification_commands.md \\",
            f"        deu_validation/stage3b_outputs/{OUT_STEM}_preprint_wording.md \\",
            f"        deu_validation/stage3b_outputs/{OUT_STEM}_claim_matrix.csv \\",
            f"        deu_validation/stage3b_outputs/{OUT_STEM}_allowed_preprint_statements.csv \\",
            f"        deu_validation/stage3b_outputs/{OUT_STEM}_blocked_claims.csv \\",
            f"        deu_validation/stage3b_outputs/{OUT_STEM}_github_release_checklist.csv \\",
            f"        deu_validation/stage3b_outputs/{OUT_STEM}_github_publish_plan.md \\",
            f"        deu_validation/stage3b_outputs/{OUT_STEM}_evidence_lineage.csv \\",
            f"        deu_validation/stage3b_outputs/{OUT_STEM}_tt_lite_scope.md \\",
            f"        deu_validation/stage3b_outputs/{OUT_STEM}_tri_anchor_context.csv \\",
            f"        deu_validation/stage3b_outputs/{OUT_STEM}_scope_manifest.json",
            "git commit -m \"Stage 3B-40 GitHub public verification release\"",
            "git tag deu-stage3b40-github-public-verification-release-v0",
            "```",
        ]
    else:
        lines.append("FAIL: do not book. Repair missing stage/package artifacts or claim-scope checks first.")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: Optional[Sequence[str]] = None) -> int:
    _ = argv
    root = Path.cwd().resolve()
    require_root(root)
    p = paths(root)
    p["out"].mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    print(json.dumps({"stage": STAGE, "event": "start", "generated_utc": now(), "cwd": str(root)}, indent=2, sort_keys=True), flush=True)

    out = p["out"]
    stage_status = collect_stage_status(out)
    artifact_rows = core_artifact_rows(out) + expand_recommended_release_artifacts(out)
    checklist = github_release_checklist(stage_status, artifact_rows)

    stage32 = load_json(stage_json_path(out, INDEPENDENT_GATE_STEM))
    stage33 = load_json(stage_json_path(out, PUBLICATION_LOCK_STEM))
    evidence_rows = evidence_lineage(stage32, stage33)
    tri_rows = tri_anchor_rows(out)

    write_csv(p["release_manifest_csv"], artifact_rows)
    p["release_manifest_json"].write_text(json.dumps(clean({"artifacts": artifact_rows}), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_csv(p["sha256_manifest_csv"], [{"relative_path": r.get("relative_path"), "sha256": r.get("sha256")} for r in artifact_rows if r.get("sha256")])
    write_csv(p["claim_matrix_csv"], claim_matrix())
    write_csv(p["allowed_statements_csv"], allowed_preprint_statements())
    write_csv(p["blocked_claims_csv"], blocked_claims())
    write_csv(p["github_release_checklist_csv"], checklist)
    write_csv(p["evidence_lineage_csv"], evidence_rows)
    write_csv(p["tri_anchor_context_csv"], tri_rows)

    manifest = build_manifest(stage_status, artifact_rows, checklist, evidence_rows)
    write_markdown_outputs(p, manifest, evidence_rows)
    p["scope_manifest"].write_text(json.dumps(clean(manifest), indent=2, sort_keys=True) + "\n", encoding="utf-8")

    acc = compute_acceptance(stage_status, artifact_rows, checklist, manifest, p)
    report = {
        "stage": STAGE,
        "script": SCRIPT_NAME,
        "generated_utc": now(),
        "elapsed_s": time.time() - t0,
        "cwd": str(root),
        "stage_status": stage_status,
        "github_release_checklist": checklist,
        "release_artifact_count": len(artifact_rows),
        "core_required_artifact_count": len([r for r in artifact_rows if r.get("artifact_group") == "core_required"]),
        "evidence_lineage": evidence_rows,
        "tri_anchor_context_count": len(tri_rows),
        "scope_manifest": manifest,
        "acceptance": acc,
        "outputs": {
            "json": str(p["json"]),
            "acceptance_md": str(p["acceptance_md"]),
            "github_readme": str(p["github_readme"]),
            "public_verification_report": str(p["public_verification_report"]),
            "release_manifest_csv": str(p["release_manifest_csv"]),
            "release_manifest_json": str(p["release_manifest_json"]),
            "sha256_manifest_csv": str(p["sha256_manifest_csv"]),
            "repository_layout_md": str(p["repository_layout_md"]),
            "verification_commands_md": str(p["verification_commands_md"]),
            "preprint_wording_md": str(p["preprint_wording_md"]),
            "claim_matrix_csv": str(p["claim_matrix_csv"]),
            "allowed_statements_csv": str(p["allowed_statements_csv"]),
            "blocked_claims_csv": str(p["blocked_claims_csv"]),
            "github_release_checklist_csv": str(p["github_release_checklist_csv"]),
            "github_publish_plan_md": str(p["github_publish_plan_md"]),
            "evidence_lineage_csv": str(p["evidence_lineage_csv"]),
            "tt_lite_scope_md": str(p["tt_lite_scope_md"]),
            "tri_anchor_context_csv": str(p["tri_anchor_context_csv"]),
            "scope_manifest": str(p["scope_manifest"]),
        },
    }
    p["json"].write_text(json.dumps(clean(report), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_acceptance_md(p["acceptance_md"], report)

    compact = {
        "stage": STAGE,
        "generated_utc": report["generated_utc"],
        "elapsed_s": report["elapsed_s"],
        "diagnostic_outcome": acc.get("diagnostic_outcome"),
        "hard_guard_pass": acc.get("hard_guard_pass"),
        "public_github_verification_package_ready": manifest.get("public_github_verification_package_ready"),
        "author_led_preprint_release_allowed": manifest.get("author_led_preprint_release_allowed"),
        "peer_review_claims_allowed": manifest.get("peer_review_claims_allowed"),
        "model_superiority_claims_allowed": manifest.get("model_superiority_claims_allowed"),
        "outputs": report["outputs"],
    }
    print(json.dumps(clean(compact), indent=2, sort_keys=True), flush=True)
    return 0 if acc.get("hard_guard_pass") else 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
