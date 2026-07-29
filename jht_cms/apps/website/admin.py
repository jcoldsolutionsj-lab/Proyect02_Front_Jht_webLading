from django.contrib import admin
from .models import Pagina, BloqueSeccion, ItemBloque, Servicio, FlotaVehiculo, ConfiguracionGlobal

class ItemBloqueInline(admin.TabularInline):
    model = ItemBloque
    extra = 1
    fields = ('titulo', 'descripcion', 'imagen_icono', 'enlace_url', 'orden', 'activo')

class BloqueSeccionInline(admin.StackedInline):
    model = BloqueSeccion
    extra = 0
    fields = ('tipo_bloque', 'titulo', 'subtitulo', 'imagen_fondo', 'video_fondo', 'orden', 'activo')

@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'activa')
    prepopulated_fields = {'slug': ('titulo',)}
    inlines = [BloqueSeccionInline]

@admin.register(BloqueSeccion)
class BloqueSeccionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'pagina', 'tipo_bloque', 'orden', 'activo')
    list_filter = ('pagina', 'tipo_bloque')
    inlines = [ItemBloqueInline]
    
@admin.register(ItemBloque)
class ItemBloqueAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'bloque', 'orden', 'activo')
    list_filter = ('bloque__pagina', 'bloque__tipo_bloque')

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden', 'activo')
    list_editable = ('orden', 'activo')
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields = ('titulo', 'descripcion_corta')

@admin.register(FlotaVehiculo)
class FlotaVehiculoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'orden', 'activo')
    list_filter = ('categoria', 'activo')
    list_editable = ('orden', 'activo')
    search_fields = ('nombre',)

@admin.register(ConfiguracionGlobal)
class ConfiguracionGlobalAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'telefono_principal', 'correo_contacto')

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)
