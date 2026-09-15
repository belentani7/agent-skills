#!/usr/bin/env node
// creative-web-algorithm — Build Verification Script
// Run: node scripts/verify-build.js
// Purpose: Automated verification of creative-web project health

import { execSync } from 'child_process';
import { existsSync } from 'fs';

const checks = [];

function check(name, command, expected) {
  try {
    const output = execSync(command, { encoding: 'utf-8', timeout: 30000 });
    const passed = expected ? output.includes(expected) : output.length > 0;
    checks.push({ name, passed, output: output.trim().slice(0, 100) });
  } catch (e) {
    checks.push({ name, passed: false, output: e.message.slice(0, 100) });
  }
}

function report() {
  const passed = checks.filter(c => c.passed).length;
  const total = checks.length;
  console.log(`\n=== BUILD VERIFICATION ===\n`);
  checks.forEach(c => {
    console.log(`  ${c.passed ? '✅' : '❌'} ${c.name}`);
    if (!c.passed) console.log(`     ${c.output}`);
  });
  console.log(`\n  Result: ${passed}/${total} checks passed\n`);
  process.exit(passed === total ? 0 : 1);
}

// TypeScript check
check('TypeScript', 'npx tsc --noEmit 2>&1', '');

// Build check
check('Build', 'npm run build 2>&1', '');

// Lint check
check('Lint', 'npm run lint 2>&1', '');

// Bundle size check
if (existsSync('dist/bundle.js')) {
  const stats = execSync('stat -f%z dist/bundle.js 2>/dev/null || stat -c%s dist/bundle.js 2>/dev/null', { encoding: 'utf-8' });
  const size = parseInt(stats.trim());
  checks.push({ name: 'Bundle Size', passed: size < 500000, output: `${(size/1024).toFixed(1)}KB (target: <500KB)` });
}

// WebGL check (requires browser context - skip in CI)
check('WebGL Context', 'node -e "const canvas = document.createElement(\'canvas\'); console.log(canvas.getContext(\'webgl2\') ? \'supported\' : \'unsupported\')" 2>&1', '');

report();
