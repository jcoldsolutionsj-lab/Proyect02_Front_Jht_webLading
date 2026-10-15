from django.views.generic import TemplateView
from .models import Pagina, Servicio, FlotaVehiculo, ConfiguracionGlobal

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
    """Landing page dinámica gestionada por Page Builder."""
    template_name = 'public/landing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # 1. Configuración global (Singleton)
        context['config'] = ConfiguracionGlobal.objects.first()
        
        # 2. Catálogos Core independientes
        context['servicios'] = Servicio.objects.filter(activo=True)
        context['vehiculos'] = FlotaVehiculo.objects.filter(activo=True)
        
        # 3. Page Builder (Página Landing y sus Bloques Dinámicos)
        try:
            # prefetch_related('bloques__items') minimiza consultas a la BD (evita el problema N+1)
            pagina = Pagina.objects.prefetch_related('bloques__items').get(slug='landing', activa=True)
            context['pagina'] = pagina
            
            # Diccionario de bloques para acceder fácil desde HTML: {{ bloques.HERO }}
            bloques_dict = {}
            for bloque in pagina.bloques.filter(activo=True):
                bloques_dict[bloque.tipo_bloque] = bloque
                
            context['bloques'] = bloques_dict
            
        except Pagina.DoesNotExist:
            context['pagina'] = None
            context['bloques'] = {}

        return context
