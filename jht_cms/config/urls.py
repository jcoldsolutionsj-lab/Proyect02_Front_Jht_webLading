"""
Servicios Logísticos JHT - Django CMS
URL Configuration
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin Django
    path('admin/', admin.site.urls),

    # Autenticación
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Apps
    path('rastreo/', include('apps.service_status.urls')),
    path('gestion/', include('apps.service_management.urls')),

    # Sitio web público (al final, ya que incluye la raíz '/')
    path('', include('apps.website.urls')),
]

# Servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
