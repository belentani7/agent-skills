---
name: creative-web-algorithm
description: >-
  Build or refactor premium creative-web experiences from an existing codebase using an observe-first execution algorithm. Use for HTML/CSS/JS/WebGL landing pages, SaaS interfaces, parallax, image-to-motion, liquid glass/metal, chromatic effects, canvas scenes, boot state machines, and performance-sensitive interactive frontends. Triggers: "make this page 3D", "add WebGL", "creative landing page", "liquid glass UI", "Three.js scene", "interactive canvas", "parallax website", "SaaS hero section", "webGL portfolio", "shader effects", "particle system web", "chromatic aberration", "motion design web", "boot state machine", "creative web algorithm".
---

# Creative Web Algorithm v3.0

Transform **STATE A → STATE B** while preserving valid behavior, proving each significant change, and delivering a production-grade experience. Never begin by editing.

## Operating Contract (Inviolable)

1. **Observe before modifying.** Map the entire runtime before touching a single line.
2. **Never patch unknown runtimes, exported snapshots, iframes, or minified bundles** until execution model is fully mapped.
3. **Component decisions only:** Keep, Refactor, Replace, Remove, or mark Unknown. Never remove without evidence.
4. **Strict separation:** `RENDERING ≠ UI ≠ ANIMATION ≠ STATE ≠ ASSETS ≠ PERFORMANCE_POLICY`. Each layer has its own module, its own tests, its own lifecycle.
5. **Never claim a feature exists until it has been run and tested** in a real browser. Console + Network + Performance tabs required.
6. **Prefer reversible incremental migrations over rewrites.** Every change must be rollbackable in ≤1 commit.
7. **If the format prevents reliable development, extract/reconstruct the runtime first.** Stop, diagnose, rebuild the foundation before continuing.
8. **One owned render loop. One state machine. One source of truth for scene state.** No orphaned RAF handles, no duplicate loops.
9. **Memory is a first-class concern.** Every GPU resource, every listener, every timer must have an explicit disposal path.
10. **Accessibility is non-negotiable.** Every visual effect must have a reduced-motion fallback and keyboard/screen-reader equivalent.

---

## Phase 0 — OBSERVE (Zero Modifications)

**Goal:** Produce a complete Architecture Map before writing any code.

### Scan Checklist

| Category | What to inspect | Tool |
|----------|----------------|------|
| **Entry points** | HTML, JS modules, CSS entry, config files | `grep`, `find` |
| **Dependencies** | npm packages, CDN imports, dynamic imports | `package.json`, `import` statements |
| **DOM structure** | Element tree, canvas elements, iframes | DevTools, `document.querySelectorAll` |
| **CSS architecture** | Custom properties, animations, layout system | `grep` for `@keyframes`, `:root` |
| **JS modules** | Export/import graph, state management, store patterns | AST analysis |
| **Canvas/WebGL** | WebGL context, shader programs, render targets, framebuffers | `WEBGL_debug_renderer_info` |
| **Shaders** | Vertex/fragment source, uniform locations, texture bindings | File scan |
| **Assets** | Images, fonts, audio, video, models, with sizes and formats | File scan, `ls -lh` |
| **Loading/boot** | Sequence order, preloaders, skeleton screens, lazy loading | Code trace |
| **Iframes** | Embedded content, cross-origin, postMessage channels | DOM scan |
| **CSP** | Content-Security-Policy headers, nonce/hashes, restrictions | Network tab |
| **Timers/promises** | setInterval, setTimeout, Promise chains, microtasks | Code scan |
| **External resources** | APIs, CDNs, fonts, analytics, tracking | Network tab |
| **Event listeners** | Mouse, touch, scroll, keyboard, resize, custom events | Code scan, DevTools |
| **Performance** | FPS, frame time, memory, layout thrashing | Performance tab |
| **Network** | Requests, waterfalls, caching, compression | Network tab |

### Output: Architecture Map

```markdown
# Architecture Map — [Project Name]

## Entry Points
- [ ] Primary: [file] → [initialization sequence]
- [ ] Secondary: [file] → [purpose]

## Module Graph
- [module A] imports [B, C]
- [module B] exports [X, Y]
- [module C] depends on [D, E]

## State Management
- [ ] Single source of truth: [store/context/prop]
- [ ] Derived state: [computed values]
- [ ] Side effects: [saga/epic/effect]

## Render Architecture
- [ ] Primary renderer: [Three.js/Canvas2D/WebGL]
- [ ] Secondary renderers: [overlays, post-processing]
- [ ] Render loop ownership: [which module]

## Asset Pipeline
- [ ] Loading strategy: [lazy/eager/prefetch]
- [ ] Cache policy: [memory/disk/None]
- [ ] Fallback assets: [low-res/progressive]

## Performance Profile
- [ ] Current FPS: [target/described]
- [ ] Memory budget: [bytes]
- [ ] Frame budget: [ms]
- [ ] Bundle size: [KB]

## Known Issues
- [ ] [Issue description, evidence, impact]
```

