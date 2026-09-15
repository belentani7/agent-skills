# github — full repo config via CLI/API

## Create + push

```bash
gh repo create <owner>/<repo> --public --description "<one-liner>"
git remote set-url origin https://github.com/<owner>/<repo>.git
git branch -m master main   # if needed
git push -u origin main && git branch develop && git push -u origin develop
```

## Metadata

```bash
gh repo edit <o>/<r> --add-topic security --add-topic <niche...>
gh api -X PATCH repos/<o>/<r> -f homepage="<primary-url>" -f has_discussions=true
```

## Branch protection (`main`)

PUT `repos/<o>/<r>/branches/main/protection` with JSON file:

```json
{"required_status_checks": null, "enforce_admins": false,
 "required_pull_request_reviews": {"dismiss_stale_reviews": true,
  "require_code_owner_reviews": false, "required_approving_review_count": 1},
 "restrictions": null, "allow_force_pushes": false, "allow_deletions": false,
 "required_conversation_resolution": true}
```

Note: `enforce_admins:false` lets owner push directly; set true for strict teams.

## Security features

```bash
gh api -X PUT repos/<o>/<r>/vulnerability-alerts
gh api -X PUT repos/<o>/<r>/automated-security-fixes
```

Verify: `GET repos/<o>/<r>` → `security_and_analysis` all `enabled`.

## Files to add

| File | Purpose |
|---|---|
| `.github/dependabot.yml` | pip + npm (+gui) + github-actions, weekly |
| `.github/workflows/ci.yml` | Compile + build on push/PR to main/develop |
| `.github/workflows/pages-deploy.yml` | Build frontend → `gh-pages` on push to main (`contents: write`) |
| `.github/workflows/codeql.yml` | python + javascript-typescript, weekly schedule |
| `.github/CODEOWNERS` | `* @owner` |
| `SECURITY.md` | Private disclosure (security/advisories/new), supported versions |

## Pages (static SPA)

1. Build locally. Copy `build/*` to temp dir, add `404.html` (= copy of `index.html`) + `.nojekyll`.
2. Push temp repo to `gh-pages` branch (orphan).
3. POST `repos/<o>/<r>/pages` `{"build_type":"legacy","source":{"branch":"gh-pages","path":"/"}}`.
4. Poll `GET repos/<o>/<r>/pages` until `status: built`. URL: `https://<owner>.github.io/<repo>/`.
