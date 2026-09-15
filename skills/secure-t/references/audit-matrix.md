# audit-matrix — what to hunt per layer

Split audit subagents by domain. Each finding needs `file:line` + severity + one-line why.

## Backend (Python/Node/any)

| Pattern | Severity | Fix |
|---|---|---|
| `shell=True` / `os.system` / `exec` with user input | CRITICO | argv list, `shell=False` |
| SQL string concatenation | CRITICO | Parameterized queries / ORM |
| Auth check that never verifies secret (`return True` on existence) | CRITICO | Verify credential, token sessions |
| Hardcoded SECRET_KEY / passwords / API keys | CRITICO | Env vars, fail-closed defaults |
| Predictable session tokens (`hash(user+time)`, sequential) | ALTO | `secrets.token_urlsafe`, expiry |
| Plaintext password compare/store | ALTO | Hashers (werkzeug/bcrypt/Django) |
| Unauthed sensitive endpoints (`/process`, `/admin`, debug) | ALTO | Require session on all |
| CORS `*` / `ALLOW_ALL=True` | ALTO | Explicit origin whitelist |
| `DEBUG=True` / empty `ALLOWED_HOSTS` in prod config | ALTO | Env-gated |
| Untrusted `pickle.load` / `yaml.load` / `eval` | ALTO | Validate type or use safe loaders |
| `requests.get` without timeout | BAJO | `timeout=10` |
| Bare `except:` swallowing errors | MEDIO | Catch specific exceptions |

## Frontend (React/Angular/any SPA)

| Pattern | Severity | Fix |
|---|---|---|
| `console.log` of tokens/passwords/cookies | ALTO | Delete dumps |
| Serializing full state (incl. secrets) in fetch body | ALTO | Send only required fields, never raw password/state |
| Secrets in localStorage | ALTO | HttpOnly cookies or memory |
| Login redirects on failure / cookie `"undefined"` | ALTO | Validate response before session set |
| Secret inputs with `type="text"` | MEDIO | `type="password"` |
| No route guards (client-only redirect) | MEDIO | Guard + server-side auth |
| Plain-HTTP credential POST | MEDIO | HTTPS only |
| Bogus imports (`{ component }` from react) | MEDIO | Remove, rebuild |
| react/react-dom major mismatch | MEDIO | Pin same major |

## Core libs / logic

| Pattern | Severity | Fix |
|---|---|---|
| `SyntaxError` / duplicate kwargs (module never imports) | MEDIO | Fix signature |
| Wrong attribute (`self.x` vs `self._X`) changing control flow | ALTO | Correct name, add test |
| Method used without `()` (always truthy) | ALTO | Call it |
| `@staticmethod` using `self` | MEDIO | Drop decorator |
| Invisible chars (U+200B) in paths/strings | MEDIO | Rewrite literal, verify bytes |
| `Path + str` TypeError | MEDIO | `Path / "seg"` |
| Unbound var on alternate branch | MEDIO | Init to None first |
| Infinite recursion (cleaners, mkdir helpers) | MEDIO | Base case / iterative |
| Input parsed without validation (`int(input())`, headers) | MEDIO | try/except + ranges |
| Relative paths depending on cwd (`../data/x`) | MEDIO | Absolute from `__file__` |

## Dependencies

| Pattern | Severity | Fix |
|---|---|---|
| Pinned CVE versions (check NVD/dependabot) | ALTO | Bump + regression test |
| EOL frameworks (Django 4.0, Angular 14) | MEDIO | Plan upgrade |
| `node_modules` or `build/` committed | MEDIO | `.gitignore` + `git rm --cached` |
| Missing lockfile (`package-lock.json` ignored) | MEDIO | Commit lockfile |
| `>=` ranges on breaking majors | BAJO | Pin or cap (`^`) |

## Threat-model pass (after pattern hunt)

For the app type, answer: who attacks, via what input, worst impact? Cover: network-exposed inputs, auth boundary, secret storage, deserialization points, subprocess calls. Add missing cases as findings.