### Dependency Graph (ASCII)
```
[Entry] → [Renderer] → [Scene] → [Camera]
              ↓              ↓
        [PostFX]        [Lights]
              ↓              ↓
        [UI Layer] ← [State Store]
              ↓
        [Animation] → [Assets]
```

---

## Phase 1 — CLASSIFY

**Goal:** Create a Component Decision Map with evidence for every component.

### Decision Categories

| Category | Criteria | Action |
|----------|----------|--------|
| **KEEP** | Functional, valuable, no structural issues | Leave untouched |
| **REFACTOR** | Valuable but structurally unsafe, hard to extend, or technically debt | Rewrite internals, preserve API |
| **REPLACE** | Unsuitable for target state with concrete evidence | Swap implementation, preserve interface |
| **REMOVE** | Redundant, broken, harmful with evidence | Delete + add migration note |
| **UNKNOWN** | Insufficient evidence to classify | Investigate → reclassify → act |

### Decision Record Format
```markdown
## Component Decision Map

### [Component Name]
- **Location:** [file:line]
- **Current state:** [working/broken/debt]
- **Evidence:** [test results, performance metrics, bug reports]
- **Decision:** KEEP / REFACTOR / REPLACE / REMOVE / UNKNOWN
- **Rationale:** [why this decision]
- **Risk if wrong:** [what breaks]
- **Reversibility:** [how to undo]

### [Next Component]
...
```

### Evidence Requirements
- **Performance data:** FPS benchmarks, memory snapshots, frame timing
- **Functional tests:** Unit tests passing/failing, integration test results
- **User feedback:** Bug reports, support tickets, analytics data
- **Code quality:** Cyclomatic complexity, bundle impact, coupling metrics

---

## Phase 2 — DETECT FAILURE MODES

**Goal:** For every issue, record `CAUSE → EFFECT → FIX`. Fix causes, not symptoms.

### Failure Mode Catalog

| Failure Mode | CAUSE | EFFECT | FIX |
|-------------|-------|--------|-----|
| **Infinite/duplicated loops** | RAF not cancelled, recursive setTimeout, missing break condition | CPU spike, battery drain, tab crash | Cancel RAF on unmount, use `useEffect` cleanup, add `requestID` tracking |
| **Duplicate listeners** | Event added in render without cleanup, closure scoping bug | Memory leak, double-fire, exponential growth | Use `AbortController`, `removeEventListener`, single subscription pattern |
| **Blocking initialization** | Synchronous asset load, blocking script, large bundle parse | White screen >3s, TTI degradation | Code splitting, lazy import, skeleton screen, streaming |
| **Failed promises** | Missing `.catch()`, unhandled rejection, race condition | Silent failure, zombie state | Always `.catch()`, use `Promise.allSettled`, add error boundaries |
| **Missing assets** | Broken URL, wrong path, CORS restriction | Fallback broken, layout shift | Verify paths, use `onError` handlers, preload critical assets |
| **Broken imports** | Circular dependency, missing module, wrong export | Runtime error, blank page | Fix import paths, use `eslint import/no-cycle`, tree-shake |
| **iframe/CSP conflicts** | CSP blocks inline scripts, iframe sandbox restrictions | Content blocked, security errors | Adjust CSP headers, use `sandbox` attribute carefully |
| **Memory leaks** | Orphaned listeners, unclosed connections, retained references | Gradual slowdown, OOM crash | `WeakRef` for caches, explicit dispose, DevTools memory profiling |
| **Excessive DPR** | `devicePixelRatio > 2` on high-DPI screens | GPU memory spike, frame drops | Cap DPR at `Math.min(window.devicePixelRatio, 2)` |
| **Reflow/repaint cost** | Layout thrashing, forced synchronous layouts | Jank, >16ms frame time | Batch DOM reads/writes, use `transform`/`opacity` only, `will-change` |
| **Runaway particles** | Unbounded particle count, no max cap, no culling | GPU overload, FPS collapse to <10 | Cap count, use LOD, frustum culling, GPU instancing |
| **Orphaned GPU resources** | Disposed but not freed textures, unreleased framebuffers | VRAM leak, context lost | Track all GPU handles, explicit `dispose()` on unmount |
| **Shader compilation stalls** | Many shaders compiled in one frame, large programs | Frame drop, jank | Precompile during loading, use `THREE.ShaderMaterial` warmup |
| **Network waterfall** | Sequential dependencies, unoptimized loading | Long TTI, slow perceived performance | Parallelize, prefetch, use HTTP/2+ push, CDN |

