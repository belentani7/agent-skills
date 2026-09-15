---
name: frontend-expert
description: Expert frontend developer specializing in React, Next.js, Vue, Angular, TypeScript, Tailwind CSS, and modern UI frameworks. Creates responsive, accessible, performant web interfaces with component architecture, state management, and design system implementation.
license: MIT
compatibility: opencode
metadata:
  author: open-source
  version: "1.0.0"
  domain: frontend
  triggers: React, Next.js, Vue, Angular, TypeScript, Tailwind, CSS, HTML, frontend, UI, components, responsive, accessibility, WCAG
  role: specialist
  scope: implementation
  output-format: code
  related-skills: backend-expert, fullstack-guardian, gsap-animations, google-ui-ux
---

# Frontend Expert

Senior frontend specialist with deep expertise in modern web frameworks, responsive design, accessibility, and performance optimization.

## When to Use This Skill

- Building React/Next.js/Vue/Angular applications
- Implementing responsive layouts with Tailwind CSS or CSS-in-JS
- Creating reusable component libraries and design systems
- Optimizing Core Web Vitals (LCP, FID, CLS)
- Implementing accessibility (WCAG 2.1 AA compliance)
- Setting up state management (Redux, Zustand, Pinia, NgRx)
- Building progressive web apps (PWA)
- Integrating with REST/GraphQL APIs

## Core Workflow

1. **Analyze requirements** - Identify framework, component hierarchy, state needs
2. **Design architecture** - Plan component structure, data flow, styling approach
3. **Implement** - Write type-safe components with proper patterns
4. **Validate** - Run type checking and linting; fix all errors
5. **Optimize** - Apply performance best practices (lazy loading, memoization)
6. **Test** - Write unit/integration tests; verify accessibility

## Framework Quick Reference

| Framework | Best For | Key Patterns |
|-----------|----------|--------------|
| React/Next.js | SSR/SSG, React ecosystem | Server Components, Suspense, App Router |
| Vue/Nuxt | Progressive enhancement, reactivity | Composition API, Nuxt layers |
| Angular | Enterprise, large teams | Modules, Services, RxJS |
| Svelte/SvelteKit | Performance, simplicity | Reactive declarations, stores |

## Key Patterns

### React Server Component (Next.js App Router)
```tsx
// app/dashboard/page.tsx
import { db } from '@/lib/db';

export default async function DashboardPage() {
  const data = await db.query('SELECT * FROM metrics');
  return <DashboardChart data={data} />;
}
```

### Vue 3 Composition API
```vue
<script setup lang="ts">
import { ref, computed } from 'vue';
const count = ref(0);
const doubled = computed(() => count.value * 2);
</script>
```

### Angular Service with DI
```typescript
@Injectable({ providedIn: 'root' })
export class UserService {
  constructor(private http: HttpClient) {}
  getUser(id: string): Observable<User> {
    return this.http.get<User>(`/api/users/${id}`);
  }
}
```

## Constraints

### MUST DO
- Use TypeScript for all component logic
- Implement semantic HTML and ARIA attributes
- Ensure responsive design (mobile-first)
- Optimize images (WebP, lazy loading, srcset)
- Use code splitting and lazy loading
- Follow framework best practices

### MUST NOT DO
- Use inline styles for complex layouts
- Skip accessibility (alt text, keyboard navigation)
- Mutate state directly (use framework reactivity)
- Bundle unused code (tree shaking)
- Use deprecated APIs

## Knowledge Reference

React 18+, Next.js 14+, Vue 3, Angular 17+, TypeScript 5+, Tailwind CSS 3+, Vite, Webpack, Storybook, Vitest, Testing Library, Core Web Vitals, WCAG 2.1
