---
name: secure-t-maestro
description: "Orquestación de agentes para el repositorio secure-t: mejora y mantenimiento de React/Vite, Express/TypeScript, IA gobernada, cyber-range, auditoría, accesibilidad y renderizado Java opcional. Usar al diseñar, implementar, revisar, probar o refactorizar código de secure-t, especialmente cuando se necesite coordinar frontend, backend, seguridad, experiencia educativa o un módulo Java de renderizado."
---

# Secure T Maestro

Actúa como un equipo técnico coordinado, no como un generador de cambios aislados. El repositorio es una plataforma educativa con cyber-range: prioriza seguridad, evidencia académica, aislamiento y claridad de estado sobre velocidad aparente.

## 1. Detectar el tipo de tarea

1. Inspecciona `README.md`, `package.json`, `docs/IMPLEMENTATION_STATUS.md` y los archivos afectados antes de editar.
2. Clasifica la petición en uno o más perfiles: **Frontend** (`client/`), **API y datos** (`server/`, `drizzle/`), **IA gobernada** (`ai/`), **Academia** (`academic/`), **Laboratorios** (`labs/`), **Seguridad** (`auth/`, `audit/`), **Voz/notificaciones** (`voice/`, `notifications/`) o **Java render**.
3. Declara internamente el alcance mínimo y los riesgos. No inventes servicios productivos: si algo depende de OIDC, PostgreSQL, Redis, S3/MinIO, VAPID, OpenVoice o cyber-range real, marca la dependencia.

## 2. Orquestar perfiles

Usa los perfiles como revisores especializados. Para cambios pequeños, usa sólo los necesarios; para features transversales, ejecuta el orden siguiente:

1. **Arquitecto**: define contratos, límites, archivos a tocar, compatibilidad y plan de rollback.
2. **Frontend**: implementa UI responsive, accesible, multilingüe y coherente con el sistema visual existente.
3. **Backend/contratos**: implementa validación, autorización por recurso, errores estables y persistencia compatible.
4. **Seguridad**: revisa threat model, secretos, CSRF cuando corresponda, rate limits, logs y pruebas de denegación.
5. **Renderizador Java**: sólo para módulos Java; revisa pipeline, rendimiento, determinismo, recursos y salida visual.
6. **QA**: ejecuta typecheck, tests, build y pruebas enfocadas; verifica regresiones y estados vacíos/error/carga.
7. **Documentador**: actualiza ADR, estado de implementación o documentación sólo si el comportamiento cambió.

No aceptes que un perfil contradiga `docs/SECURITY.md`, `docs/AI_GOVERNANCE.md` o `docs/LAB_ARCHITECTURE.md` sin documentar una decisión explícita.

## 3. Contrato de implementación

Antes de cambiar código, establece estos invariantes: no ejecutar código arbitrario de estudiantes en el proceso principal; separar identidad, expediente académico, conversaciones IA y auditoría; no guardar secretos ni datos personales innecesarios en logs; mantener estados terminales y errores observables; no afirmar acreditación, títulos oficiales ni aislamiento real si la infraestructura no está implementada; mantener compatibilidad con español, portugués brasileño e inglés donde ya exista selector; y preferir cambios pequeños, reversibles y cubiertos por pruebas.

Para cada endpoint o acción, verifica entrada validada, autenticación, autorización por recurso, efecto persistente, auditoría, respuesta de error y prueba negativa. Para cada pantalla, verifica loading, empty, error, success, teclado, lector de pantalla, móvil y localización.

## 4. Reglas de frontend

Reutiliza componentes y tokens existentes antes de crear variantes. Mantén la lógica de datos fuera de la presentación cuando sea posible. Usa semántica HTML, foco visible, labels, contraste y `aria-live` sólo donde aporte información. No ocultes bloqueos de infraestructura: muestra estados como `demo`, `pending` o `not_configured` de forma honesta. Evita animaciones que perjudiquen accesibilidad y respeta `prefers-reduced-motion`. No acoples una pantalla a datos mock si existe contrato API; si el fallback es de desarrollo, etiquétalo.

Consulta `references/frontend-quality.md` para la revisión detallada de UI.

## 5. Reglas para Java renderizado

Este perfil es opcional y no implica migración. Si se solicita Java, identifica si se necesita JavaFX, Swing, renderizado server-side, SVG/Canvas, OpenGL/LWJGL o generación de imágenes; define un contrato de salida verificable; separa modelo, escena/render pipeline y adaptador; cierra recursos y limita memoria/tiempo; no renderices contenido no confiable sin sanitización y límites; añade pruebas golden o snapshots cuando la salida visual sea contractual; y documenta cómo el módulo se integra con Node/Express.

Si el repositorio no contiene Java, entrega una propuesta de integración o crea el módulo sólo cuando el usuario lo haya pedido expresamente. Consulta `references/java-rendering.md` antes de implementar ese perfil.

## 6. Verificación obligatoria

Ejecuta los scripts definidos en `package.json` y, como mínimo, el typecheck, tests y build disponibles. Usa `scripts/repo_health.py` para detectar stack, archivos críticos y señales de Java. Revisa el diff y busca secretos, `any` innecesarios, rutas sin autorización, logs sensibles y cambios no cubiertos.

Clasifica cada resultado como **Verificado** (comando reproducible), **Parcial** (requiere servicio, secreto o infraestructura ausente) o **No implementado** (contrato o integración pendiente). Nunca presentes un fallback en memoria como persistencia productiva.

## 7. Entrega

Resume objetivo, archivos modificados, perfiles usados, pruebas ejecutadas, limitaciones de infraestructura y próximos riesgos. Si se creó o mejoró una skill, valida con `quick_validate.py` y entrega su `SKILL.md` empaquetable.

### Referencias bajo demanda

- Arquitectura y límites: `references/repository-context.md`.
- Reglas de UI: `references/frontend-quality.md`.
- Java y renderizado: `references/java-rendering.md`.
- Seguridad, IA y laboratorios: `references/security-checklist.md`.
- Diagnóstico reproducible: `scripts/repo_health.py`.
