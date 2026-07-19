from django.db import models

class Servicio(models.Model):
    """Modelo para administrar los servicios de JHT"""
    titulo = models.CharField("Título del Servicio", max_length=100)
    slug = models.SlugField("URL Slug", unique=True, help_text="Se genera automáticamente a partir del título.")
    descripcion_corta = models.TextField("Descripción Corta", max_length=255, help_text="Texto breve que aparece en las tarjetas de la página de inicio.")
    descripcion_larga = models.TextField("Descripción Larga", help_text="Texto completo que aparece en el detalle del servicio.")
    icono = models.FileField("Icono (SVG/PNG)", upload_to='servicios/iconos/', blank=True, null=True, help_text="Opcional. Icono representativo.")
    imagen_banner = models.ImageField("Imagen Banner", upload_to='servicios/banners/', help_text="Imagen principal del servicio.")
    orden = models.PositiveIntegerField("Orden", default=0, help_text="Orden de aparición (0 es el primero).")
    activo = models.BooleanField("Activo", default=True, help_text="Si está desmarcado, el servicio no aparecerá en la web.")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['orden', 'titulo']

    def __str__(self):
        return self.titulo


class VehiculoFlota(models.Model):
    """Modelo para administrar la flota de vehículos de JHT"""
    CATEGORIAS_FLOTA = [
        ('liviana', 'Flota Liviana'),
        ('mediana', 'Flota Mediana'),
        ('pesada', 'Flota Pesada'),
    ]

    nombre = models.CharField("Nombre del Vehículo", max_length=100, help_text="Ej. Furgón 2 Toneladas")
    categoria = models.CharField("Categoría", max_length=20, choices=CATEGORIAS_FLOTA, default='liviana')
    capacidad_carga = models.CharField("Capacidad de Carga", max_length=50, help_text="Ej. 1.5 a 3 Toneladas")
    capacidad_volumen = models.CharField("Capacidad de Volumen", max_length=50, help_text="Ej. 15 a 20 m3")
    descripcion = models.TextField("Descripción", help_text="Breve descripción del vehículo y su uso ideal.")
    imagen = models.ImageField("Imagen del Vehículo", upload_to='flota/')
    orden = models.PositiveIntegerField("Orden", default=0)
    activo = models.BooleanField("Activo", default=True)

    class Meta:
        verbose_name = "Vehículo de Flota"
        verbose_name_plural = "Vehículos de Flota"
        ordering = ['categoria', 'orden']

    def __str__(self):
        return f"{self.nombre} ({self.get_categoria_display()})"


