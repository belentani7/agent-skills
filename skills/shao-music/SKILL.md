---
name: shao-music
description: "Shao - High-fidelity music generation by unified acoustic-token pipeline. Open-source complete music works."
platforms: [linux]
metadata:
  hermes:
    tags: [Music-Generation, High-Fidelity, Acoustic-Token, Open-Source]
---

# Shao - High-Fidelity Music Generation

Open-source system for high-fidelity music generation using unified acoustic-token pipeline. Generates complete musical works from text descriptions and lyrics.

## When to Use
- User needs the highest quality open-source music generation
- User wants complete musical works (not just loops)
- User wants text + lyric controlled music
- User has NVIDIA GPU with 24GB+ VRAM

## Key Features
- Unified acoustic-token representation
- 64-layer RVQ acoustic token hierarchy
- Two-stage generation pipeline
- Complete musical works (not short clips)
- Text and lyric control
- Coarse-to-fine acoustic detail generation

## Requirements
- NVIDIA GPU with 24GB+ VRAM (RTX 4090 or higher)
- Docker and NVIDIA Container Toolkit
- CUDA-compatible NVIDIA driver
- Python and Node.js

## Installation

```bash
git clone https://github.com/Shao-Music-AI/Shao.git
cd Shao
# Follow ENVIRONMENT_SETUP.md for Docker setup
```

## Quick Start

```bash
# Docker-based inference
docker build -t shao .
docker run --gpus all -it shao
```

## Architecture

| Stage | Description |
|-------|-------------|
| Backbone | Generates coarse acoustic tokens |
| Super-Resolution | Completes higher RVQ token layers |
| Decoder | Reconstructs audio waveform |

## Online Demo
- https://shao-music-ai.github.io/Shao-demo/

## Model Weights
- HuggingFace: liujiafeng/Shao-MusicGeneration-v1.0
- arXiv: https://arxiv.org/abs/2605.01790

## Related
- `song-generation`: Tencent SongGeneration/LeVo
- `heartmula`: HeartMuLa music models
- `rvc`: Voice conversion and singing
