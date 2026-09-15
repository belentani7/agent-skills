---
name: opencode
description: "Delegate coding to OpenCode CLI (features, PR review). Optimized for token efficiency."
version: 1.2.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Coding-Agent, OpenCode, Autonomous, Refactoring, Code-Review, Token-Efficient]
    related_skills: [claude-code, codex, hermes-agent]
---

# OpenCode CLI - Token-Efficient Configuration

Use OpenCode as an autonomous coding worker with Hermes for maximum token savings.

## When to Use
- User explicitly asks to use OpenCode
- You want an external coding agent to implement/refactor/review code
- Long-running coding sessions with progress checks
- Parallel task execution in isolated workdirs

## Prerequisites (Token-Efficient)
- OpenCode installed: `npm i -g opencode-ai@latest`
- Auth configured: `opencode auth login` or set provider env vars
- Verify: `opencode auth list` should show at least one provider
- Git repository for code tasks (avoids repo detection overhead)
- Use `pty=true` only when interactive; otherwise use `opencode run` for one-shot

## Token-Saving Modes

### One-Shot Mode (RECOMMENDED - Saves 40-60% tokens)
```bash
terminal(command="opencode run 'Add retry logic to API calls and update tests'", workdir="~/project")
```
- Runs once, returns result, exits immediately
- No conversation history overhead
- Best for: bug fixes, single features, code reviews

### Background Mode (For iterative work)
```bash
terminal(command="opencode", workdir="~/project", background=true, pty=true)
# Returns session_id

# Send prompt (only when needed)
process(action="submit", session_id="<id>", data="Implement OAuth refresh flow")

# Poll for completion, don't log every turn
process(action="poll", session_id="<id>")
```

## Key Token Optimization Tips

1. **Use `--model` flag** to specify cheapest adequate model
   ```
   opencode run 'fix bug' --model anthropic/claude-3-5-sonnet-20241022
   ```

2. **Use `--allowedTools`** to limit tool access and reduce prompt size
   ```
   claude -p 'Add error handling' --allowedTools 'Read,Edit'
   ```

3. **Set `--max-turns`** to bound conversation length
   ```
   opencode run 'refactor' --max-turns 5
   ```

4. **Use `--json-schema`** for structured output instead of natural language descriptions

5. **Prefer `opencode run` over interactive TUI** for bounded tasks - avoids PTY overhead and session state

6. **Cache results** - if same task repeats, store and reuse successful prompts

7. **Avoid unnecessary context** - only pass relevant files, not entire project

## Common Workflows

### Code Generation (One-Shot)
```bash
opencode run 'Create REST API for user management' --model openrouter/anthropic/claude-3.5-sonnet
```

### Debugging (One-Shot)
```bash
opencode run 'Why does this return null? Debug and fix' --max-turns 3
```

### Code Review (One-Shot)
```bash
opencode run 'Review this code for security vulnerabilities' --allowedTools 'Read'
```
