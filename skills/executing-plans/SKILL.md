---
name: executing-plans
description: Use when you have a written implementation plan to execute in a separate session with review checkpoints
---

# Executing Plans

## Overview

Load plan, review critically, execute all tasks, report when complete.

**Announce at start:** "I'm using the executing-plans skill to implement this plan."

**Note:** Tell your human partner that Superpowers works much better with access to subagents (Claude Code, Codex CLI, Codex App, Copilot CLI, and Gemini CLI all qualify; see the per-platform tool refs in `../using-superpowers/references/`). If subagents are available, use superpowers:subagent-driven-development instead of this skill.

## The Process

### Step 1: Load and Review Plan
1. Ensure an isolated workspace: use superpowers:using-git-worktrees to create one or verify the existing one
2. Read plan file
3. Review critically - identify any questions or concerns about the plan
4. If concerns: Raise them with your human partner before starting
5. If no concerns: Create todos for the plan items and proceed

### Step 2: Execute Tasks

For each task:
1. Mark as in_progress
2. Follow each step exactly (plan has bite-sized steps)
3. Run verifications as specified
4. Mark as completed

### Step 3: Complete Development

After all tasks complete and verified:
- Announce: "I'm using the finishing-a-development-branch skill to complete this work."
- **REQUIRED SUB-SKILL:** Use superpowers:finishing-a-development-branch
- Follow that skill to verify tests, present options, execute choice

## When to Stop and Ask for Help

**STOP executing immediately when:**
- Hit a blocker (missing dependency, test fails, instruction unclear)
- Plan has critical gaps preventing starting
- You don't understand an instruction
- Verification fails repeatedly

**Ask for clarification rather than guessing.**

## Critical Pitfall: Audit ≠ Code Change

**An audit report is NOT a deliverable.** When a plan involves "audit and apply," the audit phase MUST produce actual file modifications — not just a markdown report.

### The Failure Pattern

```
1. Audit project → write AUDIT_REPORT.md
2. User asks: "What did you change?"
3. "I wrote an audit report..."
4. User: "There's nothing to commit!"
```

### The Fix

After auditing, immediately identify **which files can actually be modified** and make those changes:

1. **Audit** → extract findings
2. **Identify actionable changes** → which source files need modification?
3. **Apply changes** → use `write_file`/`patch` to make real edits to `.ts`, `.tsx`, `.json`, `.yaml`, etc.
4. **Commit & push** → `git add -A && git commit -m "..." && git push`
5. **Report the diff** → show `git diff --stat` as evidence of changes

### What Counts as a Change

| Action | Counts? |
|--------|---------|
| Writing an audit .md file | ❌ Not a code change |
| Reading and summarizing source files | ❌ Not a code change |
| Modifying `.ts`, `.tsx`, `.json`, `.yaml` files | ✅ Real change |
| Adding new source files | ✅ Real change |
| Updating config files | ✅ Real change |
| Committing and pushing | ✅ Real change |

### Verification

Before claiming "audit complete," verify with:
```bash
git diff --stat  # Must show modified files, not just new .md reports
```

If the only "change" is a new audit report file, the audit is incomplete — go back and apply actual code changes.

## When to Revisit Earlier Steps

**Return to Review (Step 1) when:**
- Partner updates the plan based on your feedback
- Fundamental approach needs rethinking

**Don't force through blockers** - stop and ask.

## Remember
- Review plan critically first
- Follow plan steps exactly
- Don't skip verifications
- Reference skills when plan says to
- Stop when blocked, don't guess
- Never start implementation on main/master branch without explicit user consent
