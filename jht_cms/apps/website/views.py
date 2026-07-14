from django.views.generic import TemplateView
from .models import Servicio, VehiculoFlota, Cliente, SitioConfiguracion


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
        context['servicios'] = Servicio.objects.filter(activo=True)
        context['vehiculos'] = VehiculoFlota.objects.filter(activo=True)
        context['clientes'] = Cliente.objects.filter(activo=True)
        context['config'] = SitioConfiguracion.objects.first()
        return context
