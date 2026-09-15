#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Elite Legal PDF Generator v1.0
Firma de derechos humanos de élite — estilo Olivia Pope / Human Rights Division

Features:
  - 4 themes (navy-gold, classic-bw, crimson-legal, minimalist)
  - Cover page dramática con firma institucional
  - Bookmarks PDF interactivos (outline)
  - Watermarks rotados semi-transparentes
  - Multi-idioma (PT/ES/EN/FR/IT/DE) para headers/footers
  - Numeración de párrafos (§1, §2, …)
  - Campos de firma con línea
  - Metadatos PDF completos
  - Soporte .md / .txt / directorio
  - Tables profesionales
  - Section dividers entre partes

Usage: python generate_legal_pdf.py --input ./docs/ --output brief.pdf --theme navy-gold
"""

import argparse
import os
import re
import sys
import math
from datetime import datetime
from pathlib import Path

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm, mm
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.colors import HexColor, white, black
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
    from reportlab.platypus import (
        Paragraph, Spacer, PageBreak, Table, TableStyle,
        HRFlowable, Frame, PageTemplate, BaseDocTemplate,
        NextPageTemplate, KeepTogether
    )
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas as canvasmod
except ImportError:
    print("ERROR: reportlab not installed. Run: pip install reportlab")
    sys.exit(1)


# ─────────────────────────────────────────────
# FONT REGISTRATION
# ─────────────────────────────────────────────

def register_fonts():
    """Register system fonts with cross-platform fallback."""
    font_paths = {
        'windows': "C:/Windows/Fonts",
        'linux': "/usr/share/fonts/truetype",
        'mac': "/Library/Fonts",
    }
    
    # Detect platform
    if os.path.exists("C:/Windows/Fonts"):
        fdir = font_paths['windows']
    elif os.path.exists("/usr/share/fonts"):
        fdir = font_paths['linux']
    elif os.path.exists("/Library/Fonts"):
        fdir = font_paths['mac']
    else:
        fdir = ""
    
    font_map = {
        'Arial': ('arial.ttf', 'arialbd.ttf', 'ariali.ttf', 'arialbi.ttf'),
        'Georgia': ('georgia.ttf', 'georgiab.ttf', 'georgiai.ttf', 'georgiabi.ttf'),
        'Times': ('times.ttf', 'timesbd.ttf', 'timesi.ttf', 'timesbi.ttf'),
        'Calibri': ('calibri.ttf', 'calibrib.ttf', 'calibrii.ttf', 'calibriz.ttf'),
    }
    
    registered = {}
    for family, files in font_map.items():
        try:
            normal = os.path.join(fdir, files[0])
            bold = os.path.join(fdir, files[1])
            italic = os.path.join(fdir, files[2])
            bi = os.path.join(fdir, files[3])
            if all(os.path.exists(f) for f in [normal, bold]):
                pdfmetrics.registerFont(TTFont(f'{family}', normal))
                pdfmetrics.registerFont(TTFont(f'{family}Bd', bold))
                if os.path.exists(italic):
                    pdfmetrics.registerFont(TTFont(f'{family}It', italic))
                if os.path.exists(bi):
                    pdfmetrics.registerFont(TTFont(f'{family}BI', bi))
                pdfmetrics.registerFontFamily(family,
                    normal=family, bold=f'{family}Bd',
                    italic=f'{family}It' if os.path.exists(italic) else family,
                    boldItalic=f'{family}BI' if os.path.exists(bi) else f'{family}Bd')
                registered[family] = True
        except Exception:
            pass
    
    return registered


# ─────────────────────────────────────────────
# THEMES
# ─────────────────────────────────────────────

THEMES = {
    'navy-gold': {
        'primary': '#0D1B2A',
        'secondary': '#1B2838',
        'accent': '#C6A55C',
        'accent_dark': '#9C7D3A',
        'accent_light': '#E8D5A3',
        'bg': '#FDF8F0',
        'bg_alt': '#F5F0E8',
        'text': '#1A1A1A',
        'text_med': '#3D3D3D',
        'text_light': '#6B7280',
        'border': '#D4C5A9',
        'serif': True,
        'header_bar': True,
    },
    'classic-bw': {
        'primary': '#000000',
        'secondary': '#1A1A1A',
        'accent': '#333333',
        'accent_dark': '#000000',
        'accent_light': '#666666',
        'bg': '#FFFFFF',
        'bg_alt': '#F5F5F5',
        'text': '#000000',
        'text_med': '#333333',
        'text_light': '#666666',
        'border': '#CCCCCC',
        'serif': True,
        'header_bar': False,
    },
    'crimson-legal': {
        'primary': '#1A0A0A',
        'secondary': '#3D1515',
        'accent': '#7B1818',
        'accent_dark': '#5B1A1A',
        'accent_light': '#B84040',
        'bg': '#FDF6F6',
        'bg_alt': '#F5EBEB',
        'text': '#1A1A1A',
        'text_med': '#3D3D3D',
        'text_light': '#6B7280',
        'border': '#D4B0B0',
        'serif': True,
        'header_bar': True,
    },
    'minimalist': {
        'primary': '#2D3748',
        'secondary': '#4A5568',
        'accent': '#718096',
        'accent_dark': '#4A5568',
        'accent_light': '#A0AEC0',
        'bg': '#FFFFFF',
        'bg_alt': '#F7FAFC',
        'text': '#1A202C',
        'text_med': '#4A5568',
        'text_light': '#718096',
        'border': '#E2E8F0',
        'serif': False,
        'header_bar': False,
    },
}


# ─────────────────────────────────────────────
# MULTI-LANGUAGE STRINGS
# ─────────────────────────────────────────────

I18N = {
    'pt': {
        'toc': 'ÍNDICE', 'page': 'Página', 'compiled': 'Compilado em',
        'confidential': 'CONFIDENCIAL', 'legal_doc': 'Documento Jurídico',
        'max_pressure': 'Máxima pressão jurídica, mínima vulnerabilidade factual',
        'legal_defense': 'Defesa Jurídica', 'working_doc': 'Documento de trabalho jurídico',
        'annex': 'ANEXO', 'references': 'Referências Documentais',
        'methodological_note': 'NOTA METODOLÓGICA FINAL',
        'signature': 'Assinatura', 'date': 'Data',
    },
    'es': {
        'toc': 'ÍNDICE', 'page': 'Página', 'compiled': 'Compilado el',
        'confidential': 'CONFIDENCIAL', 'legal_doc': 'Documento Jurídico',
        'max_pressure': 'Máxima presión jurídica, mínima vulnerabilidad factual',
        'legal_defense': 'Defensa Jurídica', 'working_doc': 'Documento de trabajo jurídico',
        'annex': 'ANEXO', 'references': 'Referencias Documentales',
        'methodological_note': 'NOTA METODOLÓGICA FINAL',
        'signature': 'Firma', 'date': 'Fecha',
    },
    'en': {
        'toc': 'TABLE OF CONTENTS', 'page': 'Page', 'compiled': 'Compiled on',
        'confidential': 'CONFIDENTIAL', 'legal_doc': 'Legal Document',
        'max_pressure': 'Maximum legal pressure, minimum factual vulnerability',
        'legal_defense': 'Legal Defense', 'working_doc': 'Working legal document',
        'annex': 'ANNEX', 'references': 'Documentary References',
        'methodological_note': 'FINAL METHODOLOGICAL NOTE',
        'signature': 'Signature', 'date': 'Date',
    },
    'fr': {
        'toc': 'TABLE DES MATIÈRES', 'page': 'Page', 'compiled': 'Compilé le',
        'confidential': 'CONFIDENTIEL', 'legal_doc': 'Document Juridique',
        'max_pressure': 'Maximum de pression juridique, minimum de vulnérabilité factuelle',
        'legal_defense': 'Défense Juridique', 'working_doc': 'Document de travail juridique',
        'annex': 'ANNEXE', 'references': 'Références Documentaires',
        'methodological_note': 'NOTE MÉTHODOLOGIQUE FINALE',
        'signature': 'Signature', 'date': 'Date',
    },
    'it': {
        'toc': 'INDICE', 'page': 'Pagina', 'compiled': 'Compilato il',
        'confidential': 'RISERVATO', 'legal_doc': 'Documento Giuridico',
        'max_pressure': 'Massima pressione giuridica, minima vulnerabilità fattuale',
        'legal_defense': 'Difesa Legale', 'working_doc': 'Documento di lavoro giuridico',
        'annex': 'ALLEGATO', 'references': 'Riferimenti Documentali',
        'methodological_note': 'NOTA METODOLOGICA FINALE',
        'signature': 'Firma', 'date': 'Data',
    },
    'de': {
        'toc': 'INHALTSVERZEICHNIS', 'page': 'Seite', 'compiled': 'Erstellt am',
        'confidential': 'VERTRAULICH', 'legal_doc': 'Juristisches Dokument',
        'max_pressure': 'Maximaler juristischer Druck, minimale faktische Verwundbarkeit',
        'legal_defense': 'Juristische Verteidigung', 'working_doc': 'Juristisches Arbeitsdokument',
        'annex': 'ANHANG', 'references': 'Dokumentarische Referenzen',
        'methodological_note': 'FINALE METHODISCHE ANMERKUNG',
        'signature': 'Unterschrift', 'date': 'Datum',
    },
}


def detect_language(text):
    """Auto-detect language from text content using keyword frequency."""
    lang_keywords = {
        'pt': ['cidadã', 'direito', 'jurídico', 'defesa', 'constituição', 'português',
                'não', 'é', 'da', 'de', 'uma', 'são', 'pela', 'pelo', 'estado', 'lei'],
        'es': ['ciudadana', 'derecho', 'jurídico', 'defensa', 'constitución', 'español',
                'derechos', 'fundamentales', 'estado', 'ley', 'tribunal'],
        'en': ['citizen', 'rights', 'legal', 'defense', 'constitution', 'english',
                'court', 'law', 'fundamental', 'state', 'judicial', 'human'],
        'fr': ['citoyen', 'droit', 'juridique', 'défense', 'constitution', 'français',
                'tribunal', 'loi', 'fondamental', 'état'],
        'it': ['cittadina', 'diritto', 'giuridico', 'difesa', 'costituzione', 'italiano',
                'tribunale', 'legge', 'fondamentale', 'stato'],
        'de': ['bürger', 'recht', 'juristisch', 'verteidigung', 'verfassung', 'deutsch',
                'gericht', 'gesetz', 'grundlegend', 'staat'],
    }
    text_lower = text.lower()
    scores = {}
    for lang, keywords in lang_keywords.items():
        scores[lang] = sum(1 for kw in keywords if kw in text_lower)
    best = max(scores, key=scores.get)
    return best if scores[best] > 3 else 'en'


# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────

def esc(text):
    """Escape XML special chars for reportlab Paragraph."""
    text = str(text)
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    return text


def fmt(text):
    """Process inline markdown formatting."""
    text = esc(text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    text = re.sub(r'\[\[\d+\]\(.+?\)\]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text


def hex_color(h):
    return HexColor(h)


def gold_rule(color, w="50%", thick=1.5, sb=0, sa=12):
    return HRFlowable(width=w, thickness=thick, color=hex_color(color), spaceBefore=sb, spaceAfter=sa)


def thin_rule(color, w="100%", sb=8, sa=8):
    return HRFlowable(width=w, thickness=0.4, color=hex_color(color), spaceBefore=sb, spaceAfter=sa)


# ─────────────────────────────────────────────
# TABLE PARSING
# ─────────────────────────────────────────────

def parse_table_lines(lines):
    """Parse markdown table lines into rows."""
    rows = []
    for line in lines:
        line = line.strip()
        if line.startswith('|') and line.endswith('|'):
            if all(ch in '|:- ' for ch in line):
                continue
            cells = [c.strip() for c in line.split('|')[1:-1]]
            if cells and not all(c.replace('-','').replace(':','').replace(' ','') == '' for c in cells):
                rows.append(cells)
    return rows


def make_table(rows, styles, story, theme):
    """Build a styled table from parsed rows."""
    if not rows or len(rows) < 1:
        return
    ncols = max(len(r) for r in rows)
    for r in rows:
        while len(r) < ncols:
            r.append('')
    
    # Distribute width — first column gets less for bold labels
    avail_w = A4[0] - 4.8*cm
    if ncols == 1:
        col_widths = [avail_w]
    elif ncols == 2:
        col_widths = [avail_w * 0.35, avail_w * 0.65]
    elif ncols == 3:
        col_widths = [avail_w * 0.25, avail_w * 0.40, avail_w * 0.35]
    else:
        col_widths = [avail_w / ncols] * ncols
    
    data = []
    for i, row in enumerate(rows):
        sr = []
        for cell in row:
            ct = fmt(cell)
            if i == 0:
                sr.append(Paragraph(ct, styles['th']))
            else:
                sr.append(Paragraph(ct, styles['td']))
        data.append(sr)
    
    if not data:
        return
    
    t = Table(data, colWidths=col_widths)
    ts = [
        ('BACKGROUND', (0,0), (-1,0), hex_color(theme['primary'])),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('TOPPADDING', (0,0), (-1,0), 8),
        ('BOTTOMPADDING', (0,0), (-1,0), 8),
        ('TOPPADDING', (0,1), (-1,-1), 6),
        ('BOTTOMPADDING', (0,1), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0.4, hex_color(theme['border'])),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('LINEBELOW', (0,0), (-1,0), 1.5, hex_color(theme['accent'])),
    ]
    for i in range(1, len(data)):
        bg = theme['bg_alt'] if i % 2 == 0 else theme['bg']
        ts.append(('BACKGROUND', (0,i), (-1,i), hex_color(bg)))
    
    t.setStyle(TableStyle(ts))
    story.append(Spacer(1, 0.4*cm))
    story.append(t)
    story.append(Spacer(1, 0.4*cm))


# ─────────────────────────────────────────────
# CONTENT PARSERS
# ─────────────────────────────────────────────

def process_txt(filepath, story, styles, theme, bookmarks, numbered, para_count):
    """Process plain text files (.txt)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        story.append(Paragraph(f"Erro: {e}", styles['body']))
        return para_count
    
    tbuf = []
    in_table = False
    
    for line in lines:
        s = line.strip()
        
        # Table detection
        if s.startswith('|') and s.endswith('|'):
            tbuf.append(s)
            in_table = True
            continue
        elif in_table:
            if tbuf:
                rows = parse_table_lines(tbuf)
                if rows:
                    make_table(rows, styles, story, theme)
                tbuf = []
            in_table = False
        
        if not s:
            story.append(Spacer(1, 0.15*cm))
            continue
        
        if s in ('---', '***', '___'):
            story.append(thin_rule(theme['border']))
            continue
        
        # Roman numeral sections (I., II., III.…)
        rm = re.match(r'^([IVXLCDM]+)\.\s+(.+)$', s)
        if rm:
            title = f'{rm.group(1)}. {esc(rm.group(2))}'
            story.append(Paragraph(title, styles['h1']))
            bookmarks.append((rm.group(2)[:60], 1))
            continue
        
        # ALL CAPS section headers
        if s.isupper() and 5 < len(s) < 120 and not s.startswith(('ARTIGO', 'PEDIDO')):
            story.append(Paragraph(esc(s), styles['h2']))
            continue
        
        # Known section starters
        if re.match(r'^(BLOCO|PEDIDO|NOTA|TESE|CONCLUSÃO|FORMULAÇÃO)', s):
            story.append(Paragraph(f'<b>{esc(s)}</b>', styles['h3']))
            continue
        
        # Arrows and special bullets
        if s.startswith('→'):
            story.append(Paragraph(f'→ {esc(s[1:].strip())}', styles['bullet']))
            if numbered:
                para_count[0] += 1
            continue
        if s.startswith('❌'):
            story.append(Paragraph(
                f'<font color="{theme["accent"]}">✗</font> {esc(s[2:].strip())}',
                styles['bullet']))
            continue
        if s.startswith('- ') or s.startswith('• '):
            story.append(Paragraph(f'• {fmt(s[2:])}', styles['bullet']))
            if numbered:
                para_count[0] += 1
            continue
        
        # Quoted lines
        if s.startswith('"') and s.endswith('"'):
            story.append(Paragraph(f'<i>{esc(s)}</i>', styles['quote']))
            continue
        
        # Numbered items
        nm = re.match(r'^(\d+)\.\s+(.+)$', s)
        if nm:
            story.append(Paragraph(f'<b>{nm.group(1)}.</b> {fmt(nm.group(2))}', styles['bullet']))
            continue
        
        # Regular paragraph
        text = fmt(s)
        if numbered:
            para_count[0] += 1
            text = f'<font color="{theme["accent_light"]}" size="8">§{para_count[0]}</font> {text}'
        story.append(Paragraph(text, styles['body']))
    
    # Flush remaining table
    if tbuf:
        rows = parse_table_lines(tbuf)
        if rows:
            make_table(rows, styles, story, theme)
    
    return para_count


