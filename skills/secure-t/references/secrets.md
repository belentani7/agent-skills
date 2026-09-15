# secrets — hygiene + rotation

## Scan (before every commit AND push)

```bash
gitleaks protect --staged --no-banner --config <cfg>   # pre-commit scope
gitleaks detect --no-banner --log-opts="--all"         # pre-push scope (full history)
```

4+ hits in training-data CSVs (JWTs, sample tokens) are typical false-positive-shaped reals: redact, don't allowlist blindly.

## Env-var pattern (all runtimes)

| Before | After |
|---|---|
| `SECRET = "hardcoded"` | `os.environ.get('APP_SECRET') or secrets.token_urlsafe(50)` |
| `DEBUG = True` | `os.environ.get('APP_DEBUG','0')=='1'` |
| `ALLOWED_HOSTS = []` | Parse from env, default localhost |
| `CORS_ALLOW_ALL = True` | `False` + explicit whitelist |

Never commit real values. Never leave `django-insecure-*`-shaped placeholders that scanners flag.

## Redact datasets

Targeted replace of flagged tokens with `REDACTED` (keep row structure for ML training data). Verify: re-run gitleaks → `no leaks found`. Grep tree for `AKIA|BEGIN PRIVATE KEY|ghp_|xox[baprs]-|sk-[A-Za-z0-9]{20,}` excluding lockfiles.

## Push blocked by secret history

1. Fix current tree first (env-vars, redacts).
2. Squash to single clean commit (`--orphan` or fresh `git init`), push clean branch.
3. Keep upstream attribution in README (fork line + original authors).
4. Do NOT `--no-verify` to bypass hooks unless tree is proven clean by manual scan.

## Rotation (secret was real and exposed)

Assume burned. Order: revoke at provider → generate new → update env/secret manager → redeploy → verify old key dead (`/models`-style free endpoint where available) → purge from history if pushed (filter-repo + force-push + notify).
