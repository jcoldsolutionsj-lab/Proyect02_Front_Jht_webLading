from django.views.generic import TemplateView
from .models import Servicio, VehiculoFlota, Cliente, SitioConfiguracion, SeccionLanding, Beneficio, PasoTrabajo, PreguntaFrecuente


class IndexView(TemplateView):
    """Página principal del sitio web."""
    template_name = 'public/index.html'


class ServiciosView(TemplateView):
    """Página de servicios."""
    template_name = 'public/servicios.html'


class FlotaView(TemplateView):
    """Página de flota."""
    template_name = 'public/flota.html'


class NosotrosView(TemplateView):
    """Página nosotros."""
    template_name = 'public/nosotros.html'


class ContactoView(TemplateView):
    """Página de contacto."""
    template_name = 'public/contacto.html'


class LandingView(TemplateView):
    """Landing page."""
    template_name = 'public/landing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Modelos existentes
        context['servicios'] = Servicio.objects.filter(activo=True)
        context['vehiculos'] = VehiculoFlota.objects.filter(activo=True)
        context['clientes'] = Cliente.objects.filter(activo=True)
        context['config'] = SitioConfiguracion.objects.first()

        # Nuevos modelos de Secciones
        # Convertimos las secciones a un diccionario para accederlas fácilmente en el template: {{ secciones.HERO.titulo }}
        secciones_activas = SeccionLanding.objects.filter(activo=True)
        context['secciones'] = {sec.seccion: sec for sec in secciones_activas}

        context['beneficios'] = Beneficio.objects.filter(activo=True)
        context['pasos'] = PasoTrabajo.objects.filter(activo=True)
        context['faqs'] = PreguntaFrecuente.objects.filter(activo=True)
        return context
