# deploy — build fixes + multi-CDN + verify

## React build triage (in order)

1. Read the actual error line (output truncates — rerun and capture head, not tail).
2. `react-dom/client` missing → react/react-dom major mismatch → pin same major (`18.2.0`/`18.2.0`), regenerate lockfile.
3. Peer conflicts → `npm install --legacy-peer-deps`; persist via `vercel.json` `installCommand`.
4. Bogus imports / TS errors → fix source, rebuild locally until exit 0.
5. Never commit `build/` or `node_modules/`; always commit lockfile.

## Vercel

`react_gui/vercel.json`:
```json
{"installCommand": "npm install --legacy-peer-deps",
 "rewrites": [{"source": "/(.*)", "destination": "/index.html"}]}
```

```bash
vercel link --yes --project <name>   # once
vercel deploy --prod --yes           # remote build from pushed git state
```

Rule: push code FIRST — Vercel builds from git, not local files. Static files bypass rewrites automatically.

## Cloudflare Pages

`public/_redirects` (ships inside build):
```
/* /index.html 200
```

```bash
wrangler pages deploy <build-dir> --project-name <name>
```

## Verify (blocking gate)

```bash
curl -s -o /dev/null -w "%{http_code}" <url>            # → 200
curl -s -o /dev/null -w "%{http_code}" <url>/dashboard  # SPA route → 200, not 404
```

Need 3 live URLs minimum (Pages + Vercel + Cloudflare) for redundancy.

## Rollback

- Vercel: dashboard → deployment → Promote previous, or `vercel rollback`.
- Pages (branch): `git revert` on `gh-pages` or re-push last good build.
- Cloudflare: Pages dashboard → Rollback to deployment.
- After rollback: re-verify all URLs, note cause in README/deploy log.

## README links (phase 9)

Update README with every live URL + audit summary. Push. Confirm pages workflow rebuilt `gh-pages` if triggered.
