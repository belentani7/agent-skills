---
name: flux-gen
description: "FLUX Image Generation by Black Forest Labs - State-of-the-art open image generation and editing."
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Image-Generation, FLUX, Stable-Diffusion, AI-Art]
---

# FLUX - Image Generation by Black Forest Labs

Open-weight image generation and editing models. FLUX.1 and FLUX.2 families.

## When to Use
- User wants to generate images from text prompts
- User wants image editing (inpainting, outpainting)
- User needs high-quality AI art generation
- User wants open-source alternative to Midjourney/DALL-E

## Models

| Model | License | VRAM | Best For |
|-------|---------|------|----------|
| FLUX.1 [schnell] | Apache 2.0 | 8GB+ | Fast text-to-image |
| FLUX.1 [dev] | Non-Commercial | 24GB+ | Maximum quality |
| FLUX.2 [klein] 4B | Apache 2.0 | 8GB+ | Real-time generation |
| FLUX.2 [klein] 9B | Non-Commercial | 16GB+ | High quality |
| FLUX.2 [dev] | Non-Commercial | 80GB+ | Pro quality |

## Installation

```bash
git clone https://github.com/black-forest-labs/flux.git
cd flux
pip install -r requirements.txt
```

## Quick Start

### FLUX.1 schnell (Apache 2.0)
```python
from diffusers import FluxPipeline
import torch

pipe = FluxPipeline.from_pretrained(
    "black-forest-labs/FLUX.1-schnell",
    torch_dtype=torch.bfloat16
)
pipe.to("cuda")

image = pipe("A beautiful sunset over mountains").images[0]
image.save("output.png")
```

### FLUX.2 klein 4B (Fastest, Apache 2.0)
```python
from diffusers import Flux2Pipeline
pipe = Flux2Pipeline.from_pretrained(
    "black-forest-labs/FLUX.2-klein-4B",
    torch_dtype=torch.bfloat16
)
image = pipe("A cyberpunk city at night").images[0]
```

## Key Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `guidance_scale` | 3.5-5.0 | Prompt adherence |
| `num_inference_steps` | 28-50 | Quality vs speed |
| `width` / `height` | 1024 | Resolution |
| `max_sequence_length` | 512 | Prompt length |

## Editing Modes
- **Inpainting**: Replace parts of an image
- **Outpainting**: Extend image boundaries
- **Multi-reference**: Use multiple reference images
- **Image-to-Image**: Transform existing images

## UI Options
- `easydiffusion`: 1-click GUI for Stable Diffusion
- `comfyui`: Node-based workflow editor
- `stable-diffusion-webui`: Full-featured web UI
