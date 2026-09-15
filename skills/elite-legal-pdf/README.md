# Elite Legal PDF Generator

**Premium legal document generator — Human rights law firm style.**

Converts markdown, plain text, and legal documents into professionally designed PDFs with the look and feel of a top-tier human rights law firm.

## Features

- **4 premium themes**: Navy-Gold (international law), Classic B&W (court filings), Crimson-Legal (aggressive defense), Minimalist (internal memos)
- **Interactive PDF bookmarks** — click-to-navigate outline in any PDF reader
- **Watermarks** — CONFIDENCIAL, DRAFT, PRIVILEGED, ATTORNEY-CLIENT, or custom text
- **6 languages** — PT, ES, EN, FR, IT, DE with auto-detection
- **Paragraph numbering** (§1, §2, …) for formal legal submissions
- **Signature blocks** with attorney credentials and date
- **Professional tables** with theme-colored headers
- **Section dividers** for multi-part briefs
- **Cover page** with firm identity and confidential notice
- **Full PDF metadata** — title, author, subject, creator, creation date
- **Cross-platform** — Windows, macOS, Linux font detection

## Installation

```bash
pip install reportlab pypdf
```

## Quick Start

```bash
# Single document
python generate_legal_pdf.py --input defense.md --output brief.pdf

# Multi-part legal brief from folder
python generate_legal_pdf.py --input ./legal_docs/ --output full_brief.pdf

# With all options
python generate_legal_pdf.py \
  --input ./docs/ \
  --output defense.pdf \
  --theme navy-gold \
  --watermark CONFIDENCIAL \
  --lang pt \
  --title "Da Cidadã Europeia à Suspeita Perpétua" \
  --subtitle "Um Desafio ao Estado de Direito" \
  --author "OP & Associates" \
  --firm "Human Rights Division" \
  --numbered \
  --sign "Dr. Maria Silva, OAB/SP 123.456" \
  --confidential
```

## Themes

| Theme | Preview | Best For |
|-------|---------|----------|
| `navy-gold` | Navy header bar + gold accents on ivory | Human rights, international law, EU cases |
| `classic-bw` | Black serif on white, no color | Court filings, formal submissions |
| `crimson-legal` | Deep red + charcoal | Criminal defense, aggressive posture |
| `minimalist` | Clean grey, sans-serif | Internal memos, working documents |

## CLI Reference

```
--input, -i       Input file(s) or directory (required)
--output, -o      Output PDF path (required)
--theme, -t       navy-gold | classic-bw | crimson-legal | minimalist
--watermark, -w   CONFIDENCIAL | DRAFT | PRIVILEGED | WORK PRODUCT | ATTORNEY-CLIENT | CUSTOM:text
--lang, -l        auto | pt | es | en | fr | it | de
--title           Cover page title
--subtitle        Cover page subtitle
--author          Author/firm name (shown in header + cover)
--firm            Firm division text (shown in cover)
--numbered, -n    Add §-numbering to paragraphs
--sign            Signature line text
--date            Document date (default: today)
--cover-desc      Cover description line
--confidential    Show CONFIDENCIAL in header
--no-cover        Skip cover page
--no-toc          Skip table of contents
```

## File Format Support

| Format | Detection |
|--------|-----------|
| `.md` | Headers, bold/italic, tables, lists, links |
| `.txt` | Roman numeral sections, ALL-CAPS headers, quotes, arrows |
| Directory | Auto-discovers .md and .txt, creates section dividers |

## Language Auto-Detection

The generator analyzes the first 5000 characters of input to detect language by keyword frequency. Override with `--lang`.

## Architecture

```
elite-legal-pdf/
├── SKILL.md                  # Skill definition (for AI agent systems)
├── generate_legal_pdf.py     # Main generator (single-file, zero dependencies beyond reportlab)
├── README.md                 # This file
├── reference/                # Extended documentation
└── assets/                   # Templates and samples
```

## As a Skill for AI Agents

This tool is designed as a skill for Qwen Code, Claude Code, and similar AI agent systems. When the agent detects a request for legal PDF generation, it invokes `generate_legal_pdf.py` with appropriate flags.

Install as a local skill:
```bash
# Copy the elite-legal-pdf folder to your skills directory
cp -r elite-legal-pdf ~/.agents/skills/
```

## License

MIT

## Author

Pedro Belentani — [belentani7](https://github.com/belentani7)
