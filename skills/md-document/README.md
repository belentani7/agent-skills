# md-document

Converts long-form markdown (specs, RFCs, reports, plans, explainers) into a single-file, lightly-interactive HTML document with sticky TOC, scrollspy, search filter, code-copy buttons, and design-system-driven brand tokens. Triggers when the markdown-html-orchestrator classifies an input as DOCUMENT, or when invoked directly via /cs:md-document. Reads the design-system config via config_loader.py and inlines the user's 12 derived CSS custom properties; refuses to render if onboarding hasn't run. Single-file output — Google Fonts + Prism.js CDN are the only externals; no framework runtime, no build step. Use after orchestrator routing or after design-system onboarding is confirmed.

## Installation

### Claude Code
```bash
cp -r md-document ~/.claude/skills/
```

### MiMoCode / OpenCode
```bash
cp -r md-document ~/.opencode/skills/
```

### Cursor
Add to your project's CLAUDE.md:
```markdown
Load the md-document skill from ~/.opencode/skills/md-document/SKILL.md
```

## License

MIT
