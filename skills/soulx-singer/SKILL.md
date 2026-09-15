---
name: soulx-singer
description: "SoulX-Singer - Zero-shot singing voice synthesis by Soul AI Lab. Generate singing voices for any unseen singer."
platforms: [linux, macos]
metadata:
  hermes:
    tags: [Singing-Voice-Synthesis, SVS, Zero-Shot, Voice, Music]
---

# SoulX-Singer - Zero-Shot Singing Voice Synthesis

High-fidelity zero-shot singing voice synthesis by Soul AI Lab (Shanghai Jiao Tong University). Generate realistic singing voices for any unseen singer.

## When to Use
- User wants to generate singing voices from any reference
- User wants to clone a singer's voice
- User needs melody-conditioned singing synthesis
- User wants MIDI-based singing control
- User needs singing voice conversion (SVC)

## Key Features
- Zero-shot singing voice synthesis (no fine-tuning needed)
- Melody (F0) and Score (MIDI) conditioning
- Timbre cloning across languages and styles
- Singing voice editing (modify lyrics keeping prosody)
- Cross-lingual synthesis
- Audio-to-Audio SVC (no transcription needed)
- 42,000+ hours of aligned vocals, lyrics, notes
- Languages: Mandarin, English, Cantonese

## Installation

```bash
git clone https://github.com/Soul-AILab/SoulX-Singer.git
cd SoulX-Singer
pip install -r requirements.txt
```

## Quick Start

### Download Models
```bash
# SVS and SVC models
hf download Soul-AILab/SoulX-Singer --local-dir pretrained_models/SoulX-Singer
# Preprocessing models
hf download Soul-AILab/SoulX-Singer-Preprocess --local-dir pretrained_models/SoulX-Singer-Preprocess
```

### Generate Singing Voice
```python
from soulx_singer import SoulXSingerv1

model = SoulXSingerv1.from_pretrained("./pretrained_models/SoulX-Singer")

# Zero-shot singing from lyrics and reference voice
audio = model.synthesize(
    lyrics="Your lyrics here",
    melody_reference="reference_singing.wav",
    voice_reference="target_singer.wav"
)
audio.save("output.wav")
```

### Singing Voice Conversion (SVC)
```python
# Convert source singing to target voice
audio = model.svc(
    source_audio="source_singing.wav",
    target_reference="target_voice.wav",
    midi_transcribe=False  # Audio-to-audio, no transcription needed
)
audio.save("converted.wav")
```

## Parameters

| Parameter | Values | Description |
|-----------|--------|-------------|
| `lyrics` | string | Song lyrics |
| `melody_reference` | path | F0/melody reference audio |
| `voice_reference` | path | Target singer voice reference |
| `control_mode` | melody, score | F0 contour or MIDI notes |
| `midi_transcribe` | bool | Whether to use MIDI transcription |

## Related
- `rvc`: Voice conversion and singing synthesis
- `heartmula`: Open source music generation
- `ycing-music-singer`: Another singing voice synthesis model
- `tcsinger2`: Multilingual singing voice synthesis
