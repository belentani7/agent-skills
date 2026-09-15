# karpathy-coder

Use when writing, reviewing, or committing code to enforce Karpathy's 4 coding principles — surface assumptions before coding, keep it simple, make surgical changes, define verifiable goals. Triggers on "review my diff", "check complexity", "am I overcomplicating this", "karpathy check", "before I commit", or any code quality concern where the LLM might be overcoding.

## Installation

### Claude Code
```bash
cp -r karpathy-coder ~/.claude/skills/
```

### MiMoCode / OpenCode
```bash
cp -r karpathy-coder ~/.opencode/skills/
```

### Cursor
Add to your project's CLAUDE.md:
```markdown
Load the karpathy-coder skill from ~/.opencode/skills/karpathy-coder/SKILL.md
```

## License

MIT
