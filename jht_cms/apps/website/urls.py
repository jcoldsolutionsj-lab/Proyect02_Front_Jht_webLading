from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('servicios/', views.ServiciosView.as_view(), name='servicios'),
    path('flota/', views.FlotaView.as_view(), name='flota'),
    path('nosotros/', views.NosotrosView.as_view(), name='nosotros'),
    path('contacto/', views.ContactoView.as_view(), name='contacto'),
    path('landing/', views.LandingView.as_view(), name='landing'),
    
    # Rutas de prueba para diseño de Frontend (Noticias)
    path('noticias/', TemplateView.as_view(template_name='public/noticias.html'), name='noticias'),
    path('noticias/ejemplo/', TemplateView.as_view(template_name='public/noticia_detalle.html'), name='noticia_detalle'),
]
