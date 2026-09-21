---
name: aider
description: "Delegate coding to Aider (code editor AI pair programming). Optimized for token efficiency."
---
# Aider - Token Efficient Configuration

Delegate coding tasks to Aider, the AI pair programmer that works in your editor/terminal with minimal token overhead.

## When to Use
- User wants AI pair programming in the terminal
- Multi-file code edits with coherent context
- Refactoring across multiple files
- Natural language code modifications

## Prerequisites (Token-Efficient)
- Aider installed: `pip install aider-coding-assistant` or `pip install aider`
- Auth configured: Set OPENAI_API_KEY or other supported provider
- Verify: `aider --model` should show available models
- Git repository recommended for full context

## Token-Saving Modes

### One-Shot Mode (RECOMMENDED - Saves 50-70% tokens)
```bash
aider --model gpt-4o-mini "Add logging to all API endpoints" --edit src/api.py
```
- Single command, single edit pass
- No conversation history overhead
- Best for: single-file changes, simple additions

### Multi-Turn Mode (Only when needed)
```bash
aider --model gpt-4o-mini
# Then send prompts as needed
```
- Use only for complex multi-file refactoring
- Each turn adds token overhead

## Key Token Optimization Tips

1. **Use smaller models for simple tasks**
   ```
   aider --model gpt-4o-mini "Fix indentation in utils.py"
   ```

2. **Limit file scope**
   ```
   aider --model gpt-4o-mini "Fix bug in calculate.py" --file calculate.py
   ```

3. **Use --edit for specific files only**
   ```
   aider "Refactor auth module" --edit auth.py main.py
   ```

4. **Batch multiple small edits in one session** rather than multiple single-edit sessions

5. **Prefer `aider --send` with specific prompts** over interactive conversation when possible

6. **Use `--model` flag** to select cost-effective model per task complexity

7. **Cache successful edit patterns** - repeatable changes can reuse successful prompts

## Common Workflows (Token-Efficient)

### Single File Edit (One-Shot)
```bash
aider --model gpt-4o-mini "Add type hints to calculate.py" --file calculate.py
```

### Multi-File Refactoring (Minimal Turns)
```bash
aider --model gpt-4o-mini "Extract calculation logic to utils module" --edit utils.py calc.py
```

### Bug Fix (One-Shot)
```bash
aider --model gpt-4o-mini "Fix null reference in user_service.py" --file user_service.py
```

## Cost-Per-Task Guide

| Task Complexity | Recommended Model | Expected Tokens |
|----------------|------------------|-----------------|
| Simple fix/edit | gpt-4o-mini / claude-3.5-haiku | 500-2000 |
| Medium complexity | gpt-4o / claude-3.5-sonnet | 2000-5000 |
| Complex refactoring | gpt-4o / claude-3.5-sonnet-4 | 5000-15000 |
| Agentic multi-file | Claude 3.5 Sonnet or better | 15000+ |
