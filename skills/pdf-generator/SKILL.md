---
name: pdf-generator
description: Generación de PDFs profesionales con apariencia premium. Crea informes, reportes, documentos formales con diseños elegantes, tablas estilizadas, y estructura clara. Usa cuando el usuario pida "crear PDF", "generar informe", "documento profesional", o "reporte en PDF".
---

# PDF Generator - Documentos Profesionales

## Instalación
```bash
pip install reportlab pypdf Pillow
```

## Estructura de un PDF Profesional

### 1. Portada
- Título grande y centrado
- Subtítulo descriptivo
- Fecha y autor
- Tabla de información resumen

### 2. Índice
- Lista de secciones con números
- Referencias cruzadas

### 3. Contenido
- Headers por sección (H1, H2, H3)
- Tablas estilizadas con colores
- Cajas de información (advertencia, éxito, info)
- Listas con viñetas
- Bloques de código

### 4. Footer
- Números de página
- Clasificación de confidencialidad
- Fecha de generación

## Paleta de Colores Recomendada

```python
COLORS = {
    'primary': '#1a1a2e',      # Navy oscuro
    'secondary': '#16213e',    # Navy medio
    'accent': '#0f3460',       # Azul
    'highlight': '#e94560',    # Rojo accent
    'success': '#00b894',      # Verde
    'warning': '#fdcb6e',      # Amarillo
    'danger': '#d63031',       # Rojo
    'text': '#2d3436',         # Gris oscuro
    'text_light': '#636e72',   # Gris medio
    'bg_light': '#f5f6fa',     # Fondo claro
}
```

## Template Básico con ReportLab

```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

# Estilos
styles = getSampleStyleSheet()
styles.add(ParagraphStyle('CustomTitle', fontSize=28, textColor=colors.HexColor('#1a1a2e'), alignment=1))

# Documento
doc = SimpleDocTemplate("output.pdf", pagesize=A4, leftMargin=50, rightMargin=50, topMargin=70, bottomMargin=60)

# Contenido
story = [
    Paragraph("Título del Documento", styles['CustomTitle']),
    Spacer(1, 20),
    Paragraph("Contenido aquí...", styles['BodyText']),
]

# Tabla estilizada
data = [["Col1", "Col2", "Col3"], ["Dato1", "Dato2", "Dato3"]]
tbl = Table(data, colWidths=[1.5*inch, 1.5*inch, 1.5*inch])
tbl.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a1a2e')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
]))
story.append(tbl)

doc.build(story)
```

## Header/Footer

```python
def header_footer(canvas, doc):
    canvas.saveState()
    # Header
    canvas.setFont('Helvetica', 8)
    canvas.drawString(50, A4[1] - 45, "Título del Documento")
    canvas.drawRightString(A4[0] - 50, A4[1] - 45, "Fecha")
    # Footer
    canvas.line(50, 40, A4[0] - 50, 40)
    canvas.drawString(50, 28, "Confidencial")
    canvas.drawRightString(A4[0] - 50, 28, f"Página {doc.page}")
    canvas.restoreState()

doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
```

## Validación
```bash
python -c "from pypdf import PdfReader; r=PdfReader('output.pdf'); print(f'Páginas: {len(r.pages)}')"
```
