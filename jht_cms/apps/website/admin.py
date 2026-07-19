from django.contrib import admin
from .models import Servicio, VehiculoFlota, Cliente, SitioConfiguracion, SeccionLanding, Beneficio, PasoTrabajo, PreguntaFrecuente

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

@admin.register(SeccionLanding)
class SeccionLandingAdmin(admin.ModelAdmin):
    list_display = ('get_seccion_display', 'titulo', 'activo')
    list_filter = ('activo',)
    list_editable = ('activo',)

@admin.register(Beneficio)
class BeneficioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden', 'activo')
    list_editable = ('orden', 'activo')
    search_fields = ('titulo', 'descripcion')

@admin.register(PasoTrabajo)
class PasoTrabajoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'titulo', 'activo')
    list_editable = ('activo',)
    search_fields = ('titulo', 'descripcion')

@admin.register(PreguntaFrecuente)
class PreguntaFrecuenteAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'orden', 'activo')
    list_editable = ('orden', 'activo')
    search_fields = ('pregunta', 'respuesta')