### Failure Mode Report
```markdown
## Failure Mode Analysis

### F-001: [Title]
- **Severity:** Critical / High / Medium / Low
- **CAUSE:** [root cause]
- **EFFECT:** [observable impact]
- **FIX:** [specific solution]
- **Evidence:** [data proving this]
- **Prevention:** [how to avoid in future]
```

---

## Phase 3 — DEFINE TARGET ARCHITECTURE

**Goal:** Create a maintainable, scalable structure with strict layer separation.

### Canonical Directory Structure
```text
project/
├── src/
│   ├── scene/              # Scene graph, objects, entities
│   │   ├── index.ts
│   │   ├── Camera.ts       # Camera management, transitions
│   │   ├── Lights.ts       # Lighting system
│   │   ├── Objects/        # Reusable 3D objects
│   │   │   ├── Indexed.ts  # Pre-registered geometries
│   │   │   └── Materials/  # Material definitions
│   │   └── Environment/    # Sky, fog, post-processing
│   ├── renderer/           # Renderer configuration, context
│   │   ├── index.ts
│   │   ├── WebGLContext.ts # Context creation, loss handling
│   │   └── PostFX/         # Bloom, SSAO, chromatic, etc.
│   ├── shaders/            # GLSL source code
│   │   ├── common.glsl
│   │   ├── vertex/
│   │   └── fragment/
│   ├── effects/            # Visual effects pipeline
│   │   ├── LiquidGlass.ts
│   │   ├── Chromatic.ts
│   │   ├── Haze.ts
│   │   └── Particles.ts
│   ├── animation/          # Animation system
│   │   ├── Animator.ts     # Main animation controller
│   │   ├── Tweens.ts       # Easing functions
│   │   └── Timeline.ts     # Sequenced animations
│   ├── ui/                 # HTML/CSS overlay layer
│   │   ├── components/
│   │   ├── styles/
│   │   └── state/          # UI state (separate from scene state)
│   ├── assets/             # Static assets, textures, models
│   │   ├── textures/
│   │   ├── models/
│   │   └── audio/
│   ├── state/              # Single source of truth for scene state
│   │   ├── Store.ts        # Centralized state management
│   │   └── selectors.ts    # Derived state
│   ├── utils/              # Shared utilities
│   │   ├── math.ts
│   │   ├── geometry.ts
│   │   └── helpers.ts
│   └── main.ts             # Entry point, boot sequence
├── tests/
│   ├── unit/
│   ├── integration/
│   └── visual/
├── public/
│   └── index.html
├── package.json
├── tsconfig.json
├── vite.config.ts
└── README.md
```

### Architecture Rules

1. **`RENDERING ≠ UI ≠ ANIMATION ≠ STATE ≠ ASSETS ≠ PERFORMANCE`** — Each module owns its domain, never crosses boundaries without explicit interfaces.
2. **Single source of truth** — Scene state lives in `state/Store.ts`. UI state lives in `ui/state/`. Never duplicate.
3. **Renderer is agnostic** — `renderer/` knows nothing about scene content. Scene provides geometries; renderer draws them.
4. **Animation is parameterized** — All motion derives from `time`, `delta`, `velocity`, `damping`, `easing`. Never hardcode frame counts.
5. **Assets are lazy** — Load on demand. Preload only critical path (<100KB).
6. **Effects are composable** — PostFX pipeline is a chain. Add/remove without affecting core render.
7. **Cleanup is mandatory** — Every module exports `dispose()`. Call it on unmount/context loss.

---

## Phase 4 — BUILD THE VISUAL SYSTEM

**Goal:** Create a layered scene graph with explicit depth, parallax, and motion policy.

### Scene Graph Layers (Front to Back)
```
┌─────────────────────────────────┐
│  UI LAYER                       │  ← HTML/CSS overlay, interactive controls
│  ─────────────────────────────  │
│  INTERACTION LAYER              │  ← Raycasting, pointer events, hover
│  ─────────────────────────────  │
│  PARTICLES LAYER                │  ← Atmospheric particles, ambient
│  ─────────────────────────────  │
│  SUBJECT LAYER                  │  ← Main 3D object, hero geometry
│  ─────────────────────────────  │
│  LIGHTING LAYER                 │  → Reflections, shadows, glow
│  ─────────────────────────────  │
│  ENVIRONMENT LAYER              │  → Sky, fog, ground, skybox
│  ─────────────────────────────  │
│  DEPTH LAYERS                   │  → Parallax planes, background depth
│  ─────────────────────────────  │
│  ATMOSPHERE LAYER               │  → Haze, fog, volumetric light
│  ─────────────────────────────  │
│  BACKGROUND LAYER               │  → Solid color, gradient, gradient
└─────────────────────────────────┘
```

