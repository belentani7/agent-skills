---
name: whadoa
description: >-
  Use when the user describes something they saw but cannot name — by how it looks, where they saw it, or what it was for — and expects identification: a file, photo, HTML page, video, repo, clone or dupe, local vs pushed artifact, or something possibly open-source or Anthropic/Claude-related.
---

# WHADOA — "What Was That Thing?" Identifier

## Overview
New developers often see something, forget its name, and describe it vaguely ("the HTML of those photos", "that black gallery thing"). WHADOA turns vague descriptions into exact identifications: name, type, location, and next action.

## When to Use
- User describes an artifact by appearance ("black page with 6 photos"), location ("it was on the Desktop", "in that chat"), or purpose ("it showed metrics") instead of naming it.
- User asks "find me X" where X is a fuzzy reference to files, images, videos, pages, repos, clones/dupes.
- User wonders about origin: open-source? Anthropic/Claude-related? local file vs pushed/deployed copy?

When NOT to use: user gives an exact filename, path, or URL — just open it directly.

## Identification Dimensions
Extract up to five dimensions from the message (in Spanish or English):
1. **APPEARANCE** — colors, layout, shapes, text fragments remembered.
2. **LOCATION** — screen, folder, chat/export, URL, "it was here yesterday".
3. **PURPOSE** — what it did or displayed.
4. **FORMAT-CLUES** — image, video, HTML, JS, repo, clone/dupe, zip, log.
5. **ORIGIN-CLUES** — open-source? Anthropic/Claude? local vs pushed vs deployed?

## Artifact Taxonomy
Map clues to types before searching:

| User says | Check |
|---|---|
| "foto(s)", image, screenshot, gallery | `*.png/jpg/webp`, gallery HTMLs with embedded/base64 images |
| "página", page, dashboard, GUI | `*.html` containing remembered text |
| video, clip, recording | `*.mp4/webm`, project folders |
| repo, clon, dupe, copia | duplicate filenames, `-copy`, `(1)`, `_backup`, git remotes |
| local vs push/subido | local path vs Downloads/Drive/remote URL |
| open source? | LICENSE, repo URL (github), package.json |
| Anthropic/Claude-related? | mentions of Claude, Anthropic, `claude-*` models, `.claude/` configs |

## Workflow
1. **Search local first** (fast, private): glob by likely names, then content-grep for remembered words inside likely file types. Exclude `node_modules`, caches.
2. **Confirm, don't assume**: read the top candidate (head only for huge files) and verify it matches ≥2 dimensions.
3. **Stale-index rule**: if a search hit doesn't open, re-list the parent directory — indexes lie, directories don't.
4. **Report**: exact path(s), what it is (type + one-line description), and the single most useful next action (open, move, deploy, edit).
5. **Ambiguous?** Present max 3 candidates with distinguishing detail + one short question. Never dump 50 paths without grouping.
6. **Not found?** Say so plainly with where you looked. Offer to create it (e.g. rebuild a missing gallery) only after confirming.

## Verification Rules
- Evidence before naming: quote the matched line or filename as proof.
- Never invent paths — every reported path must come from an actual listing or search hit.
- Base64/embedded content counts as "the HTML of those photos" even with no separate image files.
