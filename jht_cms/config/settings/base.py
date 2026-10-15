"""
Servicios Logísticos JHT - Django CMS
Settings base compartidos entre desarrollo y producción.
"""

import os
from pathlib import Path
from decouple import config, Csv

# ===========================================
# PATHS
# ===========================================
# BASE_DIR apunta a jht_cms/ (donde está manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ===========================================
# SEGURIDAD
# ===========================================
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())

# ===========================================
# APLICACIONES
# ===========================================
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'tailwind',
    'storages',
    'rest_framework',
]

LOCAL_APPS = [
    'apps.core',
    'apps.website',
    'apps.noticias',            # Módulo de Noticias y Novedades JHT
    'apps.service_status',
    'apps.service_management',
    'apps.integrations',
    'apps.crm',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ===========================================
# MIDDLEWARE
# ===========================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ===========================================
# URLS Y WSGI
# ===========================================
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

# ===========================================
# TEMPLATES
# ===========================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ===========================================
# BASE DE DATOS
# ===========================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='jht_cms_db'),
        'USER': config('DB_USER', default=''),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# ===========================================
# VALIDACIÓN DE CONTRASEÑAS
# ===========================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ===========================================
# INTERNACIONALIZACIÓN
# ===========================================
LANGUAGE_CODE = 'es-pe'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True

# ===========================================
# ARCHIVOS ESTÁTICOS (CSS, JS, Imágenes)
# ===========================================
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static_src',
]
STATIC_ROOT = BASE_DIR / 'static'

# ===========================================
# ARCHIVOS MEDIA (Uploads del CMS)
# ===========================================
USE_S3 = config('USE_S3', default=False, cast=bool)

if USE_S3:
    # Cloudflare R2 / AWS S3 Settings
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_ENDPOINT_URL = config('AWS_S3_ENDPOINT_URL')
    
    # Optional settings
    AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME', default='auto') 
    AWS_S3_CUSTOM_DOMAIN = config('AWS_S3_CUSTOM_DOMAIN', default=None)
    
    # Configuraciones críticas para Cloudflare R2
    AWS_S3_SIGNATURE_VERSION = 's3v4'
    AWS_S3_ADDRESSING_STYLE = 'path' # Evita que boto3 trate de crear subdominios con el nombre del bucket
    
    # Desactivar URLs firmadas para usar el Custom Domain / Public URL
    AWS_QUERYSTRING_AUTH = False
    
    # Evitar sobreescribir archivos con el mismo nombre
    AWS_S3_FILE_OVERWRITE = False

    # Use S3 for media storage
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
else:
    # Local Storage Fallback
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'

# ===========================================
# CAMPO AUTO POR DEFECTO
# ===========================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ===========================================
# AUTENTICACIÓN
# ===========================================
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/gestion/'
LOGOUT_REDIRECT_URL = '/'
