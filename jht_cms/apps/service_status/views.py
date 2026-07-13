from django.views.generic import TemplateView


class ConsultaView(TemplateView):
    """Consulta pública de seguimiento de envío."""
    template_name = 'service_status/consulta.html'


class ResultadoView(TemplateView):
    """Resultado del seguimiento."""
    template_name = 'service_status/resultado.html'
