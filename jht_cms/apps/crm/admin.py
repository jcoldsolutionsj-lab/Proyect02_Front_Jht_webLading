from django.contrib import admin
from .models import CrmContacto, CrmSolicitud

@admin.register(CrmContacto)
class CrmContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'empresa', 'correo', 'telefono', 'fecha_registro')
    search_fields = ('nombre', 'apellido', 'empresa', 'correo', 'telefono')
    list_filter = ('fecha_registro',)
    ordering = ('-fecha_registro',)

@admin.register(CrmSolicitud)
class CrmSolicitudAdmin(admin.ModelAdmin):
    list_display = ('contacto', 'origen', 'servicio_interes', 'estado_ventas', 'fecha_solicitud')
    search_fields = ('contacto__nombre', 'contacto__correo', 'contacto__empresa')
    list_filter = ('estado_ventas', 'origen', 'servicio_interes', 'fecha_solicitud')
    ordering = ('-fecha_solicitud',)
    list_editable = ('estado_ventas',) # Permite a ventas cambiar el estado desde la lista
