# Calidad frontend

## Antes de editar

Inspeccionar rutas, componentes compartidos, estilos globales, tipos y el contrato API que alimenta la vista. Reutilizar patrones existentes y evitar introducir una librería de estado o UI sin necesidad.

## Checklist visual y funcional

- Responsive en móvil, tablet y escritorio.
- Estados de carga, vacío, error, éxito y no configurado.
- Navegación por teclado y foco visible.
- Contraste y nombres accesibles para controles e iconos.
- `prefers-reduced-motion` para transiciones.
- Idiomas existentes: español, portugués brasileño e inglés.
- Fechas, números y textos sin concatenaciones frágiles.
- No exponer tokens, prompts sensibles, PII o detalles internos en el cliente.
- No representar como completada una acción que el backend no confirmó.

## Datos

Preferir tipos derivados de contratos y manejo explícito de `null`/errores. Invalidar o refrescar datos tras mutaciones. Los fallbacks locales deben tener un indicador de entorno y no simular garantías productivas.

## Pruebas

Cubrir interacción principal, permiso denegado, API fallida, contenido vacío y accesibilidad básica. Para componentes visuales complejos, usar una prueba de render o snapshot sólo si el repositorio ya usa ese patrón.