### Layer Configuration
Each layer has explicit properties:
```typescript
interface LayerConfig {
  name: string;
  depth: number;           // 0.0 (back) to 1.0 (front)
  parallaxCoefficient: number; // 0.0 (static) to 1.0 (follows pointer)
  motionPolicy: 'static' | 'parallax' | 'animated' | 'interactive';
  opacity: number;         // 0.0 to 1.0
  visible: boolean;
  quality: 'high' | 'medium' | 'low';
}
```

### Parameterized Inputs
Route these same inputs to ALL visual layers:
- `time` — `clock.getElapsedTime()` — drives all animations
- `pointer` — `mouse.x, mouse.y` — drives parallax, hover, interaction
- `viewport` — `window.innerWidth/innerHeight` — drives resolution, scale
- `scroll` — `window.scrollY` — drives depth, reveals, transitions
- `delta` — `clock.getDelta()` — drives frame-rate-independent motion

**Anti-pattern:** Applying arbitrary transforms to every element and calling it "3D". Every transform must serve a visual purpose documented in the layer config.

---

## Phase 5 — BUILD THE MATERIAL SYSTEM SELECTIVELY

**Goal:** Choose materials hierarchically. Every effect must earn its place.

### Material Hierarchy

**Primary (One Dominant Effect):**
Choose ONE primary visual identity:
- **Liquid Glass:** `MeshPhysicalMaterial` with `transmission: 0.85`, `thickness: 0.5`, `ior: 1.5`, `clearcoat: 1.0`, `roughness: 0.05`. Creates refractive, reflective surfaces.
- **Liquid Metal:** `MeshPhysicalMaterial` with `metalness: 1.0`, `roughness: 0.0`, `color: [theme]`, `envMapIntensity: 2.0`. Creates mirror-like metallic surfaces.
- **Ethereal:** `MeshStandardMaterial` with `emissive`, `transparent`, `opacity: 0.3`, `wireframe: true`. Creates ghostly, sci-fi surfaces.
- **Neon Glow:** `MeshBasicMaterial` with `emissive`, `emissiveIntensity: 2.0`, `transparent: true`, `opacity: 0.8`. Creates glowing, holographic surfaces.

**Secondary (Supporting Effects):**
- **Reflection/Refraction:** Environment maps, `cubeCamera`, `refractionRatio`
- **Fresnel:** `FresnelMaterial` or custom shader with `dot(normal, viewDir)`
- **Displacement:** `displacementMap`, `displacementScale`, vertex displacement
- **Chromatic:** Custom shader with RGB channel offset based on view angle

**Atmospheric (Global Effects):**
- **Bloom:** `UnrealBloomPass` — strength 0.5-1.5, radius 0.4, threshold 0.85
- **Light Scatter:** `LensFlare`, `sprite` glow, `AdditiveBlending`
- **Haze:** `FogExp2` or custom depth-based fog
- **RGB Shift:** Custom post-process shader with chromatic aberration offset

### Material Decision Rules
1. **Never use a generated still image to cover or replace an existing animated canvas** unless explicitly requested by the user.
2. **Remove effects that do not improve composition.** If a bloom pass doesn't add visual value, remove it. If a chromatic effect distracts from the subject, kill it.
3. **One primary effect.** Supporting effects only earn their place if they enhance the primary without competing.
4. **Performance budget:** Primary material <2 shader compiles. Total post-processing <3 passes.

### Liquid Glass Implementation Template
```glsl
// Fragment shader for liquid glass
uniform float uTime;
uniform float uTransmission;
uniform vec3 uColor;
uniform float uIOR;

void main() {
  vec3 viewDir = normalize(vViewPosition);
  vec3 normal = normalize(vNormal);
  
  // Fresnel for edge glow
  float fresnel = pow(1.0 - dot(viewDir, normal), 3.0);
  
  // Transmission for refraction
  vec3 refracted = texture2D(uTransmissionMap, vUv).rgb;
  vec3 transmitted = mix(uColor, refracted, uTransmission);
  
  // Edge glow
  vec3 edgeGlow = vec3(0.0, 0.9, 0.97) * fresnel * 0.5;
  
  gl_FragColor = vec4(transmitted + edgeGlow, 0.85 + fresnel * 0.15);
}
```

---

## Phase 6 — BUILD DETERMINISTIC MOTION

**Goal:** All motion derives from parameterized inputs. Never hardcoded values.

### Motion Parameter System
```typescript
interface MotionParams {
  velocity: number;        // Base speed (units/sec)
  acceleration: number;    // Rate of change of velocity
  damping: number;         // Friction/decay (0-1)
  easing: 'linear' | 'easeIn' | 'easeOut' | 'easeInOut' | 'elastic' | 'bounce';
  depth: number;           // Z-depth parallax coefficient
  amplitude: number;       // Max displacement
  frequency: number;       // Oscillations per second
  phase: number;           // Time offset
}
```

