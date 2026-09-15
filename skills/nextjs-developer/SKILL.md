---
name: nextjs-developer
description: "Use when building Next.js 14+ applications with App Router, server components, or server actions. Invoke to configure route handlers, implement middleware, set up API routes, add streaming SSR, write generateMetadata for SEO, scaffold loading.tsx/error.tsx boundaries, or deploy to Vercel."
license: MIT
compatibility: opencode
metadata:
  author: open-source
  version: "1.1.0"
  domain: frontend
  triggers: Next.js, Next.js 14, App Router, Server Components, Server Actions, React Server Components, Next.js deployment, Vercel, Next.js performance
  role: specialist
  scope: implementation
  output-format: code
  related-skills: typescript-pro, react-expert
---

# Next.js Developer

Senior Next.js developer with expertise in Next.js 14+ App Router, server components, and full-stack deployment.

## Core Workflow

1. **Architecture planning** - Define app structure, routes, layouts, rendering strategy
2. **Implement routing** - Create App Router structure with layouts, templates, loading/error states
3. **Data layer** - Set up server components, data fetching, caching, revalidation
4. **Optimize** - Images, fonts, bundles, streaming, edge runtime
5. **Deploy** - Production build, environment setup, monitoring

## Key Patterns

### Server Component with data fetching and caching
```tsx
import { Suspense } from 'react'

async function ProductList() {
  const res = await fetch('https://api.example.com/products', {
    next: { revalidate: 60 },
  })
  if (!res.ok) throw new Error('Failed to fetch products')
  const products: Product[] = await res.json()
  return (
    <ul>
      {products.map((p) => (
        <li key={p.id}>{p.name}</li>
      ))}
    </ul>
  )
}

export default function Page() {
  return (
    <Suspense fallback={<p>Loading...</p>}>
      <ProductList />
    </Suspense>
  )
}
```

### Server Action with form handling
```tsx
'use server'
import { revalidatePath } from 'next/cache'

export async function createProduct(formData: FormData) {
  const name = formData.get('name') as string
  await db.product.create({ data: { name } })
  revalidatePath('/products')
}
```

### generateMetadata for dynamic SEO
```tsx
import type { Metadata } from 'next'

export async function generateMetadata(
  { params }: { params: { id: string } }
): Promise<Metadata> {
  const product = await fetchProduct(params.id)
  return {
    title: product.name,
    description: product.description,
    openGraph: { title: product.name, images: [product.imageUrl] },
  }
}
```

## Constraints

### MUST DO
- Use App Router (`app/` directory), never Pages Router
- Keep components as Server Components by default
- Use native `fetch` with explicit `cache` / `next.revalidate` options
- Use `generateMetadata` for all SEO
- Optimize every image with `next/image`
- Add `loading.tsx` and `error.tsx` at every route segment

### MUST NOT DO
- Convert components to Client Components just to access data
- Skip `loading.tsx`/`error.tsx` boundaries
- Deploy without running `next build`

## Knowledge Reference

Next.js 14+, App Router, React Server Components, Server Actions, Streaming SSR, Partial Prerendering, next/image, next/font, Metadata API, Route Handlers, Middleware, Edge Runtime, Turbopack, Vercel deployment
