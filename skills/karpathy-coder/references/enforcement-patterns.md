# Enforcement Patterns — Hooks, CI, and Team Adoption

How to make the four principles stick mechanically instead of relying on memory.

## 1. Pre-commit hook (local, non-blocking)

`.git/hooks/pre-commit` or Husky `pre-commit`:

```bash
#!/usr/bin/env bash
set -euo pipefail
# Run the shipped checkers on staged files (stdlib-only Python).
staged=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(py|ts|tsx|js|sh)$' || true)
[ -z "$staged" ] && exit 0

python scripts/complexity_checker.py $staged || echo "warn: complexity"
python scripts/diff_surgeon.py --staged || echo "warn: diff noise"
```

Keep it **warn-only** by default. Make it blocking (`exit 1`) only once the team agrees.

## 2. CI gate (blocking on regressions)

GitHub Actions example:

```yaml
name: karpathy-gate
on: [pull_request]
jobs:
  discipline:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - name: Complexity
        run: python scripts/complexity_checker.py $(git diff --name-only origin/main...HEAD)
      - name: Diff scope
        run: python scripts/diff_surgeon.py --base origin/main
      - name: Plan quality
        run: python scripts/goal_verifier.py --plan PLAN.md || true
```

Fail the job only on **new** violations relative to the base branch to avoid blocking legacy code.

## 3. Agent / tool integration

| Tool | Wiring |
|------|--------|
| Claude Code | `/karpathy-check` slash command; `karpathy-reviewer` sub-agent; plugin auto-loads principles via `CLAUDE.md` |
| Codex CLI | Add the principles to `AGENTS.md` |
| Cursor | `AGENTS.md` or `.cursorrules` |
| OpenCode / Gemini CLI | `AGENTS.md` |

Wire `complexity_checker.py` and `diff_surgeon.py` into the agent's pre-commit or post-edit step so violations surface during generation, not review.

## 4. Team adoption path

```
Week 1  Warn-only hook. No gates. Collect false positives.
Week 2  Tune thresholds; document accepted exceptions in the repo.
Week 3  CI runs warn-only on PRs; reviewers cite specific patterns.
Week 4  Enable blocking CI for new violations only (not legacy).
Ongoing Track violation counts as a trend, not a hard metric.
```

## 5. Thresholds and tuning

Start permissive and tighten:

| Checker | Initial | Tightened |
|---------|---------|-----------|
| Nesting depth | > 5 | > 4 |
| Cyclomatic complexity | > 15 | > 10 |
| Classes per file | > 3 | > 2 |
| Unused params | report | block |
| Diff noise ratio | > 30% | > 15% |

## 6. Reducing friction

- Scope checks to **changed lines**, never the whole repo.
- Provide an explicit escape hatch: `# karpathy: allow <reason>` on the offending line.
- Never block on style; block only on scope and complexity regressions.
- Keep every tool stdlib-only so it runs anywhere without installs.

## 7. Measuring success

- Fewer review comments about "why is this so big".
- Smaller, single-purpose diffs.
- New tests accompany behavior changes.
- Fewer reverts caused by unverified assumptions.
