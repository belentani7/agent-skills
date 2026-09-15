# Karpathy Principles — Context and Relaxation Guide

Deeper context behind the four principles, the observations that motivated them, and when to relax each.

## Origin

Derived from Andrej Karpathy's public observations on how LLMs fail at coding:

> "The models make wrong assumptions on your behalf and just run along with them without checking. They don't manage their confusion, don't seek clarifications, don't surface inconsistencies, don't present tradeoffs, don't push back when they should."

> "They really like to overcomplicate code and APIs, bloat abstractions, don't clean up dead code... implement a bloated construction over 1000 lines when 100 would do."

> "LLMs are exceptionally good at looping until they meet specific goals... Don't tell it what to do, give it success criteria and watch it go."

These are **failure modes of the model**, not general style preferences. Each principle targets one of them.

## Principle 1 — Think Before Coding

Targets: silent assumption-making and hidden confusion.

**In practice**
- Restate the task and list assumptions explicitly before editing.
- When the request is ambiguous, present the interpretations instead of choosing silently.
- Name tradeoffs (performance vs. simplicity, consistency vs. correctness).
- Stop and ask when a wrong assumption would be expensive to undo.

**Relax when** the task is mechanical and unambiguous (rename a symbol, fix a typo, apply a known pattern).

## Principle 2 — Simplicity First

Targets: over-engineering and speculative abstraction.

**In practice**
- Write the minimum that satisfies the requirement.
- No abstractions for single-use code, no config that wasn't asked for.
- No error handling for conditions that cannot occur.
- Delete scaffolding you added while exploring.

**The test:** Would a senior engineer call this overcomplicated? If yes, simplify.

**Relax when** the requirement is genuinely extensible by design (a public library API, a documented plugin point) — then some structure is warranted.

## Principle 3 — Surgical Changes

Targets: drive-by refactors, formatting churn, and scope creep in diffs.

**In practice**
- Every changed line should trace to the request.
- Match surrounding style even if you'd write it differently.
- Do not "improve" adjacent code or reformat untouched blocks.
- Mention unrelated dead code; do not delete it unasked.
- Remove only the imports/variables your change made unused.

**Relax when** the user explicitly asks for a refactor or cleanup.

## Principle 4 — Goal-Driven Execution

Targets: vague plans that cannot be verified.

**In practice**
- Convert instructions into success criteria.
- Prefer a failing test that reproduces the bug, then make it pass.
- For multi-step work, state a plan with a verification per step.
- Loop until the criterion is met; don't stop at "looks right".

| Instead of | Transform to |
|---|---|
| "Add validation" | "Write tests for invalid inputs, then make them pass" |
| "Fix the bug" | "Write a test that reproduces it, then make it pass" |
| "Refactor X" | "Ensure tests pass before and after" |

**Relax when** no automated check is feasible (exploratory spikes, UI polish) — then define a manual acceptance check.

## Decision summary

| Situation | Apply strongly |
|-----------|----------------|
| >20 lines changed | All four |
| Code you don't fully understand | 1, 4 |
| Multi-step, unclear requirements | 1, 4 |
| Reviewed by humans | 3 |
| Public/API surface | 2 (balanced) |
| Trivial one-liner / typo | Use judgment |

These principles bias toward **caution over speed**. On trivial tasks, judgment overrides process.
