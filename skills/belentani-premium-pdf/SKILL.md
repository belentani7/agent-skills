---
name: belentani-premium-pdf
description: |
  Genera CVs y documentos PDF premium con diseño cognitivo de alto impacto.
  Basado en la estructura cognitiva de Ausubel + principios de dopamine design.
  Patrones: navy-gold, curiosity gaps, métricas cuantificadas, ATS-safe.
---

# Belentani Premium PDF Skill v2.0

## Instalación
```bash
pip install reportlab pypdf Pillow
```

## Filosofía de Diseño

### Estructura Cognitiva (Ausubel)
- **Diferenciación progresiva**: Cada sección añade profundidad sin romper el flujo
- **Reconciliación integradora**: La información nueva se conecta con lo conocido
- **Principio Ausubel**: "Lo más importante que influye en el aprendizaje es lo que el alumno ya sabe"

### Dopamine Design para CVs
1. **Curiosity Gap**: Abrir con información incompleta que genere interés
2. **Quantified Reward**: Métricas concretas que activan circuitos de recompensa
3. **Open Loop**: Dejar preguntas que inviten a seguir leyendo
4. **Zeigarnik Effect**: Secciones que crean tensión resoluble

### Paleta de Colores Premium
```python
COLORS = {
    'primary': '#0a1628',       # Navy oscuro profundo
    'secondary': '#1a2d4a',     # Navy medio
    'accent': '#c9a84c',        # Gold clásico
    'accent_light': '#e8d5a3',  # Gold claro
    'text': '#1a1a2e',          # Texto oscuro
    'text_light': '#4a5568',    # Texto secundario
    'bg_light': '#f7f9fc',      # Fondo claro
    'white': '#ffffff',
    'border': '#d4a853',        # Borde gold
}
```

## Estructura del CV Premium (4 capas cognitivas)

### Capa 1: DATOS (Hechos - Representación simbólica)
- Nombre completo, contacto, redes
- Header con línea dorada decorativa
- Sin foto, sin diseño recargado
- Tipografía: Space Grotesk (títulos) + Inter (cuerpo)

### Capa 2: COMPETENCIAS (Percepción - Razonamiento lógico)
- Core competencies como skill cards con iconos
- Cada skill tiene: nombre, nivel, escala cuantificable
- Organizado por dominio (3-4 categorías)
- Diferenciación progresiva: de general a específico

### Capa 3: IMPACTO (Acción - Diferenciación progresiva)
- Logros cuantificados con métricas
- Estrategia de dopamine: cada bullet genera "recompensa"
- Formato: Acción → Resultado → Métrica
- Curiosity gaps entre proyectos

### Capa 4: VISIÓN (Síntesis - Reconciliación integradora)
- Objetivos de carrera
- Conexión entre pasado y futuro
- Call to action implícito
- Cierre con loop abierto (invita a conversación)

## Template ReportLab (con prefijos BV_)

```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

# Configuración global
PAGE = A4
MARGINS = {'left': 45, 'right': 45, 'top': 55, 'bottom': 50}

# Estilos cognitivos - todos con prefijo BV_ para evitar colisiones
def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle('BV_Title', fontName='Helvetica-Bold', fontSize=24, textColor=colors.HexColor('#0a1628'), spaceAfter=2))
    styles.add(ParagraphStyle('BV_Subtitle', fontName='Helvetica', fontSize=11, textColor=colors.HexColor('#c9a84c'), spaceAfter=4))
    styles.add(ParagraphStyle('BV_SectionHeader', fontName='Helvetica-Bold', fontSize=13, textColor=colors.HexColor('#0a1628'), spaceBefore=12, spaceAfter=4))
    styles.add(ParagraphStyle('BV_Body', fontName='Helvetica', fontSize=9, leading=13, textColor=colors.HexColor('#1a1a2e'), spaceAfter=3))
    styles.add(ParagraphStyle('BV_Metric', fontName='Helvetica-Bold', fontSize=9, textColor=colors.HexColor('#c9a84c')))
    styles.add(ParagraphStyle('BV_Bullet', fontName='Helvetica', fontSize=9, leading=12, leftIndent=10, bulletIndent=2, spaceAfter=2))
    styles.add(ParagraphStyle('BV_Footer', fontName='Helvetica', fontSize=7, textColor=colors.HexColor('#4a5568'), alignment=TA_CENTER))
    return styles
```

## Patrones de Contenido Dopamina

### Formato de Achievement Bullet:
```
&#8226; [VERBO_ACCION] [OBJETO] -> [MÉTRICA] -> [IMPACTO]
Ej: "Architected workforce platform -> 340% ROI -> $2.1M waste eliminated"
```

### Curiosity Gap Opening:
```
"Built the glue that makes complex operational systems coherent.
Where Workday handles HR, Twilio handles messaging, and Claude handles AI—
but nobody integrates all three with legal compliance."
```

### Open Loop Closing:
```
"5 pilot customers validating market fit. References available under NDA.
Let's discuss what 8.4x efficiency looks like for your organization."
```

## Reglas Anti-Cliché

❌ ELIMINAR: "Passionate", "Dedicated", "Hardworking", "Team player", "Dynamic", "Innovative", "Proactive"
✅ REEMPLAZAR: Verbos de acción + métricas + resultado cuantificable

## Output
- PDF A4, 2 páginas máximo
- Navy-gold premium aesthetic
- ATS-safe (texto seleccionable, sin tablas complejas)
- Font: Helvetica family (universal ATS compatibility)
- Tamaño fuente: 9-11pt cuerpo, 24pt nombre, 13pt secciones

## Uso
```bash
python generate_premium_cv.py --input profile_data.json --output CV_Premium.pdf --theme belentani
```

## Validación
```bash
python -c "from pypdf import PdfReader; r=PdfReader('output.pdf'); print(f'Pages: {len(r.pages)}')"
```

## Archivos de Referencia
- Inventario completo: `C:\Users\USER\Desktop\INVENTARIO_CURRICULUMS.md`
- Generador: `C:\Users\USER\Desktop\generate_premium_cv.py`
- CV generado: `C:\Users\USER\Desktop\PEDRO_BELENTANI_PREMIUM_CV.pdf`
- Perfil unificado: `C:\Users\USER\Documents\01_PROYECTOS\CONSOLIDADO\BELENTANI\03-DOCUMENTOS\03_PERFIL-CV\PEDRO_BELENTANI_CVD_UNIFIED_2026.md`
- Framework capacidades: `C:\Users\USER\Downloads\NOIACORE\capacidades_1.html`