def process_md(filepath, story, styles, theme, bookmarks, numbered, para_count):
    """Process markdown files (.md)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        story.append(Paragraph(f"Erro: {e}", styles['body']))
        return para_count
    
    tbuf = []
    in_table = False
    
    for line in lines:
        s = line.strip()
        
        # Table detection
        if s.startswith('|') and s.endswith('|'):
            tbuf.append(s)
            in_table = True
            continue
        elif in_table:
            if tbuf:
                rows = parse_table_lines(tbuf)
                if rows:
                    make_table(rows, styles, story, theme)
                tbuf = []
            in_table = False
        
        if not s:
            story.append(Spacer(1, 0.12*cm))
            continue
        
        if s in ('---', '***', '___'):
            story.append(thin_rule(theme['border']))
            continue
        
        # Markdown headers
        if s.startswith('#### '):
            story.append(Paragraph(fmt(s[5:]), styles['h4']))
            continue
        if s.startswith('### '):
            title_text = s[4:]
            story.append(Paragraph(fmt(title_text), styles['h3']))
            bookmarks.append((title_text[:60], 3))
            continue
        if s.startswith('## '):
            title_text = s[3:]
            story.append(Paragraph(fmt(title_text), styles['h2']))
            bookmarks.append((title_text[:60], 2))
            continue
        if s.startswith('# ') and not s.startswith('## '):
            title_text = s[2:]
            story.append(Paragraph(fmt(title_text), styles['h1']))
            bookmarks.append((title_text[:60], 1))
            continue
        
        # Bold standalone line
        bm = re.match(r'^\*\*(.+?)\*\*$', s)
        if bm:
            story.append(Paragraph(f'<b>{fmt(bm.group(1))}</b>', styles['body']))
            continue
        
        # Bullets
        if s.startswith('- ') or s.startswith('* '):
            story.append(Paragraph(f'• {fmt(s[2:])}', styles['bullet']))
            if numbered:
                para_count[0] += 1
            continue
        if s.startswith('  - ') or s.startswith('  * '):
            story.append(Paragraph(f'– {fmt(s[4:])}', styles['subbullet']))
            continue
        
        # Numbered
        nm = re.match(r'^(\d+)\.\s+(.+)$', s)
        if nm:
            story.append(Paragraph(f'<b>{nm.group(1)}.</b> {fmt(nm.group(2))}', styles['bullet']))
            continue
        
        # Regular paragraph
        text = fmt(s)
        if numbered:
            para_count[0] += 1
            text = f'<font color="{theme["accent_light"]}" size="8">§{para_count[0]}</font> {text}'
        story.append(Paragraph(text, styles['body']))
    
    if tbuf:
        rows = parse_table_lines(tbuf)
        if rows:
            make_table(rows, styles, story, theme)
    
    return para_count


# ─────────────────────────────────────────────
# STYLE FACTORY
# ─────────────────────────────────────────────

def build_styles(theme, serif_name, serif_bd, serif_it, sans, sans_bd, sans_it, sans_bi):
    """Create all paragraph styles from theme colors and font names."""
    t = theme
    sf = serif_name if t['serif'] else sans
    sf_bd = serif_bd if t['serif'] else sans_bd
    sf_it = serif_it if t['serif'] else sans_it
    
    return {
        # Cover
        'cover_pre': ParagraphStyle('cpre', fontName=sans, fontSize=10, leading=14,
            alignment=TA_CENTER, textColor=hex_color(t['accent']), spaceAfter=6),
        'cover_title': ParagraphStyle('ct', fontName=sf_bd, fontSize=30, leading=38,
            alignment=TA_CENTER, textColor=hex_color(t['primary']), spaceAfter=8),
        'cover_sub': ParagraphStyle('cs', fontName=sf_it, fontSize=13, leading=19,
            alignment=TA_CENTER, textColor=hex_color(t['secondary']), spaceAfter=10),
        'cover_desc': ParagraphStyle('cd', fontName=sans, fontSize=9.5, leading=14,
            alignment=TA_CENTER, textColor=hex_color(t['text_med']), spaceAfter=4),
        'cover_conf': ParagraphStyle('cc', fontName=sans_it, fontSize=8.5, leading=12,
            alignment=TA_CENTER, textColor=hex_color(t['text_light'])),
        'cover_firm': ParagraphStyle('cf', fontName=sans_bd, fontSize=12, leading=16,
            alignment=TA_CENTER, textColor=hex_color(t['primary']), spaceAfter=4),
        'cover_firm_div': ParagraphStyle('cfd', fontName=sans, fontSize=8, leading=12,
            alignment=TA_CENTER, textColor=hex_color(t['accent_dark']), spaceAfter=20),
        
        # TOC
        'toc_title': ParagraphStyle('toct', fontName=sf_bd, fontSize=22, leading=28,
            alignment=TA_CENTER, textColor=hex_color(t['primary']), spaceAfter=20),
        'toc_part': ParagraphStyle('tocp', fontName=sans_bd, fontSize=11, leading=16,
            textColor=hex_color(t['accent']), spaceBefore=16, spaceAfter=6),
        'toc_sub': ParagraphStyle('tocs', fontName=sans, fontSize=10, leading=15,
            textColor=hex_color(t['text_med']), leftIndent=12, spaceBefore=1, spaceAfter=1),
        
        # Content headers
        'h1': ParagraphStyle('h1', fontName=sf_bd, fontSize=19, leading=25,
            textColor=hex_color(t['primary']), spaceBefore=28, spaceAfter=12),
        'h2': ParagraphStyle('h2', fontName=sans_bd, fontSize=14, leading=19,
            textColor=hex_color(t['secondary']), spaceBefore=20, spaceAfter=8),
        'h3': ParagraphStyle('h3', fontName=sans_bd, fontSize=11.5, leading=16,
            textColor=hex_color(t['secondary']), spaceBefore=14, spaceAfter=6),
        'h4': ParagraphStyle('h4', fontName=sans_bi if sans_bi != sans else sans_bd,
            fontSize=10.5, leading=15, textColor=hex_color(t['text_med']),
            spaceBefore=10, spaceAfter=5),
        
        # Body
        'body': ParagraphStyle('bd', fontName=sf, fontSize=10.5, leading=16,
            textColor=hex_color(t['text']), alignment=TA_JUSTIFY,
            spaceBefore=3, spaceAfter=6),
        'body_indent': ParagraphStyle('bdi', fontName=sf, fontSize=10.5, leading=16,
            textColor=hex_color(t['text']), alignment=TA_JUSTIFY,
            spaceBefore=3, spaceAfter=6, leftIndent=1.2*cm),
        'quote': ParagraphStyle('qt', fontName=sf_it, fontSize=10.5, leading=16,
            textColor=hex_color(t['text_med']), alignment=TA_JUSTIFY,
            spaceBefore=10, spaceAfter=10, leftIndent=1.5*cm, rightIndent=1*cm),
        'bullet': ParagraphStyle('bl', fontName=sf, fontSize=10.5, leading=15,
            textColor=hex_color(t['text']), alignment=TA_LEFT,
            spaceBefore=2, spaceAfter=3, leftIndent=1.8*cm, firstLineIndent=-0.5*cm),
        'subbullet': ParagraphStyle('sbl', fontName=sf, fontSize=10, leading=14,
            textColor=hex_color(t['text_med']), alignment=TA_LEFT,
            spaceBefore=1, spaceAfter=2, leftIndent=2.8*cm, firstLineIndent=-0.5*cm),
        
        # Table
        'th': ParagraphStyle('th', fontName=sans_bd, fontSize=9, leading=12.5,
            textColor=white, alignment=TA_LEFT, spaceBefore=2, spaceAfter=2),
        'td': ParagraphStyle('td', fontName=sf, fontSize=9, leading=13,
            textColor=hex_color(t['text']), alignment=TA_LEFT,
            spaceBefore=2, spaceAfter=2),
        
        # Divider
        'div_title': ParagraphStyle('dvt', fontName=sf_bd, fontSize=26, leading=34,
            alignment=TA_CENTER, textColor=hex_color(t['primary']), spaceAfter=12),
        'div_sub': ParagraphStyle('dvs', fontName=sf_it, fontSize=13, leading=18,
            alignment=TA_CENTER, textColor=hex_color(t['text_med'])),
    }


# ─────────────────────────────────────────────
# WATERMARK RENDERER
# ─────────────────────────────────────────────

def make_watermark_func(watermark_text, theme_color):
    """Return a function that draws a diagonal watermark on each page."""
    def draw_watermark(c, doc):
        c.saveState()
        c.setFont('Arial', 52)
        c.setFillColor(HexColor(theme_color))
        c.setFillAlpha(0.07)
        c.translate(A4[0]/2, A4[1]/2)
        c.rotate(45)
        c.drawCentredString(0, 0, watermark_text)
        c.restoreState()
    return draw_watermark


# ─────────────────────────────────────────────
# HEADER / FOOTER
# ─────────────────────────────────────────────

def make_header_footer(theme, i18n, author_text, firm_text, confidential_flag, watermark_fn):
    """Return a page drawing function for content pages."""
    def draw_hf(c, doc):
        c.saveState()
        
        if watermark_fn:
            watermark_fn(c, doc)
        
        # Header
        if theme['header_bar']:
            c.setFillColor(hex_color(theme['primary']))
            c.rect(0, A4[1] - 1.4*cm, A4[0], 1.4*cm, fill=1, stroke=0)
            c.setFont('Arial', 6.5)
            c.setFillColor(hex_color(theme['accent']))
            left = f"{i18n['legal_defense']}  ·  {confidential_flag or author_text}"
            c.drawString(2.4*cm, A4[1] - 1.05*cm, left)
            right = f"{firm_text or i18n['confidential']}"
            c.drawRightString(A4[0] - 2.4*cm, A4[1] - 1.05*cm, right)
            
            c.setStrokeColor(hex_color(theme['accent']))
            c.setLineWidth(0.8)
            c.line(2.4*cm, A4[1] - 1.45*cm, A4[0] - 2.4*cm, A4[1] - 1.45*cm)
        else:
            c.setStrokeColor(hex_color(theme['accent']))
            c.setLineWidth(0.5)
            c.line(2.4*cm, A4[1] - 1.8*cm, A4[0] - 2.4*cm, A4[1] - 1.8*cm)
            c.setFont('Arial', 7)
            c.setFillColor(hex_color(theme['text_light']))
            c.drawString(2.4*cm, A4[1] - 1.6*cm, f"{i18n['legal_defense']}")
            if confidential_flag:
                c.drawRightString(A4[0] - 2.4*cm, A4[1] - 1.6*cm, i18n['confidential'])
        
        # Footer
        c.setStrokeColor(hex_color(theme['border']))
        c.setLineWidth(0.4)
        c.line(2.4*cm, 1.6*cm, A4[0] - 2.4*cm, 1.6*cm)
        
        c.setFont('Arial', 7)
        c.setFillColor(hex_color(theme['text_light']))
        c.drawCentredString(A4[0]/2, 1.0*cm, f"— {doc.page} —")
        c.setFont('Arial', 5.5)
        c.drawString(2.4*cm, 0.6*cm,
            f"{i18n['compiled']}: {datetime.now().strftime('%d/%m/%Y')}")
        c.drawRightString(A4[0] - 2.4*cm, 0.6*cm, i18n['max_pressure'])
        
        c.restoreState()
    
    return draw_hf


# ─────────────────────────────────────────────
# COVER PAGE DRAWER
# ─────────────────────────────────────────────

def make_cover_drawer(theme, watermark_fn):
    def draw_cover(c, doc):
        c.saveState()
        if watermark_fn:
            watermark_fn(c, doc)
        c.restoreState()
    return draw_cover


# ─────────────────────────────────────────────
# SECTION DIVIDER
# ─────────────────────────────────────────────

def add_section_divider(story, styles, theme, title, subtitle=""):
    story.append(Spacer(1, 7*cm))
    story.append(gold_rule(theme['accent'], "40%", 2, 0, 20))
    # Support <br/> in title
    story.append(Paragraph(title, styles['div_title']))
    if subtitle:
        story.append(Paragraph(subtitle, styles['div_sub']))
    story.append(gold_rule(theme['accent'], "40%", 2, 20, 0))
    story.append(PageBreak())


# ─────────────────────────────────────────────
# SIGNATURE BLOCK
# ─────────────────────────────────────────────

def add_signature_block(story, styles, theme, sign_text, date_text, i18n):
    story.append(Spacer(1, 2*cm))
    story.append(thin_rule(theme['accent'], "30%", 0, 8))
    story.append(Paragraph(esc(sign_text), ParagraphStyle(
        'sig', fontName='Arial', fontSize=10, leading=14,
        alignment=TA_CENTER, textColor=hex_color(theme['text']),
        spaceBefore=12, spaceAfter=4)))
    story.append(Paragraph(f'{i18n["date"]}: {date_text}', ParagraphStyle(
        'sigdate', fontName='ArialIt' if 'ArialIt' in pdfmetrics.getRegisteredFontNames() else 'Arial',
        fontSize=9, leading=13, alignment=TA_CENTER,
        textColor=hex_color(theme['text_light']))))


# ─────────────────────────────────────────────
# PDF BOOKMARKS (OUTLINE)
# ─────────────────────────────────────────────

def add_bookmarks_to_pdf(pdf_path, bookmark_list):
    """Add PDF outline bookmarks using pypdf if available."""
    try:
        from pypdf import PdfReader, PdfWriter
    except ImportError:
        return  # pypdf not available, skip bookmarks
    
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    
    for page in reader.pages:
        writer.add_page(page)
    
    # Copy metadata
    if reader.metadata:
        writer.add_metadata({
            '/Title': reader.metadata.get('/title', ''),
            '/Author': reader.metadata.get('/author', ''),
            '/Subject': reader.metadata.get('/subject', ''),
        })
    
    # Add bookmarks (outline)
    parent_bookmarks = {}
    for title, level in bookmark_list:
        if level == 1:
            bm = writer.add_outline_item(title, 0)
            parent_bookmarks[1] = bm
        elif level == 2 and 1 in parent_bookmarks:
            bm = writer.add_outline_item(title, 0, parent=parent_bookmarks[1])
            parent_bookmarks[2] = bm
        elif level == 3 and 2 in parent_bookmarks:
            writer.add_outline_item(title, 0, parent=parent_bookmarks[2])
        else:
            writer.add_outline_item(title, 0)
    
    with open(pdf_path, 'wb') as f:
        writer.write(f)


# ─────────────────────────────────────────────
# MAIN BUILD FUNCTION
# ─────────────────────────────────────────────

def build_pdf(args):
    """Main entry point — build the premium legal PDF."""
    
    # Resolve theme
    theme = THEMES.get(args.theme, THEMES['navy-gold'])
    
    # Resolve language
    lang = args.lang
    if not lang or lang == 'auto':
        # Auto-detect from first input file
        for inp in args.input:
            if os.path.isfile(inp):
                try:
                    with open(inp, 'r', encoding='utf-8') as f:
                        sample = f.read(5000)
                    lang = detect_language(sample)
                    break
                except:
                    pass
        if not lang or lang == 'auto':
            lang = 'en'
    
    i18n = I18N.get(lang, I18N['en'])
    
    # Register fonts
    reg = register_fonts()
    has_g = 'Georgia' in reg
    has_t = 'Times' in reg
    
    serif_name = 'Georgia' if has_g else ('Times' if has_t else 'Arial')
    serif_bd = f'{serif_name}Bd'
    serif_it = f'{serif_name}It' if f'{serif_name}It' in pdfmetrics.getRegisteredFontNames() else serif_name
    
    sans = 'Arial'
    sans_bd = 'ArialBd'
    sans_it = 'ArialIt' if 'ArialIt' in pdfmetrics.getRegisteredFontNames() else 'Arial'
    sans_bi = 'ArialBI' if 'ArialBI' in pdfmetrics.getRegisteredFontNames() else 'ArialBd'
    
    # Build styles
    styles = build_styles(theme, serif_name, serif_bd, serif_it, sans, sans_bd, sans_it, sans_bi)
    
    # Resolve inputs
    input_files = []
    for inp in args.input:
        if os.path.isdir(inp):
            for ext in ['*.md', '*.txt']:
                import glob as globmod
                input_files.extend(sorted(globmod.glob(os.path.join(inp, ext))))
        elif os.path.isfile(inp):
            input_files.append(inp)
    
    if not input_files:
        print(f"ERROR: No input files found in: {args.input}")
        sys.exit(1)
    
    # Create document
    doc = BaseDocTemplate(
        args.output, pagesize=A4,
        leftMargin=2.4*cm, rightMargin=2.4*cm,
        topMargin=2.8*cm, bottomMargin=2.4*cm,
        title=args.title or "Legal Document",
        author=args.author or "",
        subject=args.subtitle or "",
        creator="Elite Legal PDF Generator v1.0",
    )
    
    frame = Frame(2.4*cm, 2.4*cm, A4[0]-4.8*cm, A4[1]-5.2*cm, id='main')
    
    # Watermark function
    wm_fn = None
    if args.watermark:
        wm_text = args.watermark
        if wm_text.startswith('CUSTOM:'):
            wm_text = wm_text[7:]
        wm_fn = make_watermark_func(wm_text, theme['accent'])
    
    # Header/footer function
    hf_fn = make_header_footer(
        theme, i18n,
        args.author or "", args.firm or "",
        args.confidential, wm_fn
    )
    
    # Cover drawer
    cover_fn = make_cover_drawer(theme, wm_fn)
    
    doc.addPageTemplates([
        PageTemplate(id='cover', frames=[frame], onPage=cover_fn),
        PageTemplate(id='content', frames=[frame], onPage=hf_fn),
    ])
    
    story = []
    bookmarks = []  # (title, level)
    para_count = [0]  # mutable counter
    
    # ── COVER PAGE ──
    if not args.no_cover:
        story.append(Spacer(1, 5.5*cm))
        story.append(gold_rule(theme['accent'], "35%", 3, 0, 24))
        story.append(Paragraph(i18n['confidential'] if args.confidential else i18n['legal_doc'],
            styles['cover_pre']))
        story.append(Spacer(1, 0.8*cm))
        
        title_text = args.title or Path(input_files[0]).stem.replace('_', ' ').title()
        story.append(Paragraph(esc(title_text), styles['cover_title']))
        story.append(Spacer(1, 0.5*cm))
        
        if args.subtitle:
            story.append(Paragraph(esc(args.subtitle), styles['cover_sub']))
            story.append(Spacer(1, 0.5*cm))
        
        story.append(gold_rule(theme['accent'], "35%", 3, 24, 30))
        
        if args.cover_desc:
            story.append(Paragraph(esc(args.cover_desc), styles['cover_desc']))
            story.append(Spacer(1, 1.5*cm))
        
        if args.author or args.firm:
            story.append(Paragraph(f'<font size="12"><b>{esc(args.author or "")}</b></font>',
                styles['cover_firm']))
            if args.firm:
                story.append(Paragraph(
                    f'<font size="8" color="{theme["accent_dark"]}">{esc(args.firm)}</font>',
                    styles['cover_firm_div']))
            story.append(Spacer(1, 1*cm))
        
        date_str = args.date or datetime.now().strftime('%d de %B de %Y')
        story.append(Paragraph(
            f'{i18n["legal_doc"]}  ·  {date_str}', styles['cover_desc']))
        story.append(Spacer(1, 0.5*cm))
        story.append(Paragraph(
            f'<i>{i18n["working_doc"]}</i>', styles['cover_conf']))
        
        story.append(NextPageTemplate('content'))
        story.append(PageBreak())
    
    # ── PROCESS INPUT FILES ──
    part_num = 0
    for filepath in input_files:
        part_num += 1
        fname = Path(filepath).stem
        
        # Section divider for multi-file docs
        if len(input_files) > 1 and not args.no_cover:
            part_label = f'PARTE {part_num}' if lang in ('pt', 'es') else f'PART {part_num}'
            add_section_divider(story, styles, theme,
                part_label, fname.replace('_', ' ').title())
            bookmarks.append((part_label, 1))
        
        # Process based on extension
        ext = Path(filepath).suffix.lower()
        if ext == '.md':
            process_md(filepath, story, styles, theme, bookmarks, args.numbered, para_count)
        elif ext in ('.txt', '.text'):
            process_txt(filepath, story, styles, theme, bookmarks, args.numbered, para_count)
        else:
            # Try as plain text
            process_txt(filepath, story, styles, theme, bookmarks, args.numbered, para_count)
        
        if part_num < len(input_files):
            story.append(PageBreak())
    
    # ── SIGNATURE BLOCK ──
    if args.sign:
        date_str = args.date or datetime.now().strftime('%d/%m/%Y')
        add_signature_block(story, styles, theme, args.sign, date_str, i18n)
    
    # ── METHODOLOGICAL NOTE ──
    story.append(Spacer(1, 1.5*cm))
    story.append(gold_rule(theme['accent'], "100%", 1, 0, 16))
    story.append(Paragraph(i18n['methodological_note'], styles['h3']))
    story.append(Paragraph(
        f'<i><font color="{theme["accent"]}" size="12">{i18n["max_pressure"]}</font></i>',
        ParagraphStyle('motto', fontName=serif_it, fontSize=12, leading=18,
            alignment=TA_CENTER, spaceBefore=8, spaceAfter=16)))
    
    # BUILD
    doc.build(story)
    
    # Add bookmarks post-build
    if bookmarks:
        add_bookmarks_to_pdf(args.output, bookmarks)
    
    sz = os.path.getsize(args.output)
    print(f"✓ PDF generated: {args.output}")
    print(f"  Size: {sz/1024:.1f} KB")
    print(f"  Theme: {args.theme}")
    print(f"  Language: {lang}")
    print(f"  Files processed: {len(input_files)}")
    if args.watermark:
        print(f"  Watermark: {args.watermark}")
    if args.numbered:
        print(f"  Paragraphs numbered: {para_count[0]}")


# ─────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='Elite Legal PDF Generator — Premium legal documents',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --input ./docs/ --output brief.pdf
  %(prog)s --input defense.md --output legal.pdf --theme crimson-legal --watermark DRAFT
  %(prog)s --input ./parts/ --output full.pdf --numbered --sign "Dr. Silva, OAB 123"
        """)
    
    parser.add_argument('--input', '-i', nargs='+', required=True,
        help='Input file(s) or directory containing .md/.txt files')
    parser.add_argument('--output', '-o', required=True,
        help='Output PDF file path')
    parser.add_argument('--theme', '-t', default='navy-gold',
        choices=list(THEMES.keys()), help='Visual theme (default: navy-gold)')
    parser.add_argument('--watermark', '-w', default=None,
        help='Watermark: CONFIDENCIAL, DRAFT, PRIVILEGED, WORK PRODUCT, ATTORNEY-CLIENT, or CUSTOM:text')
    parser.add_argument('--lang', '-l', default='auto',
        choices=['auto', 'pt', 'es', 'en', 'fr', 'it', 'de'],
        help='Document language (default: auto-detect)')
    parser.add_argument('--title', default=None,
        help='Document title for cover page')
    parser.add_argument('--subtitle', default=None,
        help='Document subtitle')
    parser.add_argument('--author', default=None,
        help='Author/firm name')
    parser.add_argument('--firm', default=None,
        help='Firm division text')
    parser.add_argument('--numbered', '-n', action='store_true',
        help='Number paragraphs (§1, §2, …)')
    parser.add_argument('--sign', default=None,
        help='Signature line text (e.g., "Dr. Maria Silva, OAB/SP 123.456")')
    parser.add_argument('--date', default=None,
        help='Document date (default: today)')
    parser.add_argument('--cover-desc', default=None,
        help='Cover page description line')
    parser.add_argument('--confidential', action='store_true',
        help='Add CONFIDENCIAL header')
    parser.add_argument('--no-cover', action='store_true',
        help='Skip cover page')
    parser.add_argument('--no-toc', action='store_true',
        help='Skip table of contents')
    
    args = parser.parse_args()
    build_pdf(args)


if __name__ == '__main__':
    main()
