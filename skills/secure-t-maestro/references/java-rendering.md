# Perfil Java de renderizado

## Selección de tecnología

- **JavaFX**: aplicaciones desktop con escena interactiva.
- **Swing/`BufferedImage`**: render 2D headless, exportación PNG/JPEG o compatibilidad legacy.
- **SVG/HTML server-side**: documentos vectoriales o plantillas, con sanitización estricta.
- **LWJGL/OpenGL**: sólo cuando se requiera GPU/3D; es una decisión de infraestructura, no una dependencia casual.

## Pipeline recomendado

1. Definir `RenderRequest` inmutable y validado.
2. Convertirlo a modelo de escena sin IO ni acceso a secretos.
3. Renderizar con límites de tamaño, tiempo y memoria.
4. Serializar a salida con MIME y checksum conocidos.
5. Liberar recursos y registrar sólo metadatos no sensibles.

## Integración con secure-t

Para una integración con Express, preferir un worker/proceso JVM aislado con protocolo JSONL, HTTP interno autenticado o cola. Aplicar timeout, límite de payload, límite de concurrencia, backpressure, kill/restart y healthcheck. No ejecutar Java arbitrario recibido del estudiante. Si el render procesa contenido de usuario, sanitizar SVG/HTML, limitar fuentes y evitar acceso a filesystem/red.

## Pruebas

Usar pruebas unitarias del modelo, golden images con tolerancia documentada, pruebas de payload inválido, timeout, dimensiones extremas, concurrencia y liberación de recursos. Hacer el resultado determinista: versión de fuentes, locale, timezone, antialiasing y semilla explícitos.

## Entrega

Documentar JDK soportado, build tool, comando reproducible, imagen/runtime, memoria, timeout, formato de salida y cómo se monitoriza. Si no hay código Java en el repositorio, no añadir una JVM al build principal sin una solicitud de implementación concreta.
