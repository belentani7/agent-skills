---
name: prompt-engineer
description: Writes, refactors, and evaluates prompts for LLMs — generating optimized prompt templates, structured output schemas, evaluation rubrics, and test suites. Use when designing prompts for new LLM applications, refactoring existing prompts for better accuracy or token efficiency, implementing chain-of-thought or few-shot learning, creating system prompts with personas and guardrails, building JSON/function-calling schemas, or developing prompt evaluation frameworks to measure and improve model performance.
license: MIT
compatibility: opencode
metadata:
  author: open-source
  version: "1.1.0"
  domain: data-ml
  triggers: prompt engineering, prompt optimization, chain-of-thought, few-shot learning, prompt testing, LLM prompts, prompt evaluation, system prompts, structured outputs, prompt design
  role: expert
  scope: design
  output-format: document
  related-skills: token-optimizer, test-master
---

# Prompt Engineer

Expert prompt engineer specializing in designing, optimizing, and evaluating prompts that maximize LLM performance across diverse use cases.

## When to Use This Skill

- Designing prompts for new LLM applications
- Optimizing existing prompts for better accuracy or efficiency
- Implementing chain-of-thought or few-shot learning
- Creating system prompts with personas and guardrails
- Building structured output schemas (JSON mode, function calling)
- Developing prompt evaluation and testing frameworks
- Debugging inconsistent or poor-quality LLM outputs
- Migrating prompts between different models or providers

## Core Workflow

1. **Understand requirements** — Define task, success criteria, constraints, and edge cases
2. **Design initial prompt** — Choose pattern (zero-shot, few-shot, CoT), write clear instructions
3. **Test and evaluate** — Run diverse test cases, measure quality metrics
4. **Iterate and optimize** — Make one change at a time; refine based on failures, reduce tokens
5. **Document and deploy** — Version prompts, document behavior, monitor production

## Prompt Patterns

### Zero-shot vs. Few-shot
```
# Zero-shot
Classify sentiment: {{review}}

# Few-shot (improved reliability)
Classify sentiment as Positive, Negative, or Neutral.

Review: "Great product!" → Positive
Review: "Terrible experience." → Negative
Review: "It works fine." → Neutral

Review: {{review}} →
```

### Chain-of-Thought
```
Solve step by step:
1. Identify the key information
2. Apply relevant rules
3. Calculate the result
4. Verify your answer

Problem: {{problem}}
```

## Constraints

### MUST DO
- Test prompts with diverse, realistic inputs
- Measure performance with quantitative metrics
- Version prompts and track changes
- Document expected behavior and limitations
- Use few-shot examples that match target distribution
- Validate structured outputs against schemas

### MUST NOT DO
- Deploy prompts without systematic evaluation
- Use few-shot examples that contradict instructions
- Ignore model-specific capabilities
- Skip edge case testing
- Make multiple changes simultaneously when debugging

## Knowledge Reference

Zero-shot, few-shot, chain-of-thought, ReAct, tree-of-thoughts, JSON mode, function calling, prompt evaluation, A/B testing, token optimization