### Routing Protocol
All inputs MUST route to ALL relevant transforms:
```
[time] → camera.transform, layer.transform, shader.uniforms, lighting.position, particle.velocity, UI.transition
[pointer] → camera.position (parallax), layer.parallax, object.rotation (follow)
[scroll] → camera.position (depth), layer.opacity (reveal), object.scale (approach)
[viewport] → renderer.dpr, camera.aspect, object.scale (responsive)
```

### Animation Loop Contract
```typescript
// ONE owned loop per renderer
class AnimationLoop {
  private rafId: number | null = null;
  private lastTime = 0;
  
  start() {
    const tick = (timestamp: number) => {
      const delta = timestamp - this.lastTime;
      this.lastTime = timestamp;
      this.update(delta, timestamp);
      this.rafId = requestAnimationFrame(tick);
    };
    this.rafId = requestAnimationFrame(tick);
  }
  
  stop() {
    if (this.rafId !== null) {
      cancelAnimationFrame(this.rafId);
      this.rafId = null;
    }
  }
  
  private update(delta: number, timestamp: number) {
    // Route delta to ALL systems:
    this.scene.update(delta);
    this.ui.update(delta);
    this.particles.update(delta);
    this.camera.update(delta);
  }
  
  dispose() {
    this.stop();
    // Clean up all listeners, observers, GPU resources
  }
}
```

**Rules:**
- Use `requestAnimationFrame` only through this ONE owned loop.
- Never create additional `setTimeout`, `setInterval`, or secondary RAF loops.
- Always provide `dispose()` that cleans up listeners, RAF handles, observers, and GPU resources.
- Use `clock.getDelta()` for frame-rate-independent motion. Never assume 60fps.

---

## Phase 7 — ENFORCE PERFORMANCE

**Goal:** Adaptive quality with explicit budgets and mobile-specific states.

### Quality Tiers
```typescript
enum Quality { HIGH = 'high', MEDIUM = 'medium', LOW = 'low' }

interface QualityConfig {
  dpr: number;                    // 2, 1.5, 1
  resolution: number;             // 1, 0.75, 0.5
  particleCount: number;          // 10000, 5000, 1000
  shadowMap: { size: number, enabled: boolean }; // 2048/1024/512
  postProcessing: { bloom: boolean, ssao: boolean, chromatic: boolean };
  animationFrequency: number;     // 60, 30, 15 fps cap
  textureSize: number;            // 1024, 512, 256
  geometryDetail: number;         // high/medium/low segment counts
}
```

### Quality Selection Logic
```typescript
function selectQuality(): Quality {
  const cores = navigator.hardwareConcurrency || 2;
  const memory = (navigator as any).deviceMemory || 4;
  const dpr = Math.min(window.devicePixelRatio, 2);
  const isMobile = /Mobi|Android/i.test(navigator.userAgent);
  const fps = getBaselineFPS(); // Measure initial FPS
  
  if (isMobile || cores < 4 || memory < 4 || fps < 30) return Quality.LOW;
  if (cores < 8 || memory < 8 || dpr > 1.5 || fps < 45) return Quality.MEDIUM;
  return Quality.HIGH;
}
```

### Degradation Cascade (Priority Order)
When performance degrades, reduce in this order:
1. **Atmospheric effects first** — bloom, haze, fog
2. **Particles second** — reduce count, simplify shader
3. **Shader resolution third** — lower texture sizes, fewer segments
4. **Preserve the primary composition** — the hero object must remain visible and coherent

### Performance Budgets
| Metric | HIGH | MEDIUM | LOW | Budget |
|--------|------|--------|-----|--------|
| Target FPS | 60 | 45 | 30 | ≥30 |
| Frame Time | ≤16ms | ≤22ms | ≤33ms | <33ms |
| Draw Calls | <100 | <50 | <25 | <50 |
| Triangles | <500k | <200k | <50k | <200k |
| Textures | 10MB | 5MB | 2MB | <10MB |
| Bundle | 500KB | 300KB | 150KB | <500KB |
| GPU Memory | <500MB | <250MB | <100MB | <500MB |

### Mobile State
Mobile is a **distinct lower-cost rendering state**, not merely a scaled desktop:
- Different geometry LODs (not just scaled down)
- Different particle systems (points vs. sprites)
- Different post-processing pipeline (no bloom on mobile)
- Touch-optimized interaction (no hover-dependent UI)
- Reduced shadow quality (no real-time shadows on LOW)

---

## Phase 8 — REAL LOADING STATE MACHINE

**Goal:** Explicit, deterministic loading with no arbitrary timeouts.

