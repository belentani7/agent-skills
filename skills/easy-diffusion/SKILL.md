---
name: easy-diffusion
description: "EasyDiffusion - 1-click AI image generator with browser UI. Easy Stable Diffusion setup for beginners."
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Image-Generation, Stable-Diffusion, GUI, EasySetup]
---

# EasyDiffusion

1-click way to create beautiful artwork using AI with a browser UI. No tech knowledge required.

## When to Use
- User wants a simple GUI for AI image generation
- User is new to Stable Diffusion
- User wants a point-and-click interface
- User needs image generation without command line

## Installation

```bash
git clone https://github.com/easydiffusion/easydiffusion.git
cd easydiffusion
pip install -r requirements.txt
```

## Quick Start

```bash
python main.py --gui
```

Open browser at `http://localhost:9000` and start generating images.

## Features
- Browser-based UI
- Text-to-image and image-to-image
- Prompt editor with suggestions
- Built-in samplers and models
- Model manager
- Extension support

## Supported Models
- Stable Diffusion 1.5
- Stable Diffusion XL
- Stable Diffusion 2.x
- SDXL Turbo
- Flux (via community extensions)

## Key Settings

| Setting | Default | Description |
|---------|---------|-------------|
| `resolution` | 512x512 / 1024x1024 | Image dimensions |
| `sampler` | Euler A | Sampling method |
| `steps` | 20-30 | Inference steps |
| `cfg_scale` | 7-12 | Prompt adherence |
| `seed` | -1 (random) | Random seed |

## Related
- `comfyui`: Node-based workflow engine
- `flux-gen`: FLUX image generation models
- `stable-diffusion-webui`: Full web UI by AUTOMATIC1111
