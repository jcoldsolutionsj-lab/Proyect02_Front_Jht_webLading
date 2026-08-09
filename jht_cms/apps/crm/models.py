from django.db import models
import uuid

class CrmContacto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    apellido = models.CharField(max_length=255, blank=True, null=True, verbose_name="Apellido")
    correo = models.EmailField(unique=True, verbose_name="Correo electrónico")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono / Celular")
    empresa = models.CharField(max_length=255, blank=True, null=True, verbose_name="Empresa")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    class Meta:
        db_table = 'crm_contacto'
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ['-fecha_registro']

    def __str__(self):
        if self.apellido:
            return f"{self.nombre} {self.apellido}"
        return self.nombre


class CrmSolicitud(models.Model):
    ORIGEN_CHOICES = [
        ('cotizacion', 'Cotización'),
        ('contacto_general', 'Contacto General')
    ]

    SERVICIO_CHOICES = [
        ('transporte-carga', 'Transporte de Carga'),
        ('distribucion', 'Distribución'),
        ('courier', 'Courier / Delivery Express'),
        ('mudanzas', 'Mudanzas'),
        ('carga-refrigerada', 'Carga Refrigerada'),
        ('almacenaje', 'Almacenaje'),
        ('personal-estiba', 'Personal de Estiba'),
    ]

    ESTADO_VENTAS_CHOICES = [
        ('nuevo', 'Nuevo'),
        ('en_proceso', 'En Proceso'),
        ('cotizado', 'Cotizado'),
        ('ganado', 'Ganado'),
        ('perdido', 'Perdido'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contacto = models.ForeignKey(CrmContacto, on_delete=models.CASCADE, related_name='solicitudes', verbose_name="Contacto")
    origen = models.CharField(max_length=50, choices=ORIGEN_CHOICES, verbose_name="Origen de la Solicitud")
    servicio_interes = models.CharField(max_length=100, choices=SERVICIO_CHOICES, blank=True, null=True, verbose_name="Servicio de Interés")
    mensaje = models.TextField(blank=True, null=True, verbose_name="Mensaje o Requerimiento")
    estado_ventas = models.CharField(max_length=20, choices=ESTADO_VENTAS_CHOICES, default='nuevo', verbose_name="Estado en Ventas")
    fecha_solicitud = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Solicitud")

    class Meta:
        db_table = 'crm_solicitud'
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
        ordering = ['-fecha_solicitud']

    def __str__(self):
        return f"{self.get_origen_display()} - {self.contacto} ({self.fecha_solicitud.strftime('%d/%m/%Y')})"