### State Machine
```
┌─────────────┐
│   BOOT      │  ← Entry point, initialize globals
└──────┬──────┘
       ↓
┌──────────────┐
│INITIALIZING  │  ← Setup modules, validate dependencies
└──────┬───────┘
       ↓
┌─────────────────┐
│LOADING_ASSETS   │  ← Load textures, models, audio, fonts
│(with progress)  │  ← Report progress to UI
└──────┬──────────┘
       ↓
┌───────────────────────┐
│INITIALIZING_RENDERER  │  ← Create WebGL context, compile shaders
└──────┬────────────────┘
       ↓
┌────────────┐
│   READY    │  ← All assets loaded, renderer initialized
└──────┬─────┘
       ↓
┌────────────┐
│  ENTERING  │  ← First render, transition in
└──────┬─────┘
       ↓
┌────────────┐
│   ACTIVE   │  ← Full interactive experience
└────┬───────┘
     ↓ (from any state)
┌─────────────────┐
│RECOVERABLE_ERROR│  ← Asset failed, context lost, etc.
└──────┬──────────┘
       ↓
┌────────────┐
│  FALLBACK  │  ← Graceful degradation, cached content, error UI
└──────┬─────┘
       ↓ (user action / retry)
┌────────────┐
│   ACTIVE   │  ← Retry successful
└────────────┘

SPECIAL: ENTERING → ACTIVE (skip, if no transition needed)
```

### State Implementation
```typescript
class LoadingStateMachine {
  state: State = 'BOOT';
  progress: number = 0;
  errors: Error[] = [];
  
  async transition(to: State) {
    const valid = this.allowedTransitions[this.state];
    if (!valid.includes(to)) throw new Error(`Invalid transition: ${this.state} → ${to}`);
    this.state = to;
    this.onStateChange(to);
  }
  
  async loadAssets(urls: string[], onProgress: (p: number) => void) {
    await this.transition('LOADING_ASSETS');
    const results = await Promise.allSettled(
      urls.map(url => fetch(url).then(r => r.blob()))
    );
    // Handle partial failures gracefully
    const successes = results.filter(r => r.status === 'fulfilled');
    const failures = results.filter(r => r.status === 'rejected');
    if (failures.length > 0 && successes.length === 0) {
      await this.transition('RECOVERABLE_ERROR');
    }
    this.progress = successes.length / urls.length;
  }
  
  // skip is ALWAYS safe and idempotent
  skip() {
    this.transition('ACTIVE'); // or FALLBACK if assets not loaded
  }
}
```

### Rules
- **Advance on actual asset/renderer readiness**, never an arbitrary timeout
- **Display actionable errors** — "Failed to load texture X. Retry?" not "Error 404"
- **Skip is always safe and idempotent** — calling skip twice does nothing bad
- **Enter → Active can skip** if assets are cached (service worker)
- **Any state → Recoverable Error → Fallback → Active** for error recovery

---

## Phase 9 — VERIFY AFTER EVERY SIGNIFICANT CHANGE

**Goal:** Run the full verification matrix. Never stack unverified patches.

### Verification Matrix
```
BUILD ──────────────────────────────
  → tsc --noEmit (or equivalent)
  → Rollup/Vite build succeeds
  → No TypeScript errors
  → No bundler warnings

RUN ────────────────────────────────
  → Opens in browser without errors
  → No console errors (0 critical)
  → No console warnings (0 new)
  → Network tab: all assets load (200 OK)
  → FPS ≥ target (≥30 minimum)

INSPECT CONSOLE ────────────────────
  → Zero errors
  → Zero warnings from our code
  → No deprecated API usage
  → No CORS violations
  → No CSP violations

TEST INTERACTION ───────────────────
  → Click/hover/touch all interactive elements
  → All event handlers fire correctly
  → No duplicate listener warnings
  → Scroll works without jank

TEST BOOT ──────────────────────────
  → Fresh load: BOOT → INITIALIZING → LOADING → RENDERER → READY → ENTERING → ACTIVE
  → Progress bar updates correctly
  → Skip button works from any state
  → Error state triggers correctly on failed asset

TEST SKIP ──────────────────────────
  → Skip from BOOT: works, shows fallback
  → Skip from LOADING_ASSETS: works, shows cached content
  → Skip from INITIALIZING_RENDERER: works, shows static content
  → Skip is idempotent: calling twice = calling once

TEST RESIZE ────────────────────────
  → Window resize: camera aspect updates
  → DPR change: renderer resize triggered
  → Mobile rotate: layout adapts
  → No layout shift (CLS < 0.1)

TEST MOBILE ────────────────────────
  → Touch events work
  → Quality = LOW selected automatically
  → Reduced motion respects prefers-reduced-motion
  → No hover-dependent UI visible
  → Touch target sizes ≥ 44px

TEST PERFORMANCE ───────────────────
  → Performance tab: no long tasks (>50ms)
  → Memory: no leak over 5 min session
  → GPU: no context lost events
  → Frame time: consistent (no spikes)

VISUAL QA ──────────────────────────
  → All layers render in correct order
  → Colors match design specification
  → Typography is legible at all sizes
  → Animations are smooth (60fps target)
  → No visual artifacts, flickering, or tearing
```

