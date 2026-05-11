# Stage 3B-40 GitHub public verification release acceptance

Generated UTC: `2026-05-09T20:26:20+00:00`

This stage prepares the author-led preprint's public verification package. It does not claim peer review.

## Acceptance

| Check | Status |
|---|---:|
| Stage 3B-37 preprint scope loaded and passed | **PASS** |
| Stage 3B-38 manuscript package loaded and passed | **PASS** |
| Stage 3B-39 submission readiness loaded and passed | **PASS** |
| replication freeze lineage loaded | **PASS** |
| core required artifacts present | **PASS** |
| core required SHA256 computed | **PASS** |
| public GitHub verification package ready | **PASS** |
| author-led preprint release allowed | **PASS** |
| peer-review claims allowed | **NO** |
| model-superiority claims allowed | **NO** |
| final publication claims allowed | **NO** |
| TT_lite sampled posterior/evidence claims allowed | **NO** |
| MCMC launched by this stage | **NO** |
| new evidence computed by this stage | **NO** |
| hard guard pass | **PASS** |

Diagnostic outcome: `GITHUB_PUBLIC_VERIFICATION_RELEASE_PASS_AUTHOR_LED_PREPRINT_READY`

## Release decision

Decision type: `GITHUB_PUBLIC_VERIFICATION_RELEASE_PASS_AUTHOR_LED_PREPRINT_READY`

Recommendation: Book Stage 3B-40. Publish the repository/package link with the author-led preprint; retain caveats and blocked-claim boundaries.

Next-stage hint: `Stage 3B-41 preprint repository URL lock and submission metadata finalization`

## Outputs

- `json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b40_github_public_verification_release.json`
- `acceptance_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_acceptance.md`
- `github_readme`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_github_readme.md`
- `public_verification_report`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_public_verification_report.md`
- `release_manifest_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_release_artifact_manifest.csv`
- `release_manifest_json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_release_artifact_manifest.json`
- `sha256_manifest_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_sha256_manifest.csv`
- `repository_layout_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_repository_layout.md`
- `verification_commands_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_verification_commands.md`
- `preprint_wording_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_preprint_wording.md`
- `claim_matrix_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_claim_matrix.csv`
- `allowed_statements_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_allowed_preprint_statements.csv`
- `blocked_claims_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_blocked_claims.csv`
- `github_release_checklist_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_github_release_checklist.csv`
- `github_publish_plan_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_github_publish_plan.md`
- `evidence_lineage_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_evidence_lineage.csv`
- `tt_lite_scope_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_tt_lite_scope.md`
- `tri_anchor_context_csv`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_tri_anchor_context.csv`
- `scope_manifest`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_scope_manifest.json`

## Booking decision

PASS: bookable as the GitHub public verification release package stage.
The preprint may link the public repository for reader verification, but must not imply peer review or unqualified model superiority.

```bash
git add deu_validation/stage3b_40_github_public_verification_release.py \
        deu_validation/stage3b_outputs/stage3b40_github_public_verification_release.json \
        deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_acceptance.md \
        deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_github_readme.md \
        deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_public_verification_report.md \
        deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_release_artifact_manifest.csv \
        deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_release_artifact_manifest.json \
        deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_sha256_manifest.csv \
        deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_repository_layout.md \
        deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_verification_commands.md \
        deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_preprint_wording.md \
        deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_claim_matrix.csv \
        deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_allowed_preprint_statements.csv \
        deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_blocked_claims.csv \
        deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_github_release_checklist.csv \
        deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_github_publish_plan.md \
        deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_evidence_lineage.csv \
        deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_tt_lite_scope.md \
        deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_tri_anchor_context.csv \
        deu_validation/stage3b_outputs/stage3b40_github_public_verification_release_scope_manifest.json
git commit -m "Stage 3B-40 GitHub public verification release"
git tag deu-stage3b40-github-public-verification-release-v0
```
