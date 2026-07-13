from django.db import models

class CompanyInfo(models.Model):
    """Información general de la empresa para usar en footer y contacto."""
    name = models.CharField("Nombre de la Empresa", max_length=100, default="JHT Transport")
    email = models.EmailField("Correo de Contacto", default="contacto@jht.com.pe")
    phone = models.CharField("Teléfono", max_length=20, default="+51 987 654 321")
    address = models.CharField("Dirección", max_length=255, default="Av. Principal 123, Distrito Logístico, Ciudad.")
    
    facebook_url = models.URLField("Facebook URL", blank=True)
    linkedin_url = models.URLField("LinkedIn URL", blank=True)
    instagram_url = models.URLField("Instagram URL", blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Información de Empresa"
        verbose_name_plural = "Información de Empresa"

    def __str__(self):
        return self.name


class Service(models.Model):
    """Servicios logísticos ofrecidos por la empresa."""
    title = models.CharField("Título del Servicio", max_length=100)
    slug = models.SlugField("Slug", unique=True, help_text="URL amigable")
    icon_name = models.CharField("Icono (Material Symbols)", max_length=50, default="local_shipping")
    short_description = models.TextField("Descripción Corta", max_length=200)
    full_description = models.TextField("Descripción Completa", blank=True)
    image = models.ImageField("Imagen Representativa", upload_to='cms/services/', blank=True, null=True)
    order = models.PositiveIntegerField("Orden de visualización", default=0)
    is_active = models.BooleanField("Activo", default=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class FleetCategory(models.Model):
    """Categorías de la flota (e.g., Pesada, Liviana)."""
    name = models.CharField("Nombre de Categoría", max_length=50)
    description = models.TextField("Descripción", blank=True)
    order = models.PositiveIntegerField("Orden", default=0)

    class Meta:
        verbose_name = "Categoría de Flota"
        verbose_name_plural = "Categorías de Flota"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class FleetVehicle(models.Model):
    """Vehículos específicos dentro de la flota."""
    category = models.ForeignKey(FleetCategory, on_delete=models.CASCADE, related_name='vehicles', verbose_name="Categoría")
    name = models.CharField("Nombre/Tipo de Vehículo", max_length=100)
    capacity = models.CharField("Capacidad", max_length=100, help_text="Ej: Hasta 30 toneladas")
    features = models.TextField("Características", blank=True, help_text="Listado de características separadas por comas")
    image = models.ImageField("Imagen del Vehículo", upload_to='cms/fleet/', blank=True, null=True)
    is_active = models.BooleanField("Activo", default=True)
    order = models.PositiveIntegerField("Orden", default=0)

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.category.name})"
