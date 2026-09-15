---
name: heartmula
description: "HeartMuLa - Open-source music foundation model family by Fudan University. Music generation with lyrics."
platforms: [linux, macos]
metadata:
  hermes:
    tags: [Music-Generation, Open-Source, Fudan, HeartMuLa, Lyrics]
---

# HeartMuLa - Open-Source Music Foundation Models

Family of open-source music foundation models from Fudan University / MOSI.AI. Music generation conditioned on lyrics and tags.

## When to Use
- User wants open-source music generation
- User wants to generate music from lyrics
- User needs multilingual music generation
- User wants an alternative to Suno AI
- User wants to use ComfyUI for music generation

## Components

| Component | Description |
|-----------|-------------|
| **HeartMuLa** | Music language model (3B, 7B params) |
| **HeartCodec** | 12.5Hz music codec with high reconstruction fidelity |
| **HeartTranscriptor** | Whisper-based lyrics transcription model |
| **HeartCLAP** | Audio-text alignment model |

## Installation

```bash
git clone https://github.com/HeartMuLa/HeartMuLa.git
cd HeartMuLa
pip install -r requirements.txt
```

## Quick Start

### Download Models
```bash
# Music generation model
hf download HeartMuLa/HeartMuLa-oss-3B --local-dir ./ckpt
# Codec model
hf download HeartMuLa/HeartCodec-oss --local-dir ./ckpt
# Transcription model
hf download HeartMuLa/HeartTranscriptor-oss --local-dir ./ckpt
```

### Generate Music
```python
from examples import run_music_generation

run_music_generation(
    model_path="./ckpt/HeartMuLa-oss-3B",
    version="3B",
    lyrics_file="./assets/lyrics.txt",
    tags_file="./assets/tags",
    save_path="./assets/output.mp3",
    max_audio_length_ms=240000
)
```

## Parameters

| Parameter | Values | Description |
|-----------|--------|-------------|
| `--model_path` | path | Model checkpoint path |
| `--version` | 3B, 7B | Model size |
| `--topk` | 50 | Top-k sampling |
| `--temperature` | 1.0 | Sampling temperature |
| `--bf16` | true/false | BF16 precision |
| `--max_audio_length_ms` | 240000 | Max output duration |

## Languages Supported
- English
- Chinese
- Japanese
- Korean
- Spanish

## Licensing
- Apache 2.0 License (all models and code)

## ComfyUI Integration
- Custom node by benjiyaya: `HeartMuLa_ComfyUI`
- Enables visual music generation workflows

## Related
- `song-generation`: Tencent's SongGeneration/LeVo
- `rvc`: Voice conversion and singing
- `soulx-singer`: Singing voice synthesis
- `comfyui`: Node-based workflow engine
