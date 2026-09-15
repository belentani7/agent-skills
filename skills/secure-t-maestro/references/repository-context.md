# Contexto de secure-t

## Producto

secure-t es una plataforma educativa con currículo, lecciones, evidencias, progreso, expediente, credenciales, investigación, workspaces institucionales y un cyber-range previsto. La aplicación no debe presentarse como universidad acreditada ni como laboratorio aislado real hasta completar las integraciones y revisiones correspondientes.

## Stack observado

| Área | Tecnología o ruta |
|---|---|
| Cliente | React 19, Vite, TailwindCSS 4, shadcn/ui, Recharts, Framer Motion |
| Servidor | Express, Node.js 22, TypeScript 5.6 |
| Datos | PostgreSQL previsto, Drizzle ORM, fallback en memoria para desarrollo |
| IA | `ai/`, gateway, permisos, proveedores y fuentes aprobadas |
| Academia | `academic/` |
| Labs | `labs/`, worker aislado previsto |
| Voz | `voice/`, consentimiento y adaptadores |
| Auditoría | `audit/` |
| Notificaciones | `notifications/` |
| Verificación | Vitest, TypeScript strict, GitHub Actions |

## Estado y dependencias

La vertical slice local cubre catálogo, lecciones, evidencias, progreso, notificaciones, contratos RBAC/IA, algunas vistas de expediente/credenciales/research y workspaces. Persistencia PostgreSQL productiva, OIDC/Keycloak, Redis, S3/MinIO, cyber-range real, VAPID, TTS autoalojado y credenciales verificables requieren infraestructura y secretos.

## Regla de compatibilidad

No introducir Java sólo porque el usuario mencione “renderizado Java”. Primero comprobar si existe `pom.xml`, `build.gradle`, `*.java` o un servicio JVM. Si no existe, tratar Java como extensión propuesta y mantener el camino principal React/TypeScript.