### On Failure Protocol
1. **Roll back the last change** (`git checkout` or revert)
2. **Identify the exact cause** (not the symptom — trace back)
3. **Modify ONE thing** (never multiple changes at once)
4. **Test again** (full verification matrix)
5. **Only then proceed** to next change

**Anti-pattern:** Stacking unverified patches. If something breaks, revert and debug one change at a time.

---

## Phase 10 — FINAL ACCEPTANCE

**Goal:** All success criteria met. "The page loads" is not success.

### Acceptance Checklist
- [ ] **Functional:** All features work as specified. No bugs. All states handled.
- [ ] **Visually coherent:** Design is consistent, colors match, typography is unified.
- [ ] **Performant:** All performance budgets met. FPS ≥ target. No jank.
- [ ] **Responsive:** Works on desktop, tablet, mobile. Layout adapts correctly.
- [ ] **Accessible:** Keyboard navigable, screen-reader friendly, `prefers-reduced-motion` respected, ARIA labels present.
- [ ] **Maintainable:** Clean architecture, documented code, modular structure, tests pass.
- [ ] **Demonstrated through verification loop:** All phases 9 tests pass.

### Final Deliverable Package
```
1. Source code (all files, clean, commented)
2. Architecture notes (Architecture Map, Decision Map)
3. Performance report (FPS, memory, frame time metrics)
4. Test results (verification matrix status)
5. Documentation (README, setup instructions, API docs)
6. Assets manifest (all files, sizes, formats)
7. Deployment guide (build commands, hosting config)
```

---

## Required First Response for Existing Projects

**Before writing ANY code, return ONLY:**

1. **Architecture Map** (Phase 0 output)
2. **Component Decision Map** (Phase 1 output)
3. **Failure Modes** (`CAUSE → EFFECT → FIX` from Phase 2)
4. **Target Architecture** (Phase 3 output — directory structure)
5. **Implementation Sequence** (ordered list of tasks, phase by phase)
6. **Risks** (what could go wrong, mitigation strategies)

**Then wait for explicit authorization unless the user has already authorized implementation.**

---

## Anti-Patterns Catalog (Never Do These)

| Anti-Pattern | Why It's Bad | Correct Approach |
|-------------|-------------|-----------------|
| Using `generated still image` to replace working canvas | Static content can't respond to interaction | Keep canvas animated, overlay image only as fallback |
| `requestAnimationFrame` in multiple modules | Frame conflicts, race conditions, double renders | ONE owned loop, all modules subscribe to it |
| Hardcoded animation frames (`for (let i=0; i<60; i++)`) | Tied to 60fps, breaks on slow devices | Use `clock.getDelta()` with parameterized time |
| Applying transforms to every element calling it "3D" | Visual noise, no depth, no purpose | Only transform elements that serve a visual layer purpose |
| Removing unknown components without evidence | Destroys potentially valuable code | Mark UNKNOWN, investigate, then decide |
| `setTimeout(() => { render() }, 1000)` for loading | Arbitrary, not tied to actual readiness | Use state machine with real asset progress |
| Memory leaks from unclosed GPU resources | Progressive slowdown, eventual crash | Explicit `dispose()` on every GPU handle |
| Ignoring `prefers-reduced-motion` | Accessibility violation, motion sickness | Always provide reduced-motion fallback |
| Scaling desktop to mobile (just CSS transform) | Poor touch targets, unreadable UI | Distinct mobile rendering state with LOD |
| Stacking unverified patches | Hard to debug, cascading failures | One change, verify, then next |

---

## Debugging Strategies

### Common Issues and Solutions

**Canvas is black / white:**
1. Check WebGL context: `canvas.getContext('webgl2')` — if null, browser doesn't support WebGL2
2. Check shader compilation: `renderer.debug.checkShaderErrors = true`
3. Check scene graph: `scene.children.length > 0` — empty scene renders black
4. Check camera position: camera must be outside the near plane and facing objects

**FPS drops suddenly:**
1. Check particle count: `scene.children.filter(c => c.isPoints).length`
2. Check shadow map: `renderer.shadowMap.enabled` — disable if not needed
3. Check draw calls: `renderer.info.render.calls` — >100 is suspicious
4. Check geometry: `geometry.attributes.position.count` — high vertex counts kill FPS

**Memory growing:**
1. Take heap snapshot before and after interaction
2. Check `renderer.info.memory.geometries`, `textures`, `programs`
3. Look for detached DOM elements (DevTools Memory panel)
4. Check for orphaned event listeners (no cleanup on unmount)

