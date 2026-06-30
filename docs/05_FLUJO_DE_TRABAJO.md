# Flujo de Trabajo para el Desarrollo del Frontend

## 1. Objetivo
Desarrollar el frontend completo (Landing, Rastreo, Dashboard) respetando la arquitectura de ramas definida en `01_ESTRUCTURA_Y_DISEÑO.md` y los contenidos en `02_CONTENIDO_Y_MAQUETACION.md`, `03_PAGINA_DE_RASTREO.md`, `04_DASHBOARD.md`.

## 2. Reglas de trabajo
- **Cada sección debe desarrollarse en su propia rama** (ej. `feature/home`, `feature/servicios`, `feature/rastreo`, `feature/dashboard`).
- **Una vez finalizada una sección**, debes avisarme y esperar mi confirmación antes de hacer el commit y el merge a `develop`.
- **Los commits deben ser atómicos** y con mensajes claros según convención semántica (`feat:`, `fix:`, `style:`, etc.).

## 3. Orden sugerido de desarrollo
1. feature/configuracion   (base: Tailwind, estructura, variables CSS)
2. feature/components      (Header, Footer, botones, tarjetas)
3. feature/home
4. feature/landing
5. feature/servicios
6. feature/flota
7. feature/nosotros
8. feature/contacto
9. feature/rastreo
10. feature/dashboard

## 4. Entregable esperado
Código HTML, CSS y JS funcional, responsive, con los marcadores (`id`) definidos y listo para integrarse con Django en el futuro.