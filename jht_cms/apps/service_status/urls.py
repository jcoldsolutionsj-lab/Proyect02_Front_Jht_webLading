from django.urls import path
from . import views

app_name = 'service_status'

urlpatterns = [
    path('', views.ConsultaView.as_view(), name='consulta'),
    path('resultado/', views.ResultadoView.as_view(), name='resultado'),
]
