# Creative Web Algorithm — Reference Pack

## Liquid Glass Material Recipe

```javascript
const liquidGlassMaterial = new THREE.MeshPhysicalMaterial({
  color: 0xffffff,
  metalness: 0.0,
  roughness: 0.05,
  transmission: 0.85,
  thickness: 0.5,
  ior: 1.5,
  envMapIntensity: 1.0,
  clearcoat: 1.0,
  clearcoatRoughness: 0.1,
  transparent: true,
  opacity: 0.9,
});
```

## Liquid Metal Material Recipe

```javascript
const liquidMetalMaterial = new THREE.MeshPhysicalMaterial({
  color: 0xcccccc,
  metalness: 1.0,
  roughness: 0.0,
  envMapIntensity: 2.0,
  clearcoat: 0.5,
  clearcoatRoughness: 0.1,
});
```

## Neon Glow Material Recipe

```javascript
const neonMaterial = new THREE.MeshBasicMaterial({
  color: 0xff003c,
  emissive: 0xff003c,
  emissiveIntensity: 2.0,
  transparent: true,
  opacity: 0.8,
});
```

## Bloom Pass Configuration

```javascript
const bloomPass = new UnrealBloomPass(
  new THREE.Vector2(window.innerWidth, window.innerHeight),
  0.8,   // strength
  0.4,   // radius
  0.85   // threshold
);
```

## Chromatic Aberration Shader

```glsl
uniform sampler2D tDiffuse;
uniform float uIntensity;
varying vec2 vUv;

void main() {
  vec2 offset = vec2(uIntensity, 0.0) * vUv;
  float r = texture2D(tDiffuse, vUv + offset).r;
  float g = texture2D(tDiffuse, vUv).g;
  float b = texture2D(tDiffuse, vUv - offset).b;
  gl_FragColor = vec4(r, g, b, 1.0);
}
```

## Loading Progress Bar CSS

```css
#loader {
  position: fixed; inset: 0; z-index: 9999;
  background: #0a0a0f;
  display: flex; align-items: center; justify-content: center;
  flex-direction: column; gap: 20px;
  transition: opacity 0.5s ease;
}
#loader.hidden { opacity: 0; pointer-events: none; }
#loader-bar {
  width: 300px; height: 4px; background: rgba(255,0,60,0.2);
  border-radius: 2px; overflow: hidden;
}
#loader-fill {
  height: 100%; background: linear-gradient(90deg, #ff003c, #ffd700);
  width: 0%; transition: width 0.3s ease;
}
```

## Quality Tier Configuration

```javascript
const QUALITY_PRESETS = {
  HIGH: {
    dpr: Math.min(window.devicePixelRatio, 2),
    resolution: 1.0,
    particleCount: 10000,
    shadowMap: { size: 2048, enabled: true },
    bloom: { strength: 0.8, radius: 0.4, threshold: 0.85 },
    postProcessing: ['bloom', 'ssao', 'chromatic'],
    textureSize: 1024,
    geometryDetail: 'high',
    animationFPS: 60,
  },
  MEDIUM: {
    dpr: 1.5,
    resolution: 0.75,
    particleCount: 5000,
    shadowMap: { size: 1024, enabled: true },
    bloom: { strength: 0.5, radius: 0.3, threshold: 0.85 },
    postProcessing: ['bloom'],
    textureSize: 512,
    geometryDetail: 'medium',
    animationFPS: 45,
  },
  LOW: {
    dpr: 1,
    resolution: 0.5,
    particleCount: 1000,
    shadowMap: { size: 512, enabled: false },
    bloom: { strength: 0, radius: 0, threshold: 0 },
    postProcessing: [],
    textureSize: 256,
    geometryDetail: 'low',
    animationFPS: 30,
  }
};
```

## Animation Easing Functions

```javascript
const Easing = {
  linear: t => t,
  easeIn: t => t * t * t,
  easeOut: t => 1 - Math.pow(1 - t, 3),
  easeInOut: t => t < 0.5 ? 4*t*t*t : 1 - Math.pow(-2*t+2, 3)/2,
  elastic: t => {
    if (t === 0 || t === 1) return t;
    return Math.pow(2, -10*t) * Math.sin((t*10-0.75)*(2*Math.PI)/3) + 1;
  },
  bounce: t => {
    const n1 = 7.5625, d1 = 2.75;
    if (t < 1/d1) return n1*t*t;
    else if (t < 2/d1) return n1*(t-=1.5/d1)*t+0.75;
    else if (t < 2.5/d1) return n1*(t-=2.25/d1)*t+0.9375;
    else return n1*(t-=2.625/d1)*t+0.984375;
  }
};
```

## Memory Management Checklist