class Cliente(models.Model):
    """Modelo para el carrusel de clientes"""
    nombre = models.CharField("Nombre del Cliente", max_length=100)
    logo = models.ImageField("Logo del Cliente", upload_to='clientes/', help_text="Usar PNG transparente o WebP.")
    enlace = models.URLField("Enlace web", blank=True, null=True, help_text="Enlace a la web del cliente (Opcional)")
    orden = models.PositiveIntegerField("Orden", default=0)
    activo = models.BooleanField("Activo", default=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre


class SitioConfiguracion(models.Model):
    """Modelo Singleton para la configuración general del sitio"""
    telefono_principal = models.CharField("Teléfono Principal", max_length=20, default="+51 999 999 999")
    whatsapp = models.CharField("WhatsApp (Solo números)", max_length=20, help_text="Ej. 51999999999", default="51999999999")
    correo_contacto = models.EmailField("Correo de Contacto", default="operaciones@jht.com")
    direccion = models.TextField("Dirección Física", default="Av. Ejemplo 123, Lima, Perú")
    enlace_facebook = models.URLField("Facebook URL", blank=True, null=True)
    enlace_linkedin = models.URLField("LinkedIn URL", blank=True, null=True)
    enlace_instagram = models.URLField("Instagram URL", blank=True, null=True)
    
    # Textos adicionales
    texto_footer = models.TextField("Texto corto Footer", default="Expertos en logística y transporte a nivel nacional.", blank=True)

    class Meta:
        verbose_name = "Configuración del Sitio"
        verbose_name_plural = "Configuraciones del Sitio"

    def __str__(self):
        return "Configuración Global del Sitio JHT"

    def save(self, *args, **kwargs):
        """Asegurar que solo exista una instancia de configuración (Singleton)"""
        if self.__class__.objects.exists() and not self.pk:
            # Si ya existe una, no permitir crear otra. Solo editar.
            return
        super().save(*args, **kwargs)

class SeccionLanding(models.Model):
    """Modelo para administrar los Títulos y Multimedia de cada sección de la Landing"""
    SECCIONES = [
        ('HERO', 'Sección Principal (Hero)'),
        ('SERVICIOS', 'Sección Servicios'),
        ('FLOTA', 'Sección Nuestra Flota'),
        ('BENEFICIOS', 'Sección Beneficios'),
        ('PROCESO', 'Sección Cómo Trabajamos'),
        ('NOSOTROS', 'Sección Sobre Nosotros'),
        ('CLIENTES', 'Sección Empresas (Clientes)'),
        ('COBERTURA', 'Sección Cobertura Nacional'),
        ('CTA', 'Llamada a la acción (CTA final)'),
    ]
    seccion = models.CharField("Sección", max_length=20, choices=SECCIONES, unique=True)
    titulo = models.CharField("Título Principal", max_length=200, blank=True)
    subtitulo = models.TextField("Subtítulo o Descripción corta", blank=True)
    imagen = models.ImageField("Imagen", upload_to='landing/imagenes/', blank=True, null=True, help_text="Para secciones como Nosotros o Cobertura.")
    video_url = models.FileField("Video (MP4)", upload_to='landing/videos/', blank=True, null=True, help_text="Para el fondo del Hero o Cobertura.")
    activo = models.BooleanField("Mostrar Sección", default=True)

    class Meta:
        verbose_name = "Sección de Landing"
        verbose_name_plural = "Secciones de Landing"

    def __str__(self):
        return self.get_seccion_display()


class Beneficio(models.Model):
    """Modelo para la sección de Beneficios (¿Por qué elegir JHT?)"""
    titulo = models.CharField("Título", max_length=100)
    descripcion = models.TextField("Descripción", max_length=255)
    icono = models.CharField("Nombre del Ícono (Google Material Symbols)", max_length=50, default="verified", help_text="Ej: schedule, gps_fixed, verified_user, public")
    orden = models.PositiveIntegerField("Orden", default=0)
    activo = models.BooleanField("Activo", default=True)

    class Meta:
        verbose_name = "Beneficio"
        verbose_name_plural = "Beneficios"
        ordering = ['orden']

    def __str__(self):
        return self.titulo


class PasoTrabajo(models.Model):
    """Modelo para la sección de Cómo Trabajamos"""
    numero = models.PositiveIntegerField("Paso Número", unique=True, help_text="El número que aparece en el círculo.")
    titulo = models.CharField("Título", max_length=100)
    descripcion = models.TextField("Descripción", max_length=255)
    activo = models.BooleanField("Activo", default=True)

    class Meta:
        verbose_name = "Paso de Trabajo"
        verbose_name_plural = "Pasos de Trabajo"
        ordering = ['numero']

    def __str__(self):
        return f"Paso {self.numero}: {self.titulo}"


class PreguntaFrecuente(models.Model):
    """Modelo para la sección de Preguntas Frecuentes (FAQ)"""
    pregunta = models.CharField("Pregunta", max_length=255)
    respuesta = models.TextField("Respuesta")
    orden = models.PositiveIntegerField("Orden", default=0)
    activo = models.BooleanField("Activo", default=True)

    class Meta:
        verbose_name = "Pregunta Frecuente"
        verbose_name_plural = "Preguntas Frecuentes"
        ordering = ['orden']

    def __str__(self):
        return self.pregunta
