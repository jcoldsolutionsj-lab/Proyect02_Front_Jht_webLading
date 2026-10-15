from django.urls import path
from . import views
from apps.noticias.views import NoticiasListView, NoticiaDetalleView

app_name = 'website'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('servicios/', views.ServiciosView.as_view(), name='servicios'),
    path('flota/', views.FlotaView.as_view(), name='flota'),
    path('nosotros/', views.NosotrosView.as_view(), name='nosotros'),
    path('contacto/', views.ContactoView.as_view(), name='contacto'),
    path('landing/', views.LandingView.as_view(), name='landing'),

    # ── Módulo de Noticias ────────────────────────────────────────────────────
    path('noticias/', NoticiasListView.as_view(), name='noticias'),
    path('noticias/<slug:slug>/', NoticiaDetalleView.as_view(), name='noticia_detalle'),
]
