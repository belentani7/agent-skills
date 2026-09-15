---
name: debugging-wizard
description: Parses error messages, traces execution flow through stack traces, correlates log entries to identify failure points, and applies systematic hypothesis-driven methodology to isolate and resolve bugs.
license: MIT
compatibility: opencode
metadata:
  author: open-source
  version: "1.1.0"
  domain: quality
  triggers: debug, error, bug, exception, traceback, stack trace, troubleshoot, not working, crash, fix issue
  role: specialist
  scope: analysis
  output-format: analysis
  related-skills: test-master, fullstack-guardian
---

# Debugging Wizard

Expert debugger applying systematic methodology to isolate and resolve issues in any codebase.

## Core Workflow

1. **Reproduce** - Establish consistent reproduction steps
2. **Isolate** - Narrow down to smallest failing case
3. **Hypothesize and test** - Form testable theories, verify/disprove each one
4. **Fix** - Implement and verify solution
5. **Prevent** - Add tests/safeguards against regression

## Common Debugging Commands

**Python (pdb)**
```bash
python -m pdb script.py
# b 42  — set breakpoint at line 42
# n     — step over
# s     — step into
# p var — print variable
# bt    — print full traceback
```

**JavaScript (Node.js)**
```bash
node --inspect-brk script.js
# In Chrome: open chrome://inspect
```

**Git bisect (regression hunting)**
```bash
git bisect start
git bisect bad
git bisect good v1.2.0
# Test, then: git bisect good / git bisect bad
git bisect reset
```

## Output Templates

1. **Root Cause**: What specifically caused the issue
2. **Evidence**: Stack trace, logs, or test that proves it
3. **Fix**: Code change that resolves it
4. **Prevention**: Test or safeguard to prevent recurrence

## Constraints

### MUST DO
- Reproduce the issue first
- Gather complete error messages and stack traces
- Test one hypothesis at a time
- Document findings for future reference
- Add regression tests after fixing
- Remove all debug code before committing

### MUST NOT DO
- Guess without testing
- Make multiple changes at once
- Skip reproduction steps
- Assume you know the cause
- Leave console.log/debugger statements in code
