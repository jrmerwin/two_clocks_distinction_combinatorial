# Stage 3B-41 GitHub URL lock and preprint metadata finalization

Generated UTC: `2026-05-10T02:03:33+00:00`

This stage locks the public GitHub verification URL for the author-led preprint path. It does not launch MCMC, compute evidence, or verify network access.

## Acceptance

| Check | Status |
|---|---:|
| Stage 3B-40 reference loaded | **PASS** |
| Stage 3B-40 hard guard pass | **PASS** |
| Stage 3B-40 public verification release present | **PASS** |
| GitHub URL supplied | **PASS** |
| GitHub URL syntax valid | **PASS** |
| Manual public access verified by author | **PASS** |
| Author-led not peer-reviewed confirmed | **PASS** |
| GitHub access verified by script | **NO** |
| MCMC launched by this stage | **NO** |
| New evidence computed by this stage | **NO** |
| Peer-review/external-review claims allowed | **NO** |
| Model-superiority certification allowed | **NO** |
| TT_lite sampled posterior/evidence claims allowed | **NO** |
| Final publication claims allowed | **NO** |
| hard guard pass | **PASS** |

Diagnostic outcome: `GITHUB_URL_LOCK_PREPRINT_METADATA_PASS_AUTHOR_LED_PUBLIC_VERIFICATION_READY`

## Locked URL

Repository: `https://github.com/jrmerwin/two_clocks_distinction_combinatorial.git`

Release: `https://github.com/<owner>/<repo>/releases/tag/<tag>`

## Booking decision

PASS: bookable as the GitHub URL lock and preprint metadata finalization stage.

```bash
git add deu_validation/stage3b_41_github_url_lock_preprint_metadata.py \
        deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata.json \
        deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_acceptance.md \
        deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_github_url_input_template.json \
        deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_github_url_lock.json \
        deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_preprint_metadata.json \
        deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_preprint_release_notes.md \
        deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_public_verification_statement.md \
        deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_repository_public_access_checklist.csv \
        deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_claim_compliance_matrix.csv \
        deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_allowed_preprint_statements.csv \
        deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_blocked_claims.csv \
        deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_evidence_lineage.csv \
        deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_tt_lite_scope.md \
        deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_tri_anchor_context.csv \
        deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_submission_manifest.json
git commit -m "Stage 3B-41 GitHub URL lock preprint metadata"
git tag deu-stage3b41-github-url-lock-preprint-metadata-v0
```

## Outputs

- `json`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata.json`
- `acceptance_md`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_acceptance.md`
- `github_url_input_template`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_github_url_input_template.json`
- `github_url_lock`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_github_url_lock.json`
- `preprint_metadata`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_preprint_metadata.json`
- `preprint_release_notes`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_preprint_release_notes.md`
- `public_verification_statement`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_public_verification_statement.md`
- `repository_public_access_checklist`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_repository_public_access_checklist.csv`
- `claim_compliance_matrix`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_claim_compliance_matrix.csv`
- `allowed_preprint_statements`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_allowed_preprint_statements.csv`
- `blocked_claims`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_blocked_claims.csv`
- `evidence_lineage`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_evidence_lineage.csv`
- `tt_lite_scope`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_tt_lite_scope.md`
- `tri_anchor_context`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_tri_anchor_context.csv`
- `submission_manifest`: `/home/merwijas/deu_class/CLASS-DEU/deu_validation/stage3b_outputs/stage3b41_github_url_lock_preprint_metadata_submission_manifest.json`
