from django.views.generic import TemplateView


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
