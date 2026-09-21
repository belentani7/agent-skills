---
name: mimo
description: "Code manipulation and AI-assisted development. Optimized for token efficiency."
---
# Mimo - Token Efficient Development Assistant

Mimo is a code manipulation and AI-assisted development tool that provides efficient code generation, editing, and refactoring capabilities with minimal token overhead.

## When to Use
- User wants code generation or manipulation
- AI-assisted development in terminal
- Code editing with context awareness
- Rapid prototyping

## Prerequisites (Token-Efficient)
- Mimo installed: Check via `mimo --version` or install as needed
- API configuration as required by underlying model
- Verify installation before use

## Token-Saving Modes

### One-Shot Mode (RECOMMENDED - Saves 40-60% tokens)
```bash
mimo "Generate Python class for user authentication" --model auto
```
- Single command, gets result immediately
- No conversation history overhead
- Best for: code generation, single-file tasks

### Batch/Mode Selection
Use appropriate mode based on task complexity:
- Simple generation: one-shot command
- Complex multi-file: may need iterative approach

## Key Token Optimization Tips

1. **Use `mimo` with specific, bounded prompts**
   ```
   mimo "Create a function that sorts a list" --language python
   ```

2. **Specify language/framework when possible** to reduce model confusion
   ```
   mimo "Add React hook for state management" --framework react
   ```

3. **Prefer direct commands over interactive mode** when task is well-defined

4. **Cache successful generation patterns** - repeatable code patterns can be reused

5. **Use appropriate model for task size** - smaller models for simple tasks

## Common Workflows (Token-Efficient)

### Code Generation (One-Shot)
```bash
mimo "Generate a REST API endpoint handler" --language python
```

### Code Editing (One-Shot)
```bash
mimo "Add error handling to the auth function" --file src/auth.py
```

### Feature Implementation (Bounded Iteration)
```bash
mimo "Add user login endpoint" --language javascript --framework express
# Review output, iterate once if needed
```

## Cost Optimization

1. **One-shot is preferred** - Most completed in single command
2. **Specify language/framework** - Reduces token waste on context setting
3. **Avoid open-ended prompts** - Be specific about what to generate/modify
4. **Use model selection** if available for your setup