**Context lost:**
1. Listen: `canvas.addEventListener('webglcontextlost', handler)`
2. Save state, stop all loops
3. Attempt restore: `canvas.addEventListener('webglcontextrestored', handler)`
4. Rebuild scene from state snapshot, not from scratch

**Shader not compiling:**
1. `renderer.debug.checkShaderErrors = true`
2. Check uniform locations: `gl.getUniformLocation(program, name)` — null means not found
3. Check attribute locations: same pattern
4. Verify GLSL version matches renderer (GLSL 300 es for WebGL2)

---

## Tooling Recommendations

| Category | Tool | Purpose |
|----------|------|---------|
| **Build** | Vite | Fast bundling, HMR, TypeScript |
| **Testing** | Vitest | Unit/integration tests, fast |
| **Linting** | ESLint + TypeScript | Catch errors pre-runtime |
| **Formatting** | Prettier | Consistent code style |
| **3D Debug** | Three.js Studio / React Three Fiber | Visual scene inspection |
| **Profiling** | Chrome DevTools Performance + Memory | FPS, frame time, memory |
| **Network** | Chrome DevTools Network | Asset loading, waterfalls |
| **Type Checking** | `tsc --noEmit` | Static analysis |
| **Bundle Analysis** | `vite build --mode analyze` | Bundle size, tree-shaking |

---

## Code Templates

### Minimal Three.js Scene (Foundation)
```javascript
import * as THREE from "three";

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
document.body.appendChild(renderer.domElement);

const clock = new THREE.Clock();
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;

const animate = () => {
  const delta = clock.getDelta();
  const time = clock.getElapsedTime();
  controls.update();
  renderer.render(scene, camera);
  requestAnimationFrame(animate);
};
animate();

// Cleanup
window.addEventListener('beforeunload', () => {
  renderer.dispose();
  controls.dispose();
});
```

### Loading State Machine (Implementation)
```javascript
const STATES = ['BOOT', 'INITIALIZING', 'LOADING_ASSETS', 'INITIALIZING_RENDERER', 'READY', 'ENTERING', 'ACTIVE', 'RECOVERABLE_ERROR', 'FALLBACK'];
const ALLOWED = {
  BOOT: ['INITIALIZING'],
  INITIALIZING: ['LOADING_ASSETS', 'RECOVERABLE_ERROR'],
  LOADING_ASSETS: ['INITIALIZING_RENDERER', 'RECOVERABLE_ERROR'],
  INITIALIZING_RENDERER: ['READY', 'RECOVERABLE_ERROR'],
  READY: ['ENTERING'],
  ENTERING: ['ACTIVE', 'FALLBACK'],
  ACTIVE: ['RECOVERABLE_ERROR'],
  RECOVERABLE_ERROR: ['FALLBACK'],
  FALLBACK: ['ACTIVE'],
};

class StateMachine {
  constructor() { this.state = 'BOOT'; }
  async transition(to) {
    if (!ALLOWED[this.state]?.includes(to)) throw new Error(`Invalid: ${this.state} → ${to}`);
    this.state = to;
    this.onEnter(to);
  }
}
```

### Quality Adaptation Pattern
```javascript
function getConfig() {
  const isMobile = /Mobi|Android/i.test(navigator.userAgent);
  const cores = navigator.hardwareConcurrency || 2;
  const quality = isMobile || cores < 4 ? 'LOW' : cores < 8 ? 'MEDIUM' : 'HIGH';
  return QUALITY_PRESETS[quality];
}
```

---

## Compact Checklist

- [ ] **Observe before modify** — Architecture Map complete
- [ ] **Extract runtime** if snapshot/iframe/CSP prevents reliable work
- [ ] **One renderer loop, one state machine, explicit cleanup** — No orphaned resources
- [ ] **No static hero replacing working motion** — Everything animated or has purpose
- [ ] **One primary visual effect; supporting effects earn their place** — Material hierarchy respected
- [ ] **Adaptive quality and mobile state** — Not just scaled desktop
- [ ] **Boot/skip/error/resize/mobile tested** — Full verification matrix
- [ ] **Console and performance checked** — Zero errors, FPS on target
- [ ] **Accessible** — reduced-motion, keyboard, ARIA
- [ ] **Deliver source plus architecture notes when useful** — Documentation complete

---

## Version History

- **v3.0** — Added: Quality tiers with budgets, mobile distinct state, accessibility requirements, anti-patterns catalog, debugging strategies, tooling recommendations, code templates, performance budgets table, material hierarchy, error recovery paths, version history
- **v2.0** — Added: Liquid glass/metal material system, deterministic motion parameters, loading state machine implementation
- **v1.0** — Original: Observe → Classify → Detect → Architecture → Visual → Material → Motion → Performance → Loading → Verify → Accept
