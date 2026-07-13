# Integraciones con FastAPI

Esta carpeta contiene los clientes HTTP encargados de comunicarse con el **backend operativo** (FastAPI).

Dado que Django se encarga únicamente de:
- CMS (Marketing, Web Pública)
- Renderizado de Plantillas (UI)

Toda la lógica de negocio real (gestión de flotas profunda, ruteo, actualización GPS en tiempo real) vive en el microservicio FastAPI. 

## Archivos

- `base_client.py`: Clase base genérica que usa `requests` para comunicarse con la API, inyectando los headers de autorización requeridos.
- `operations_client.py`: Métodos específicos de negocio (ej. `get_tracking_info(tracking_number)`).

## Configuración Requerida

En `jht_cms/.env` se deben definir las variables:
```env
OPERATIONS_API_URL=http://localhost:8001/api/v1
OPERATIONS_API_KEY=tu_secreto_aqui
```

Luego, en `config/settings/base.py`, estas variables ya están siendo capturadas (asegúrate de agregarlas si no están).
