# Checklist de seguridad y gobernanza

## API y datos

Validar entradas con esquemas; autenticar; autorizar por recurso; aplicar rate limiting; usar cookies seguras; proteger CSRF cuando corresponda; gestionar secretos fuera del código; evitar PII en logs; escanear dependencias; probar errores y permisos negativos.

## IA

Respetar permisos, separación de autoridades y `EXAM_MODE`. No generar soluciones directas durante evaluaciones cuando la política lo prohíba. Registrar decisión de autorización, herramienta, metadatos de entrada/salida, resultado y motivo de fallo sin guardar secretos ni contenido innecesario.

## Labs

La aplicación principal sólo orquesta. El worker debe usar imágenes versionadas, red aislada, credenciales cortas y límites de CPU, memoria, filesystem, tiempo y red. Destruir la instancia según cleanup policy y demostrar que no existe comunicación con producción.

## Revisión final

Buscar secretos con herramientas disponibles, revisar dependencias y headers, ejecutar tests de autorización, comprobar que acciones de alto impacto tienen workflow explícito y que la UI no oculta infraestructura pendiente. Señalar cualquier afirmación de seguridad que no tenga evidencia de prueba.
