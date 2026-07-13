"""
Servicios Logísticos JHT - Django CMS
Settings de PRODUCCIÓN
"""

from .base import *  # noqa: F401, F403

# ===========================================
# PRODUCCIÓN
# ===========================================
import os
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Seguridad
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

# ===========================================
# STATIC FILES (WhiteNoise)
# ===========================================
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ===========================================
# BASE DE DATOS (SSL requerido en Render)
# ===========================================
DATABASES['default']['OPTIONS'] = {'sslmode': 'require'}
