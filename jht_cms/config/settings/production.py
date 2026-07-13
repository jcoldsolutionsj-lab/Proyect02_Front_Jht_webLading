"""
Servicios Logísticos JHT - Django CMS
Settings de PRODUCCIÓN
"""

from .base import *  # noqa: F401, F403

# ===========================================
# PRODUCCIÓN
# ===========================================
DEBUG = False

# Seguridad
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

# WhiteNoise para archivos estáticos (se instalará más adelante)
# MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
