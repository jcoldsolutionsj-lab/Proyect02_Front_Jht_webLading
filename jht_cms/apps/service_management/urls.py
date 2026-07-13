from django.urls import path
from . import views

app_name = 'service_management'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('ordenes/', views.OrdenesListView.as_view(), name='ordenes'),
    path('ordenes/<int:pk>/', views.OrdenDetailView.as_view(), name='detalle_orden'),
    path('ordenes/<int:pk>/estado/', views.ActualizarEstadoView.as_view(), name='actualizar_estado'),
    path('documentos/', views.DocumentosView.as_view(), name='documentos'),
]
