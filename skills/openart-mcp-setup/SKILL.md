---
name: openart-mcp-setup
description: Connect OpenArt image and video generation models to AI tools (Claude, ChatGPT, Cursor) through the Model Context Protocol. Use when installing or authenticating the OpenArt CLI/MCP server, or connecting OpenArt models to an AI client.
---

# OpenArt MCP Setup Skill

Connect all OpenArt models (17+ image/video models) to Claude, ChatGPT, and Cursor via MCP.

## Quick Setup (Windows)

```powershell
# 1. Install OpenArt CLI
irm https://raw.githubusercontent.com/OpenArt-AI/cli/main/install.ps1 | iex

# 2. Add to PATH for current session
$env:PATH += ";C:\Users\USER\AppData\Local\Programs\openart\bin"

# 3. Login to OpenArt
openart login
```

## Configure MCP for All AI Tools

### Claude (`~/.config/claude/mcp.json`)
```json
{
  "mcpServers": {
    "openart": {
      "url": "https://mcp.openart.ai/mcp"
    }
  }
}
```

### Cursor (`~/.cursor/mcp.json`)
```json
{
  "mcpServers": {
    "openart": {
      "url": "https://mcp.openart.ai/mcp"
    }
  }
}
```

### ChatGPT (`~/AppData/Roaming/ChatGPT/mcp.json`)
```json
{
  "mcpServers": {
    "openart": {
      "url": "https://mcp.openart.ai/mcp"
    }
  }
}
```

## Available Models (17 Total)

### Image Models
| Model ID | Name | Capabilities |
|----------|------|--------------|
| `nano-banana-2` | Nano Banana 2 | text2image, image2image |
| `nano-banana-pro` | Nano Banana Pro | text2image, image2image |
| `nano-banana-2-lite` | Nano Banana 2 Lite | text2image, image2image |
| `gpt-image-2` | GPT Image 2 | text2image, image2image |
| `byte-plus-seedream-4-5` | Seedream 4.5 | text2image, image2image |
| `byte-plus-seedream-5-pro` | Seedream 5 Pro | text2image, image2image |
| `byte-plus-seedream-5-lite` | Seedream 5 Lite | text2image, image2image |
| `kling-3-omni` | Kling 3 Omni | text2image, image2image |

### Video Models
| Model ID | Name | Capabilities |
|----------|------|--------------|
| `grok-imagine-1-5` | Grok Imagine 1.5 | text2video, image2video |
| `gemini-omni-flash` | Gemini Omni Flash | text2video, image2video, element2video |
| `gemini-omni-1-1-flash` | Gemini Omni 1.1 Flash | text2video, image2video, element2video |
| `kling-3-omni` | Kling 3 Omni | text2video, image2video, element2video |
| `byte-plus-seedance-2` | Seedance 2.0 | text2video, image2video, element2video |
| `byte-plus-seedance-2-fast` | Seedance 2.0 Fast | text2video, image2video, element2video |
| `byte-plus-seedance-2-mini` | Seedance 2.0 Mini | text2video, image2video, element2video |
| `byte-plus-seedance-2-5` | Seedance 2.5 | text2video, image2video, element2video |
| `wan2-7` | Wan 2.7 | text2video, image2video, element2video |
| `pixverseV6` | PixVerse V6 | text2video, image2video |

### Hybrid (Image + Video)
| Model ID | Name | Capabilities |
|----------|------|--------------|
| `smart-shot` | Smart Shot | preview-shot-plan, generate-shot-video |

## Usage

### Via CLI
```powershell
$env:PATH += ";C:\Users\USER\AppData\Local\Programs\openart\bin"

# Generate image
openart generate image "a red fox in the snow" --model nano-banana-2 -o ./out/

# Generate video
openart generate video "cinematic fox running" --model seedance-2-5 -o ./out/

# List models
openart model list

# Check model params
openart model form <model-id>
```

### Via AI Agents (after restart)
Simply ask your agent:
- "Generate a moodboard of a desert-glass perfume bottle — 4 variations, studio light, 1:1"
- "Create a 5-second video of a fox running in snow using Seedance 2.5"
- "Use Smart Shot to plan and generate a product commercial"

## Notes
- Requires OpenArt credits for generations
- Restart AI tools after MCP config to load the server
- MCP endpoint: `https://mcp.openart.ai/mcp`
- All generations saved to your OpenArt library automatically