```javascript
// Every GPU resource needs explicit disposal
function disposeScene(scene) {
  scene.traverse((object) => {
    if (object.geometry) object.geometry.dispose();
    if (object.material) {
      if (Array.isArray(object.material)) {
        object.material.forEach(m => m.dispose());
      } else {
        object.material.dispose();
      }
    }
    if (object.texture) object.texture.dispose();
  });
  renderer.dispose();
  if (renderer.domElement) {
    renderer.domElement.removeEventListener('webglcontextlost', ...);
  }
}

// Listener cleanup
function cleanupListeners(target, events) {
  events.forEach(([event, handler]) => {
    target.removeEventListener(event, handler);
  });
}

// Timer cleanup
function clearAllTimers(timerIds) {
  timerIds.forEach(id => clearTimeout(id));
  timerIds.length = 0;
}
```

## Error Boundary Pattern

```javascript
class ErrorBoundary {
  constructor(fallback) {
    this.fallback = fallback;
    this.state = 'ACTIVE';
  }
  
  catch(error) {
    console.error('[ErrorBoundary]', error);
    this.state = 'FALLBACK';
    this.renderFallback();
  }
  
  renderFallback() {
    const el = document.getElementById(this.fallback);
    if (el) el.style.display = 'flex';
  }
  
  reset() {
    this.state = 'ACTIVE';
    const el = document.getElementById(this.fallback);
    if (el) el.style.display = 'none';
  }
}
```

## Accessibility: Reduced Motion

```javascript
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

function shouldAnimate() {
  return !prefersReducedMotion.matches;
}

// Listen for changes
prefersReducedMotion.addEventListener('change', (e) => {
  if (e.matches) {
    // Stop all animations, freeze scene
    animationLoop.stop();
  } else {
    animationLoop.start();
  }
});
```

## Performance Monitoring Utility

```javascript
class PerformanceMonitor {
  constructor() {
    this.frames = [];
    this.lastTime = performance.now();
  }
  
  tick() {
    const now = performance.now();
    const delta = now - this.lastTime;
    this.frames.push(delta);
    this.lastTime = now;
    if (this.frames.length > 60) this.frames.shift();
  }
  
  getFPS() {
    if (this.frames.length === 0) return 0;
    return 1000 / (this.frames.reduce((a,b) => a+b, 0) / this.frames.length);
  }
  
  getAverageFrameTime() {
    return this.frames.reduce((a,b) => a+b, 0) / this.frames.length;
  }
  
  isJanky() {
    return this.getAverageFrameTime() > 33; // >30fps
  }
}
```

## Boot State Machine Template

```javascript
class BootStateMachine {
  static STATES = ['BOOT', 'INITIALIZING', 'LOADING_ASSETS', 'INITIALIZING_RENDERER', 'READY', 'ENTERING', 'ACTIVE', 'RECOVERABLE_ERROR', 'FALLBACK'];
  static TRANSITIONS = {
    BOOT: ['INITIALIZING'],
    INITIALIZING: ['LOADING_ASSETS', 'RECOVERABLE_ERROR'],
    LOADING_ASSETS: ['INITIALIZING_RENDERER', 'RECOVERABLE_ERROR'],
    INITIALIZING_RENDERER: ['READY', 'RECOVERABLE_ERROR'],
    READY: ['ENTERING'],
    ENTERING: ['ACTIVE', 'FALLBACK'],
    ACTIVE: ['RECOVERABLE_ERROR'],
    RECOVERABLE_ERROR: ['FALLBACK'],
    FALLBACK: ['ACTIVE']
  };
  
  constructor() {
    this.state = 'BOOT';
    this.progress = 0;
    this.errors = [];
  }
  
  async transition(to) {
    if (!BootStateMachine.TRANSITIONS[this.state]?.includes(to)) {
      throw new Error(`Invalid transition: ${this.state} → ${to}`);
    }
    this.state = to;
    this.onStateChange(to);
  }
}
```

## Three.js Import Map (CDN, Zero Install)

```html
<script type="importmap">
{
  "imports": {
    "three": "https://unpkg.com/three@0.160.0/build/three.module.js",
    "three/addons/": "https://unpkg.com/three@0.160.0/examples/jsm/"
  }
}
</script>
```

## Common Performance Anti-Patterns

| Anti-Pattern | Impact | Fix |
|-------------|--------|-----|
| `devicePixelRatio > 2` | GPU memory spike | Cap at `Math.min(dpr, 2)` |
| Unbounded particle count | GPU overload | Cap count, use LOD |
| Shadow maps on low-end | Frame drop | Disable on LOW quality |
| Multiple render passes | Frame budget exceeded | Max 3 post-processing passes |
| No geometry disposal | Memory leak | Explicit `geometry.dispose()` |
| RAF in multiple loops | Race conditions | ONE owned loop |
| Hardcoded frame counts | Device-dependent | Use `clock.getDelta()` |
| Loading all assets upfront | Long TTI | Lazy load, preload critical only |
