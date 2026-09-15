---
name: javascript-pro
description: Writes, debugs, and refactors JavaScript code using modern ES2023+ features, async/await patterns, ESM module systems, and Node.js APIs.
license: MIT
compatibility: opencode
metadata:
  author: open-source
  version: "1.1.0"
  domain: language
  triggers: JavaScript, ES2023, async await, Node.js, vanilla JavaScript, Web Workers, Fetch API, browser API, module system
  role: specialist
  scope: implementation
  output-format: code
  related-skills: typescript-pro, fullstack-guardian
---

# JavaScript Pro

## Core Workflow

1. **Analyze requirements** - Review package.json, module system, Node version
2. **Design architecture** - Plan modules, async flows, error handling
3. **Implement** - Write ES2023+ code with proper patterns
4. **Validate** - Run linter, check for memory leaks
5. **Test** - Write comprehensive tests with 85%+ coverage

## Key Patterns

### Async/Await Error Handling
```js
async function fetchUser(id) {
  try {
    const response = await fetch(`/api/users/${id}`);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return await response.json();
  } catch (err) {
    console.error("fetchUser failed:", err);
    return null;
  }
}
```

### Optional Chaining & Nullish Coalescing
```js
const city = user?.address?.city ?? "Unknown";
```

### ESM Module Structure
```js
// utils/math.mjs
export const add = (a, b) => a + b;
export const multiply = (a, b) => a * b;

// consumer.mjs
import { add } from "./utils/math.mjs";
```

## Constraints

### MUST DO
- Use ES2023+ features exclusively
- Use optional chaining (`?.`) and nullish coalescing (`??`)
- Use async/await for all asynchronous operations
- Use ESM (`import`/`export`) for new projects
- Implement proper error handling with try/catch

### MUST NOT DO
- Use `var` (always use `const` or `let`)
- Use callback-based patterns (prefer Promises)
- Mix CommonJS and ESM in the same module
- Skip error handling in async functions
- Use synchronous I/O in Node.js

## Knowledge Reference

ES2023+, async/await, Promises, ESM/CJS, Web Workers, Fetch API, Node.js streams, Event Loop, memory management
