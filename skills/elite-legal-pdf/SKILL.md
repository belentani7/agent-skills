---
name: elite-legal-pdf
description: >-
  Generador de documentos jurídicos PDF premium estilo firma de derechos humanos de élite (Olivia Pope /
  human rights law firm). Convierte textos, markdown y documentos legales en PDFs profesionales con
  portada dramática, tabla de contenidos interactiva con bookmarks, headers/footers institucionales,
  temas premium (navy-gold, classic-bw, crimson-legal, minimalist), watermarks (CONFIDENCIAL/DRAFT/
  PRIVILEGED/ATTORNEY-CLIENT), numeración de párrafos (§), campos de firma, y metadatos PDF completos.
  Soporta PT, ES, EN, FR, IT, DE. Usa reportlab (Python).
  TRIGGER cuando el usuario pide: "generar PDF legal", "documento jurídico PDF", "defensa en PDF",
  "legal brief PDF", "court filing", "human rights document", "premium legal PDF", "Olivia Pope PDF",
  "parecer jurídico PDF", "memorando legal", "petição PDF", "demanda PDF", o cualquier documento
  jurídico que necesite formato profesional de firma de abogados.
  NO usar para PDFs simples, facturas, o documentos no jurídicos.
platforms: [linux, macos, windows]
---

# Elite Legal PDF Generator

Genera documentos jurídicos PDF premium con diseño de firma de derechos humanos de élite.

## When to Use

- Usuario pide convertir textos/markdown en PDF jurídico profesional
- Usuario menciona "Olivia Pope", "law firm", "human rights document", "legal brief"
- Usuario necesita pareceres jurídicos, defensas, peticiones o memorandos en PDF
- Usuario pide PDF con portada, bookmarks, watermarks o formato legal premium
- Cualquier documento que necesite el aspecto de una firma de abogados de prestigio

## Prerequisites

```bash
pip install reportlab
```

Verify: `python -c "import reportlab; print(reportlab.Version)"` should print ≥ 4.0

## Usage

### Quick generation (most common)

```bash
python generate_legal_pdf.py --input ./folder/ --output defesa.pdf
```

### Full options

```bash
python generate_legal_pdf.py \
  --input ./docs/ \
  --output defense_brief.pdf \
  --theme navy-gold \
  --watermark CONFIDENCIAL \
  --lang pt \
  --title "Da Cidadã Europeia à Suspeita Perpétua" \
  --subtitle "Um Desafio ao Estado de Direito" \
  --author "OP & Associates" \
  --firm "Human Rights Division" \
  --numbered \
  --sign "Dr. Maria Silva, OAB/SP 123.456" \
  --date "2026-09-02" \
  --cover-desc "Defesa Integral contra Arbitrariedade Administrativa" \
  --confidential
```

### Single file input

```bash
python generate_legal_pdf.py --input ./document.md --output legal.pdf --theme crimson-legal
```

### Multiple files (consolidated brief)

```bash
python generate_legal_pdf.py --input ./part1.md ./part2.md ./jurisprudence.md --output brief.pdf
```

## Themes

| Theme           | Style                          | Best for                              |
|-----------------|--------------------------------|---------------------------------------|
| `navy-gold`     | Navy + gold accents (default)  | Human rights, international law       |
| `classic-bw`    | Black & white, serif           | Court filings, formal submissions     |
| `crimson-legal` | Deep red + charcoal            | Criminal defense, aggressive posture  |
| `minimalist`    | Clean grey, sans-serif         | Internal memos, working documents     |

## Watermarks

`CONFIDENCIAL` · `DRAFT` · `PRIVILEGED` · `WORK PRODUCT` · `ATTORNEY-CLIENT` · `CUSTOM:text`

## CLI Flags

| Flag              | Default       | Description                              |
|-------------------|---------------|------------------------------------------|
| `--input`         | (required)    | Input file(s) or directory               |
| `--output`        | (required)    | Output PDF path                           |
| `--theme`         | `navy-gold`   | Visual theme                             |
| `--watermark`     | none          | Watermark text                           |
| `--lang`          | auto-detect   | Language (pt/es/en/fr/it/de)             |
| `--title`         | from filename | Document title                           |
| `--subtitle`      | none          | Document subtitle                        |
| `--author`        | none          | Author/firm name                         |
| `--firm`          | none          | Firm division text                       |
| `--numbered`      | false         | Number paragraphs (§1, §2, …)            |
| `--sign`          | none          | Signature line text                      |
| `--date`          | today         | Document date                            |
| `--cover-desc`    | none          | Cover description line                   |
| `--confidential`  | false         | Add "CONFIDENCIAL" header                |
| `--no-cover`      | false         | Skip cover page                          |
| `--no-toc`        | false         | Skip table of contents                   |

## Output Features

- **Cover page** with gold rules, firm identity, confidential notice
- **Interactive TOC** with PDF bookmarks for navigation
- **Section dividers** between document parts
- **Professional tables** with navy headers and gold underlines
- **Headers/footers** with firm name, page numbers, confidentiality notice
- **Watermarks** as rotated semi-transparent text
- **Signature fields** for attorney authentication
- **Full PDF metadata** (title, author, subject, keywords, creator, dates)
- **Multi-language** header/footer text in PT/ES/EN/FR/IT/DE

## File Format Support

- **Markdown** (.md): Headers (#/##/###), bold, italic, tables, lists, links
- **Plain text** (.txt): Roman numeral detection, ALL-CAPS headers, quotes
- **Mixed**: Directory input auto-detects and orders files

## Related Skills

- `pdf` — general PDF operations (merge, split, extract)
- `markdown-documentation` — markdown formatting
- `design-taste` — visual design guidance
