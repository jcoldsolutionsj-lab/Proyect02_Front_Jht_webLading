"""
Servicios Logísticos JHT - Django CMS
Settings de DESARROLLO
"""

from .base import *  # noqa: F401, F403

# ===========================================
# DESARROLLO
# ===========================================
DEBUG = True

ALLOWED_HOSTS = ['*']

# Debug toolbar (se instalará más adelante si se necesita)
# INSTALLED_APPS += ['debug_toolbar']
# MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
# INTERNAL_IPS = ['127.0.0.1']


