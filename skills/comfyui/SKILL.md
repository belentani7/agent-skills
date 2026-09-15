---
name: comfyui
description: "ComfyUI - Node-based AI workflow engine for image generation, voice synthesis, and video processing."
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [AI-Workflow, Node-Based, Image-Generation, ComfyUI, Automation]
---

# ComfyUI - Node-Based AI Workflow Engine

Visual node-based workflow editor for AI image generation, audio processing, and more. Connect any AI model into reusable workflows.

## When to Use
- User wants to build complex AI pipelines visually
- User needs to chain multiple AI models together
- User wants reusable workflow templates
- User needs batch AI processing

## Installation

```bash
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
pip install -r requirements.txt
```

## Quick Start

```bash
python execution/main.py --comfy-path ./
```

Open browser at `http://localhost:8188` for the visual workflow editor.

## Core Features
- Node-based visual workflow builder
- Drag and drop connections
- Batch processing
- Workflow saving/loading
- Custom node support
- Model management
- Live preview

## Common Workflows
- Image generation (SD, FLUX, etc.)
- Image-to-image
- Inpainting / Outpainting
- ControlNet conditioning
- Upscaling / Enhancement
- Video generation
- Audio processing
- Voice cloning pipelines
- RVC training workflows
- Song generation chains

## Node Categories
- **Loaders**: Load models, images, audio, video
- **Model**: Load and configure AI models
- **Sampler**: Configure generation parameters
- **Image**: Process and combine images
- **Audio**: Process audio files
- **Branch**: Conditional workflows
- **Group**: Organize nodes

## Custom Nodes
```bash
pip install comfyui-manager
# Then use the built-in Custom Nodes manager in the UI
```

## HeartMuLa ComfyUI Node
For music generation with HeartMuLa:
```python
# Custom node by benjiyaya
# pip install HeartMuLa_ComfyUI
```

## Related
- `flux-gen`: FLUX image generation
- `rvc`: Voice conversion
- `song-generation`: Music generation
- `heartmula`: Music generation with ComfyUI node
