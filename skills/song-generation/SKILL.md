---
name: song-generation
description: "SongGeneration / LeVo - Open-source commercial-grade AI music generation by Tencent. Text-to-music with lyrics."
platforms: [linux, macos]
metadata:
  hermes:
    tags: [Music-Generation, AI-Music, Songwriting, Tencent, Lyrics]
---

# SongGeneration / LeVo - AI Music Generation

Open-source music foundation model by Tencent AI Lab. Commercial-grade quality rivaling Suno and Mureka.

## When to Use
- User wants to generate complete songs from text prompts
- User wants AI music composition with lyrics
- User needs multilingual music generation (zh, en, es, ja, etc.)
- User wants open-source alternative to Suno AI

## Key Features
- Commercial-grade musicality (rivals Suno v5, Mureka v8)
- Lyric accuracy: 8.55% PER (beats Suno v5 12.4%)
- Multilingual: Chinese, English, Spanish, Japanese, etc.
- Multi-preference alignment for melody, arrangement, sound quality
- Multi-modal conditioning: text + audio prompts

## Installation

```bash
git clone https://github.com/tencent-ailab/SongGeneration.git
cd SongGeneration
pip install -r requirements.txt
```

## Model Sizes

| Model | Max Length | VRAM | RTF(H20) | Languages |
|-------|-----------|------|----------|-----------|
| SongGeneration-base | 2m30s | 10-16GB | 0.67 | zh |
| SongGeneration-base-new | 2m30s | 10-16GB | 0.67 | zh, en |
| SongGeneration-base-full | 4m30s | 12-18GB | 0.69 | zh, en |
| SongGeneration-large | 4m30s | 22-28GB | 0.82 | zh, en |
| SongGeneration-v2-large | 4m30s | 22-28GB | 0.82 | zh, en, es, ja |

## Quick Start

### Download Model
```bash
# From HuggingFace
pip install huggingface_hub
huggingface-cli download lglg666/SongGeneration-v2-large --local-dir ./checkpoints/
```

### Generate Music
```python
from models import SongGenerationModel

model = SongGenerationModel.from_pretrained("./checkpoints/SongGeneration-v2-large")

result = model.generate(
    prompt="Upbeat pop song about summer love",
    lyrics="Summer nights, we dance in the moonlight",
    language="en"
)
result.save_audio("output.mp3")
```

## Parameters

| Parameter | Values | Description |
|-----------|--------|-------------|
| `prompt` | string | Music style/description |
| `lyrics` | string | Song lyrics |
| `language` | en, zh, es, ja | Output language |
| `temperature` | 0.5-1.5 | Creativity control |
| `top_k` | 10-100 | Sampling top-k |

## Online Demo
- Fast generation: https://huggingface.co/spaces/tencent/SongGeneration
- v2 fast model: generates a complete song in under 1 minute

## Related
- `heartmula`: Another open-source music foundation model
- `shao-music`: High-fidelity music generation
- `rvc`: Voice conversion for singing
