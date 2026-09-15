---
name: kilo
description: "Delegate coding to Kilo CLI (features, PRs). Optimized for token efficiency."
---\r\n\r\n# Kilo CLI Coding Assistant - Token Efficient

Use when you need to delegate coding tasks to Kilo CLI, an autonomous AI coding assistant that works in the terminal. Provides step-by-step guidance for setup, configuration, and usage with minimal token overhead.

## Trigger Conditions (Token-Optimized)
- User wants to use an AI coding assistant in the terminal/command line
- User specifically mentions "Kilo" or references the Kilo CLI
- User needs help configuring API keys for AI coding assistants
- User wants to run autonomous coding tasks from the command line

## Setup and Configuration (Minimal)

### 1. Check if Kilo is Installed
```bash
kilo --version
```

### 2. Configure API Credentials (One-Time)
Kilo requires API credentials to access AI models. Use environment variables for token efficiency:

```bash
# Set API key once (avoids repeated prompts)
export KILO_API_KEY="sk-..."
# Or configure in ~/.config/kilo/kilo.jsonc
```

### 3. Verify Configuration
```bash
kilo auth list
```

## Usage Patterns (Token-Saving)

### Interactive Mode (Use Sparingly)
Start Kilo in interactive mode only when multi-turn conversation is needed:
```bash
kilo
```

### With a Specific Prompt (PREFERRED - One-Shot)
Run Kilo with a direct instruction - single call, gets result:
```bash
kilo "Create a Python script that calculates Fibonacci numbers"
```

### Continue Previous Session (When Needed)
```bash
kilo --continue
```

### Specify Model (Token-Efficient)
```bash
kilo --model anthropic/claude-3-5-sonnet-20241022 "Explain quantum computing"
```

### Work with Specific Project
```bash
kilo ./my-project "Refactor this code to use dependency injection"
```

## Common Workflows (Token-Efficient)

### Code Generation (One-Shot)
1. Navigate to project directory
2. Run: `kilo "Create a REST API endpoint for user management"`
3. Review generated code (single output)
4. Iterate with follow-up ONLY if needed

### Debugging Assistance (One-Shot)
1. Run: `kilo "Why is this function returning null when input is valid?"`
2. Share relevant code snippets when prompted
3. Implement suggested fixes

### Code Review (One-Shot)
1. Run: `kilo "Review this code for security vulnerabilities and performance issues"`
2. Implement feedback if valid

## Token Optimization Tips

1. **One-shot is preferred** - Most tasks complete in a single Kilo call
2. **Specify model explicitly** - Use cheaper models for simple tasks
3. **Limit scope** - Be specific in prompts to reduce token usage
4. **Cache successful prompts** - Repeat patterns can reuse previous results
5. **Avoid interactive mode** unless truly needed - each turn adds overhead
6. **Use `--allowedTools` equivalent** - Though Kilo doesn't have this flag, being specific in prompts serves the same purpose
