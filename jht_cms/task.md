# 📋 Task Tracker — Django CMS JHT

## Paso 1 — Instalar Django y Crear Estructura Base ✅ COMPLETADO
- [x] Crear rama `feature/django-setup`
- [x] Crear carpeta `jht_cms/`
- [x] Crear entorno virtual (`venv`)
- [x] Instalar Django 6.0.7 + dependencias (psycopg2, Pillow, python-decouple, django-tailwind)
- [x] Crear proyecto Django (`startproject config .`)
- [x] Crear las 6 apps (core, cms, website, service_status, service_management, integrations)
- [x] Crear carpetas (templates, static_src, static, media, requirements)
- [x] Configurar settings divididos (base/development/production)
- [x] Configurar PostgreSQL (Render) — DB: `db_jht_q05l`
- [x] Configurar `.env` con credenciales
- [x] Actualizar `.gitignore` para Python/Django
- [x] Ejecutar migraciones → 18 migraciones OK
- [x] Verificar con `python manage.py check` → 0 issues

## Paso 2 — Configurar Settings (FUSIONADO CON PASO 1)
- [x] Dividir settings en base/development/production
- [x] Configurar PostgreSQL (Render)
- [x] Configurar templates, static, media paths
- [x] Registrar apps en INSTALLED_APPS
- [x] Configurar idioma español (es-pe) / zona horaria (America/Lima)
- [x] Verificar con `python manage.py migrate` → OK

## Paso 3 — Configurar Templates Base ← SIGUIENTE
- [ ] Crear `base.html` (template madre pública)
- [ ] Crear `base_dashboard.html` (template madre panel privado)
- [ ] Migrar header.html como component
- [ ] Migrar footer.html como component
- [ ] Copiar CSS (style.css, animaciones.css, servicios.css)
- [ ] Copiar JS (main.js)
- [ ] Copiar assets (imágenes y videos)
- [ ] Verificar que una página de prueba carga correctamente

## Paso 4 — Migrar Páginas Públicas
- [ ] index.html
- [ ] servicios.html
- [ ] flota.html
- [ ] nosotros.html
- [ ] contacto.html
- [ ] landing.html

## Paso 5 — Login (auth)
- [ ] Migrar acceso.html → login.html
- [ ] Configurar Django Auth

## Paso 6 — CMS Básico
- [ ] Modelos de contenido editable
- [ ] Admin personalizado

## Paso 7 — Service Status Templates
- [ ] consulta.html
- [ ] resultado.html

## Paso 8 — Service Management Templates
- [ ] dashboard.html
- [ ] ordenes.html
- [ ] detalle_orden.html
- [ ] actualizar_estado.html
- [ ] documentos.html

## Paso 9 — Integrations (Stubs)
- [ ] base_client.py
- [ ] operations_client.py
- [ ] README de integración

## Paso 10 — README Operativo + Limpieza
- [ ] README.md completo
- [ ] Limpieza final
- [ ] Merge a main
