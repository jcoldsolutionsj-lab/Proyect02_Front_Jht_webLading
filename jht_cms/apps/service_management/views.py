from django.views.generic import TemplateView


class DashboardView(TemplateView):
    """Dashboard principal del panel de gestión."""
    template_name = 'service_management/dashboard.html'


class OrdenesListView(TemplateView):
    """Lista de órdenes de servicio."""
    template_name = 'service_management/ordenes.html'


class OrdenDetailView(TemplateView):
    """Detalle de una orden de servicio."""
    template_name = 'service_management/detalle_orden.html'


class ActualizarEstadoView(TemplateView):
    """Actualizar estado de una orden."""
    template_name = 'service_management/actualizar_estado.html'


class DocumentosView(TemplateView):
    """Gestión de documentos."""
    template_name = 'service_management/documentos.html'
