from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q

from .models import Articulo, Comentario, Categoria, Etiqueta
from .forms import ComentarioForm


class NoticiasListView(ListView):
    """
    Página principal de Noticias.
    - Muestra el artículo destacado (hero/featured).
    - Lista paginada del resto de artículos publicados.
    - Filtrado opcional por categoría o etiqueta vía query param ?categoria=slug o ?etiqueta=slug.
    """
    model = Articulo
    template_name = 'public/noticias.html'
    context_object_name = 'articulos'
    paginate_by = 9  # 9 artículos en grilla de 3 columnas

    def get_queryset(self):
        qs = Articulo.objects.filter(estado='publicado').select_related('categoria', 'autor')

        # Filtro por categoría
        categoria_slug = self.request.GET.get('categoria')
        if categoria_slug:
            qs = qs.filter(categoria__slug=categoria_slug)

        # Filtro por etiqueta
        etiqueta_slug = self.request.GET.get('etiqueta')
        if etiqueta_slug:
            qs = qs.filter(etiquetas__slug=etiqueta_slug)

        # Excluir el destacado de la lista general (se muestra aparte en el hero)
        destacado = self._get_destacado()
        if destacado:
            qs = qs.exclude(pk=destacado.pk)

        return qs

    def _get_destacado(self):
        """Retorna el artículo marcado como destacado, o el más reciente si no hay ninguno."""
        destacado = Articulo.objects.filter(
            estado='publicado', es_destacado=True
        ).select_related('categoria', 'autor').first()
        if not destacado:
            destacado = Articulo.objects.filter(
                estado='publicado'
            ).select_related('categoria', 'autor').first()
        return destacado

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articulo_destacado'] = self._get_destacado()
        context['categorias'] = Categoria.objects.all()
        context['categoria_activa'] = self.request.GET.get('categoria', '')
        return context


class NoticiaDetalleView(FormMixin, DetailView):
    """
    Página de detalle de un artículo individual.
    - Busca por slug.
    - Solo artículos publicados son accesibles públicamente.
    - Incrementa el contador de vistas (atómico).
    - Maneja el POST del formulario de comentarios.
    - Pasa los comentarios aprobados y artículos relacionados al contexto.
    """
    model = Articulo
    template_name = 'public/noticia_detalle.html'
    context_object_name = 'articulo'
    slug_url_kwarg = 'slug'
    form_class = ComentarioForm

    def get_queryset(self):
        return Articulo.objects.filter(estado='publicado').select_related('categoria', 'autor')

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        # Incrementar vistas de forma atómica (thread-safe)
        self.object.incrementar_vistas()
        return response

    def get_success_url(self):
        return reverse('website:noticia_detalle', kwargs={'slug': self.object.slug}) + '#comentarios'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        comentario = form.save(commit=False)
        comentario.articulo = self.object
        comentario.aprobado = False  # Siempre requiere moderación
        comentario.save()
        messages.success(
            self.request,
            '¡Gracias por tu comentario! Será publicado una vez revisado por nuestro equipo.'
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Comentarios aprobados del artículo actual
        context['comentarios'] = self.object.comentarios.filter(aprobado=True)
        context['total_comentarios'] = self.object.comentarios.filter(aprobado=True).count()

        # Formulario de comentario (puede venir con errores si hubo POST inválido)
        if 'form' not in context:
            context['form'] = self.get_form()

        # Artículos relacionados: misma categoría, excluyendo el actual (máx. 3)
        context['articulos_relacionados'] = Articulo.objects.filter(
            estado='publicado',
            categoria=self.object.categoria
        ).exclude(pk=self.object.pk).select_related('categoria')[:3]

        return context
