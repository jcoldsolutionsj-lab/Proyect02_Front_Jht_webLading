# JHT Transport - Django CMS & Frontend 🚛

Este proyecto es el módulo de **Frontend y CMS (Marketing)** para Servicios Logísticos JHT.
Sirve como capa de presentación principal (Landing Pages, Vistas de Servicios, y Autenticación).
Toda la lógica de ruteo, tracking GPS en tiempo real y operaciones logísticas se manejará mediante una **API externa construida en FastAPI**.

## Estructura del Proyecto

El proyecto está diseñado bajo una arquitectura de microservicios (desde la perspectiva del backend).
- `jht_cms/config/`: Configuraciones divididas para `base`, `development` y `production`.
- `jht_cms/apps/website/`: Vistas de las páginas públicas (Home, Servicios, Flota, Contacto).
- `jht_cms/apps/cms/`: Modelos de base de datos para manejar el contenido dinámico del marketing.
- `jht_cms/apps/service_status/`: Pantallas de seguimiento y consulta de estado (conectadas a FastAPI en un futuro).
- `jht_cms/apps/service_management/`: Panel de gestión visual de órdenes.
- `jht_cms/apps/integrations/`: Clientes y stubs para conectarse a la API FastAPI.
- `jht_cms/templates/`: Todas las plantillas HTML (migradas desde Vite/Tailwind original).

## Tecnologías

- **Backend / CMS:** Django 6.0
- **Base de Datos:** PostgreSQL (Alojado en Render `db_jht_q05l`)
- **Estilos:** TailwindCSS (Compilado externamente y servido como `static/css/style.css`)
- **Reactividad Frontend:** Alpine.js v3
- **Iconografía:** Material Symbols (Google Fonts)

## Instalación y Desarrollo Local

1. Activar el entorno virtual:
   ```bash
   venv\Scripts\activate
   ```
2. Instalar dependencias (si aplica):
   ```bash
   pip install -r requirements/base.txt
   ```
3. Aplicar migraciones:
   ```bash
   python manage.py migrate
   ```
4. Crear superusuario (Opcional):
   ```bash
   python manage.py createsuperuser
   ```
5. Levantar el servidor:
   ```bash
   python manage.py runserver
   ```

El proyecto estará disponible en `http://127.0.0.1:8000/`.

## Variables de Entorno

Asegúrate de configurar tu archivo `.env` en base a `.env.example`:
```env
DJANGO_SECRET_KEY=...
DEBUG=True
DATABASE_URL=postgres://...
OPERATIONS_API_URL=http://localhost:8001/api/v1
OPERATIONS_API_KEY=secreto
```
Usuario: admin
Contraseña: admin
(Y el correo asociado es admin@jht.com.pe por si el sistema te lo llega a pedir en algún log, aunque para iniciar sesión solo necesitas el usuario y la contraseña).

Pantallas Privadas / Administrativas:

Acceso (Login): http://127.0.0.1:8000/login/
Panel Administrador (Django Admin): http://127.0.0.1:800/admin/ (Usuario: admin / Contraseña: admin)
