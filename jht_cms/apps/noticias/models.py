from django.db import models
from django.utils.text import slugify


class Categoria(models.Model):
    """Categoría editorial de la noticia (Normativas, Tecnología, Comercio, etc.)"""
    nombre      = models.CharField('Nombre', max_length=80, unique=True)
    slug        = models.SlugField('Slug URL', max_length=80, unique=True)
    color_badge = models.CharField(
        'Clase CSS del Badge', max_length=50, default='bg-jht-gold text-jht-dark',
        help_text="Clases Tailwind para el badge de categoría en la tarjeta. Ej: bg-jht-gold text-jht-dark"
    )

    class Meta:
        db_table = 'noticias_categorias'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)


class Etiqueta(models.Model):
    """Tags libres para clasificación y SEO. Ej: MTC, GPS, BASC, Euro 6"""
    nombre = models.CharField('Nombre', max_length=50, unique=True)
    slug   = models.SlugField('Slug URL', max_length=50, unique=True)

    class Meta:
        db_table = 'noticias_etiquetas'
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)


class Autor(models.Model):
    """Firmante del artículo. Puede ser un miembro del equipo JHT o un área."""
    nombre = models.CharField('Nombre completo o Área', max_length=120)
    cargo  = models.CharField('Cargo o Especialidad', max_length=120, blank=True)
    bio    = models.TextField('Biografía corta', blank=True)
    imagen = models.ImageField(
        'Foto del Autor', upload_to='noticias/autores/',
        blank=True, null=True,
        help_text='Opcional. Foto cuadrada recomendada (200x200px).'
    )

    class Meta:
        db_table = 'noticias_autores'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    """
    Tabla central del módulo de noticias.
    Almacena el artículo editorial completo de JHT.
    """
    ESTADO_CHOICES = [
        ('borrador',  'Borrador'),
        ('publicado', 'Publicado'),
        ('archivado', 'Archivado'),
    ]

    # ── Identificación ──────────────────────────────────────────────
    titulo = models.CharField('Título', max_length=200)
    slug   = models.SlugField(
        'Slug URL', max_length=220, unique=True,
        help_text='Se genera automáticamente desde el título. Es único y forma la URL del artículo.'
    )
    bajada = models.TextField(
        'Bajada / Resumen', max_length=320,
        help_text='Texto corto (≤320 caracteres) para la tarjeta de la lista y el meta description SEO.'
    )

    # ── Contenido ───────────────────────────────────────────────────
    contenido_html = models.TextField(
        'Contenido del Artículo (HTML)',
        help_text='Cuerpo completo del artículo en formato HTML. '
                  'Próximamente se integrará un editor visual (WYSIWYG).'
    )
    imagen_portada = models.ImageField(
        'Imagen de Portada', upload_to='noticias/portadas/',
        help_text='Imagen principal del artículo. Recomendado: 1200x630px WebP.'
    )
    imagen_cuerpo = models.ImageField(
        'Imagen en el Cuerpo', upload_to='noticias/cuerpo/',
        blank=True, null=True,
        help_text='Imagen opcional que aparece a mitad del artículo para romper el bloque de texto.'
    )
    texto_imagen_cuerpo = models.CharField(
        'Pie de foto (imagen cuerpo)', max_length=200, blank=True,
        help_text='Descripción breve que aparece bajo la imagen del cuerpo del artículo.'
    )

    # ── Clasificación ───────────────────────────────────────────────
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT,
        related_name='articulos', verbose_name='Categoría',
        help_text='PROTECT: No se puede borrar una categoría que tenga artículos asociados.'
    )
    etiquetas = models.ManyToManyField(
        Etiqueta,
        through='ArticuloEtiqueta',
        related_name='articulos',
        blank=True,
        verbose_name='Etiquetas'
    )
    autor = models.ForeignKey(
        Autor, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='articulos', verbose_name='Autor',
        help_text='SET_NULL: Si se borra el autor, el artículo queda sin autor (no se pierde).'
    )

    # ── Estado / Visibilidad ────────────────────────────────────────
    estado = models.CharField(
        'Estado', max_length=12, choices=ESTADO_CHOICES,
        default='borrador', db_index=True,
        help_text='Solo los artículos "Publicados" son visibles en la web.'
    )
    es_destacado = models.BooleanField(
        '¿Artículo Destacado?', default=False,
        help_text='Si está marcado, aparece en la sección hero/principal de la página de Noticias.'
    )
    vistas = models.PositiveIntegerField(
        'Contador de Vistas', default=0, editable=False,
        help_text='Se incrementa automáticamente cada vez que alguien visita el artículo.'
    )

    # ── Fechas ──────────────────────────────────────────────────────
    fecha_publicacion   = models.DateTimeField(
        'Fecha de Publicación', null=True, blank=True,
        help_text='Dejar vacío mientras sea borrador. Se puede programar publicación futura.'
    )
    fecha_creacion      = models.DateTimeField('Creado el', auto_now_add=True)
    fecha_actualizacion = models.DateTimeField('Actualizado el', auto_now=True)

    class Meta:
        db_table = 'noticias_articulos'
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
        ordering = ['-fecha_publicacion']
        indexes = [
            # Índice compuesto: consulta más frecuente → artículos publicados ordenados por fecha
            models.Index(fields=['estado', '-fecha_publicacion'], name='idx_noticias_estado_fecha'),
            # Índice para URL lookup por slug
            models.Index(fields=['slug'], name='idx_noticias_slug'),
            # Índice para filtrar artículos destacados rápidamente
            models.Index(fields=['es_destacado'], name='idx_noticias_destacado'),
        ]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('website:noticia_detalle', kwargs={'slug': self.slug})

    def incrementar_vistas(self):
        """Incrementa el contador de vistas de forma atómica (thread-safe)."""
        Articulo.objects.filter(pk=self.pk).update(vistas=models.F('vistas') + 1)


class ArticuloEtiqueta(models.Model):
    """
    Tabla puente explícita entre Artículo y Etiqueta (M2M con through).
    Usar through explícito permite extender la relación en el futuro
    (ej: agregar 'orden', 'relevancia', 'es_principal').
    """
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)

    class Meta:
        db_table = 'noticias_articulos_etiquetas'
        unique_together = ('articulo', 'etiqueta')
        verbose_name = 'Etiqueta de Artículo'
        verbose_name_plural = 'Etiquetas de Artículos'

    def __str__(self):
        return f'{self.articulo} → {self.etiqueta}'


class Comentario(models.Model):
    """
    Comentarios de lectores en los artículos.
    Requieren aprobación manual del administrador antes de ser visibles.
    """
    articulo     = models.ForeignKey(
        Articulo, on_delete=models.CASCADE,
        related_name='comentarios', verbose_name='Artículo'
    )
    nombre_autor = models.CharField('Nombre', max_length=80)
    email_autor  = models.EmailField('Email', max_length=120,
                    help_text='No se publica. Solo para contacto interno.')
    contenido    = models.TextField('Comentario')
    aprobado     = models.BooleanField(
        'Aprobado', default=False,
        help_text='Solo los comentarios aprobados son visibles en la web pública.'
    )
    fecha_creacion = models.DateTimeField('Enviado el', auto_now_add=True)

    class Meta:
        db_table = 'noticias_comentarios'
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['fecha_creacion']

    def __str__(self):
        return f'Comentario de {self.nombre_autor} en "{self.articulo}"'
