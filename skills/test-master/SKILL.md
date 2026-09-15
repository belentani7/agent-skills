---
name: test-master
description: Generates test files, creates mocking strategies, analyzes code coverage, designs test architectures, and produces test plans and defect reports across functional, performance, and security testing disciplines.
license: MIT
compatibility: opencode
metadata:
  author: open-source
  version: "1.1.0"
  domain: quality
  triggers: test, testing, QA, unit test, integration test, E2E, coverage, performance test, security test, regression, test strategy
  role: specialist
  scope: testing
  output-format: report
  related-skills: code-reviewer, debugging-wizard, playwright-expert
---

# Test Master

Comprehensive testing specialist ensuring software quality through functional, performance, and security testing.

## Core Workflow

1. **Define scope** - Identify what to test and which testing types apply
2. **Create strategy** - Plan the test approach
3. **Write tests** - Implement tests with proper assertions
4. **Execute** - Run tests and collect results
5. **Report** - Document findings with severity ratings

## Quick-Start Example

```js
describe('calculateDiscount', () => {
  it('applies 10% discount for premium users', () => {
    const result = calculateDiscount({ price: 100, userTier: 'premium' });
    expect(result).toBe(90);
  });

  it('throws on negative price', () => {
    expect(() => calculateDiscount({ price: -1, userTier: 'standard' }))
      .toThrow('Price must be non-negative');
  });
});
```

## Constraints

### MUST DO
- Test happy paths AND error/edge cases
- Mock external dependencies
- Use meaningful `it('...')` descriptions
- Assert specific outcomes
- Run tests in CI/CD

### MUST NOT
- Skip error-path testing
- Use production data in tests
- Create order-dependent tests
- Ignore flaky tests
- Test implementation details

## Knowledge Reference

Jest, Vitest, pytest, React Testing Library, Playwright, Cypress, k6, Artillery, OWASP testing, coverage analysis, test automation
