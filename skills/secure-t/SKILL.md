---
name: secure-t
description: "Audit any repo for security weaknesses, fix the code, push to GitHub fully configured (branches, protection, Pages, Actions, Dependabot), deploy the web UI to Vercel + Cloudflare Pages, update README with live links. Use whenever user says audita, encuentra debilidades/fallos, repáralo, súbelo a git/GitHub, despliega en Vercel/Cloudflare/Pages, déjalo impecable, que nunca se caiga, audit/fix/ship/harden/deploy, security audit — in Spanish or English — even if they never say 'secure-t'."
platforms: [linux, macos, windows]
---

# secure-t

Pipeline: recon → audit → fix → secrets → GitHub → CDN → README. 9 phases. Never skip a gate.

## 0. Pre-flight (blocking)

Run first, every time:

- `gh auth status` / `vercel whoami` / `wrangler whoami`
- Missing auth → give exact login command, proceed only with authed tools
- Vague goal → ask scope (audit-only vs full-ship) with options before touching code

## Phases

| # | Phase | Actions | Gate |
|---|-------|---------|------|
| 1 | Recon | Identify target repo/URL. GitHub search API for candidates. Fetch site. Confirm scope. | Target + scope confirmed |
| 2 | Collect | Clone (shallow ok). Fetch all issues via API (`/repos/{o}/{r}/issues?state=all`). Delegate issue extraction to explore subagent. | Issue list with open bugs |
| 3 | Audit | Dispatch 2+ explore subagents in parallel, split by domain (core/backend/frontend). Demand `file:line` + severity per finding. See `references/audit-matrix.md`. | Findings table, zero vague items |
| 4 | Fix | CRITICO+ALTO first, surgical edits. Read file before editing. `py_compile` / `npm run build` after each batch. | Compiles + builds green |
| 5 | Secrets | Gitleaks staged+history. Env-var all secrets. Redact sample tokens in datasets. Push-protection block → squash to single clean commit, keep attribution in README. See `references/secrets.md`. | `no leaks found` |
| 6 | GitHub | Create repo. Push `main`+`develop`. Topics, homepage. Branch protection via API. Vuln alerts + Dependabot. Discussions. `dependabot.yml`, CI/CodeQL/pages workflows, `SECURITY.md`, `CODEOWNERS`. See `references/github.md`. | API verifies each setting |
| 7 | Build | Build frontend. Pin `react`/`react-dom` same major. Remove bogus imports. `legacy-peer-deps` if peers clash. Never commit `build/`. | Local build exits 0 |
| 8 | Deploy | gh-pages branch (build + `404.html` + `.nojekyll`) → enable Pages. Vercel link+deploy (rewrites). `wrangler pages deploy` (`_redirects`). Curl every URL → 200. Rollback plan ready. See `references/deploy.md`. | 3 live URLs, SPA routes work |
| 9 | README | Update README with all live links + audit summary. Push. | Links verified live |

## Severity

| Level | Means | Examples |
|-------|-------|----------|
| CRITICO | RCE, breach, total auth bypass | shell=True+user input, SQLi, hardcoded prod secrets |
| ALTO | Broken control, priv-esc, mass leak | Predictable sessions, plaintext passwords, open CORS, untrusted pickle.load |
| MEDIO | Crash, logic bug, dead feature | `__int__` typo, Path+str, unbound vars, invisible chars in paths |
| BAJO | Hygiene | Debug prints, non-crypto MD5, missing timeouts |

## Anti-patterns (do not repeat)

| # | Mistake | Fix |
|---|---------|-----|
| 1 | Commit `build/` artifacts | `.gitignore` + `git rm --cached` |
| 2 | react/react-dom major mismatch (`react-dom/client`) | Pin same major (18.x), `installCommand: npm install --legacy-peer-deps` |
| 3 | CDN builds stale git state | Push code first, then deploy |
| 4 | Secrets in history block push | Redact + squash to one clean commit, attribution in README |
| 5 | SPA without fallback | `404.html` (Pages), `_redirects` (Cloudflare), `rewrites` (Vercel) |
| 6 | Creds in console/localStorage | Remove dumps, httpOnly where possible |
| 7 | Vague audit output | Require `file:line` + severity per finding |
| 8 | Skipping gates | Gate red → stop, fix, re-verify before next phase |

## Rules

- Parallelize independent audits; one domain per subagent; integrate results yourself.
- Conventional Commits: `feat:` `fix:` `docs:` `chore:`. Small atomic commits.
- Run bundled scripts, never reimplement: `scripts/smoke_test.py` validates API keys without spending tokens; `scripts/audit_rotate_keys.py` scans/rotates `.env`; `scripts/audit-api-keys.ps1` audits Windows machines.
- Backend honesty: static frontend ships to CDN; server backends need Docker/VPS/PaaS — say so, offer options, never fake it.
- Keep this file lean. Details live in `references/`.
