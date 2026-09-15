---
name: explore
description: Explore unfamiliar code with semantic search when you don't know which files to read. Not needed for quick lookups where grep or a known file path gets you there.
metadata:
  author: morph
  version: "0.1.1"
  argument-hint: <question>
---

# Explore

Use the codebase_search tool to explore a codebase, this saves time and tokens.

## When To Use

- Broad questions like "how does this work?" or "where is X implemented?" in code you haven't mapped yet.
- You need entry points, data flow, or ownership of a behavior.
- Keyword grep is likely to miss the relevant files.

Skip it when you already know the file to read or the exact string to grep for.

## Steps

1. Translate the user question into a tight natural language question, or description of the functionality you're looking for.
2. Run 2-3 instances of the `codebase_search` tool against the repo root, for each use a different search_string so you can explore the codebase from multiple angles
3. Read the returned files/sections.
4. Summarize the flow with concrete file paths.

## Query Template

"Find the entry points and data flow for <X>. Include router/handlers, config, and tests."
