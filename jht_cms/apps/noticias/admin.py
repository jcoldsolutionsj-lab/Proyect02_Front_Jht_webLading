from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Etiqueta, Autor, Articulo, ArticuloEtiqueta, Comentario


# ─────────────────────────────────────────────────────────────────────────────
# INLINES
# ─────────────────────────────────────────────────────────────────────────────

class ArticuloEtiquetaInline(admin.TabularInline):
    """Permite gestionar las etiquetas de un artículo directamente en su formulario."""
    model = ArticuloEtiqueta
    extra = 2
    autocomplete_fields = ['etiqueta']
    verbose_name = 'Etiqueta'
    verbose_name_plural = 'Etiquetas del Artículo'


class ComentarioInline(admin.TabularInline):
    """Muestra los comentarios de un artículo directamente en su formulario."""
    model = Comentario
    extra = 0
    readonly_fields = ('nombre_autor', 'email_autor', 'contenido', 'fecha_creacion')
    fields = ('nombre_autor', 'email_autor', 'contenido', 'aprobado', 'fecha_creacion')
    can_delete = True
    verbose_name = 'Comentario'
    verbose_name_plural = 'Comentarios recibidos'


# ─────────────────────────────────────────────────────────────────────────────
# ADMINS
# ─────────────────────────────────────────────────────────────────────────────

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'slug', 'color_badge')
    search_fields = ('nombre',)
    prepopulated_fields = {'slug': ('nombre',)}


@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'slug')
    search_fields = ('nombre',)
    prepopulated_fields = {'slug': ('nombre',)}


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'cargo', 'imagen_preview')
    search_fields = ('nombre', 'cargo')

    @admin.display(description='Vista Previa')
    def imagen_preview(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="width:40px;height:40px;border-radius:50%;object-fit:cover;">', obj.imagen.url)
        return '—'


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    # ── Listado ──────────────────────────────────────────────────────
    list_display   = ('titulo', 'categoria', 'autor', 'estado_badge', 'es_destacado',
                      'vistas', 'fecha_publicacion')
    list_filter    = ('estado', 'es_destacado', 'categoria')
    list_editable  = ('es_destacado',)
    search_fields  = ('titulo', 'bajada', 'contenido_html')
    date_hierarchy = 'fecha_publicacion'
    ordering       = ('-fecha_publicacion',)

    # ── Formulario ───────────────────────────────────────────────────
    prepopulated_fields = {'slug': ('titulo',)}
    readonly_fields     = ('vistas', 'fecha_creacion', 'fecha_actualizacion')
    inlines             = [ArticuloEtiquetaInline, ComentarioInline]

    fieldsets = (
        ('📋 Identificación', {
            'fields': ('titulo', 'slug', 'bajada')
        }),
        ('📝 Contenido', {
            'fields': ('contenido_html', 'imagen_portada', 'imagen_cuerpo', 'texto_imagen_cuerpo')
        }),
        ('🗂️ Clasificación', {
            'fields': ('categoria', 'autor')
        }),
        ('⚙️ Estado y Visibilidad', {
            'fields': ('estado', 'es_destacado', 'fecha_publicacion')
        }),
        ('📊 Métricas (solo lectura)', {
            'fields': ('vistas', 'fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )

    @admin.display(description='Estado', ordering='estado')
    def estado_badge(self, obj):
        colors = {
            'publicado': '#16a34a',
            'borrador':  '#d97706',
            'archivado': '#6b7280',
        }
        color = colors.get(obj.estado, '#6b7280')
        return format_html(
            '<span style="background:{};color:white;padding:2px 10px;'
            'border-radius:9999px;font-size:11px;font-weight:bold;">{}</span>',
            color, obj.get_estado_display()
        )


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display   = ('nombre_autor', 'articulo', 'aprobado', 'fecha_creacion', 'contenido_corto')
    list_filter    = ('aprobado',)
    list_editable  = ('aprobado',)
    search_fields  = ('nombre_autor', 'email_autor', 'contenido')
    readonly_fields = ('articulo', 'nombre_autor', 'email_autor', 'contenido', 'fecha_creacion')
    ordering       = ('-fecha_creacion',)
    actions        = ['aprobar_comentarios', 'rechazar_comentarios']

    @admin.display(description='Comentario')
    def contenido_corto(self, obj):
        return obj.contenido[:80] + '...' if len(obj.contenido) > 80 else obj.contenido

    @admin.action(description='✅ Aprobar comentarios seleccionados')
    def aprobar_comentarios(self, request, queryset):
        updated = queryset.update(aprobado=True)
        self.message_user(request, f'{updated} comentario(s) aprobado(s).')

    @admin.action(description='❌ Rechazar comentarios seleccionados')
    def rechazar_comentarios(self, request, queryset):
        updated = queryset.update(aprobado=False)
        self.message_user(request, f'{updated} comentario(s) rechazado(s).')
