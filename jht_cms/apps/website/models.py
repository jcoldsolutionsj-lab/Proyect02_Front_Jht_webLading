from django.db import models
from django.utils.text import slugify

# ==========================================
# 1. NÚCLEO ESTRUCTURAL (PAGE BUILDER)
# ==========================================

class Pagina(models.Model):
    """Modelo para administrar páginas completas de forma dinámica."""
    titulo = models.CharField("Título de la Página", max_length=150)
    slug = models.SlugField("URL Slug", unique=True, blank=True, help_text="Ej: 'landing', 'nosotros'. Se genera automático.")
    meta_titulo = models.CharField("Meta Título (SEO)", max_length=150, blank=True, null=True)
    meta_descripcion = models.TextField("Meta Descripción (SEO)", blank=True, null=True)
    activa = models.BooleanField("Activa", default=True)

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "1. Páginas (Page Builder)"
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)


class BloqueSeccion(models.Model):
    """Bloques dinámicos que componen una página."""
    TIPOS_BLOQUE = [
        ('HERO', 'Hero Banner Principal'),
        ('GRID_SERVICIOS', 'Catálogo: Grid de Servicios'),
        ('GRID_FLOTA', 'Catálogo: Grid de Vehículos'),
        ('GRID_TARJETAS', 'Sección: Grid de Tarjetas (Beneficios, Pasos)'),
        ('CARRUSEL_LOGOS', 'Sección: Carrusel de Logos (Clientes)'),
        ('ACORDEON', 'Sección: Acordeón (Preguntas Frecuentes)'),
        ('TEXTO_IMAGEN', 'Sección: Texto e Imagen Alternada'),
    ]

    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE, related_name='bloques', verbose_name="Página Perteneciente")
    tipo_bloque = models.CharField("Tipo de Componente", max_length=30, choices=TIPOS_BLOQUE)
    titulo = models.CharField("Título de la Sección", max_length=200, blank=True, help_text="Aparece arriba del bloque.")
    subtitulo = models.TextField("Subtítulo", blank=True)
    imagen_fondo = models.ImageField("Imagen de Fondo", upload_to='bloques/imagenes/', blank=True, null=True)
    video_fondo = models.FileField("Video de Fondo (MP4)", upload_to='bloques/videos/', blank=True, null=True)
    orden = models.PositiveIntegerField("Orden de aparición", default=0)
    activo = models.BooleanField("Mostrar Bloque", default=True)

    class Meta:
        verbose_name = "Bloque de Sección"
        verbose_name_plural = "2. Bloques de Sección"
        ordering = ['pagina', 'orden']

    def __str__(self):
        return f"{self.pagina.titulo} - {self.get_tipo_bloque_display()} ({self.titulo})"


class ItemBloque(models.Model):
    """Contenido dinámico para bloques (Tarjetas, Logos, FAQs, Pasos). Reemplaza múltiples tablas antiguas."""
    bloque = models.ForeignKey(BloqueSeccion, on_delete=models.CASCADE, related_name='items', verbose_name="Bloque Contenedor")
    titulo = models.CharField("Título del Item", max_length=200, blank=True, help_text="Para FAQs, aquí va la pregunta.")
    descripcion = models.TextField("Descripción / Contenido", blank=True, help_text="Para FAQs, aquí va la respuesta.")
    imagen_icono = models.FileField("Imagen, Logo o Icono SVG", upload_to='bloques/items/', blank=True, null=True)
    enlace_url = models.URLField("Enlace / Link", blank=True, null=True, help_text="Opcional. Si la tarjeta o logo debe llevar a un link.")
    orden = models.PositiveIntegerField("Orden del Item", default=0)
    activo = models.BooleanField("Activo", default=True)

    class Meta:
        verbose_name = "Item de Bloque"
        verbose_name_plural = "3. Items de Bloques"
        ordering = ['bloque', 'orden']

    def __str__(self):
        return f"Item: {self.titulo or 'Contenido Visual'} (de: {self.bloque})"


# ==========================================
# 2. ENTIDADES DE NEGOCIO (CATÁLOGOS)
# ==========================================

class Servicio(models.Model):
    """Catálogo Core de Servicios."""
    titulo = models.CharField("Título del Servicio", max_length=150)
    slug = models.SlugField("URL Slug", unique=True, blank=True)
    descripcion_corta = models.TextField("Descripción Corta", max_length=255)
    descripcion_larga = models.TextField("Descripción Larga")
    icono = models.FileField("Icono (SVG/PNG)", upload_to='catalogo/servicios/iconos/', blank=True, null=True)
    imagen_banner = models.ImageField("Imagen Banner", upload_to='catalogo/servicios/banners/')
    orden = models.PositiveIntegerField("Orden", default=0)
    activo = models.BooleanField("Activo", default=True)

    class Meta:
        verbose_name = "Servicio Logístico"
        verbose_name_plural = "4. Catálogo de Servicios"
        ordering = ['orden', 'titulo']

    def __str__(self):
        return self.titulo
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)


class FlotaVehiculo(models.Model):
    """Catálogo Core de Vehículos."""
    CATEGORIAS = [
        ('LIVIANA', 'Flota Liviana'),
        ('MEDIANA', 'Flota Mediana'),
        ('PESADA', 'Flota Pesada'),
    ]
    nombre = models.CharField("Nombre del Vehículo", max_length=150)
    categoria = models.CharField("Categoría", max_length=20, choices=CATEGORIAS, default='LIVIANA')
    capacidad_carga = models.CharField("Capacidad de Carga", max_length=100)
    capacidad_volumen = models.CharField("Capacidad de Volumen", max_length=100)
    descripcion = models.TextField("Descripción", blank=True)
    imagen = models.ImageField("Imagen del Vehículo", upload_to='catalogo/flota/')
    orden = models.PositiveIntegerField("Orden", default=0)
    activo = models.BooleanField("Activo", default=True)

    class Meta:
        verbose_name = "Vehículo de Flota"
        verbose_name_plural = "5. Catálogo de Flota"
        ordering = ['categoria', 'orden']

    def __str__(self):
        return f"{self.nombre} ({self.get_categoria_display()})"


# ==========================================
# 3. VARIABLES GLOBALES (SINGLETON)
# ==========================================

class ConfiguracionGlobal(models.Model):
    """Configuración única para toda la web (Footer, Contacto, Redes)."""
    telefono_principal = models.CharField("Teléfono Principal", max_length=50, default="+51 999 999 999")
    whatsapp = models.CharField("WhatsApp (Solo números para API)", max_length=30, default="51999999999")
    correo_contacto = models.EmailField("Correo de Contacto", default="operaciones@jht.com")
    direccion = models.TextField("Dirección Física", default="Lima, Perú")
    enlace_facebook = models.URLField("Facebook URL", blank=True, null=True)
    enlace_linkedin = models.URLField("LinkedIn URL", blank=True, null=True)
    texto_footer = models.TextField("Texto corto Footer", blank=True)

    class Meta:
        verbose_name = "Configuración Global"
        verbose_name_plural = "6. Configuración Global"

    def __str__(self):
        return "Ajustes Globales del Sitio"

    def save(self, *args, **kwargs):
        if self.__class__.objects.exists() and not self.pk:
            return # Prevenir más de una instancia (Singleton pattern)
        super().save(*args, **kwargs)
