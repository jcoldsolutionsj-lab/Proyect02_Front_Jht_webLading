from django.urls import path
from .views import ContactoSolicitudAPIView

app_name = 'crm'

urlpatterns = [
    path('lead/', ContactoSolicitudAPIView.as_view(), name='registro_lead'),
]
