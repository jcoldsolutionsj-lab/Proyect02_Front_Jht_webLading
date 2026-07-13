from django.contrib import admin
from .models import Servicio, VehiculoFlota, Cliente, SitioConfiguracion

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden', 'activo')
    list_editable = ('orden', 'activo')
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields = ('titulo', 'descripcion_corta')

@admin.register(VehiculoFlota)
class VehiculoFlotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'orden', 'activo')
    list_filter = ('categoria', 'activo')
    list_editable = ('orden', 'activo')
    search_fields = ('nombre',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'orden', 'activo')
    list_editable = ('orden', 'activo')
    search_fields = ('nombre',)

@admin.register(SitioConfiguracion)
class SitioConfiguracionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'telefono_principal', 'correo_contacto')

    def has_add_permission(self, request):
        """Prevenir que se cree más de una configuración"""
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)
