from django import forms
from .models import Comentario


class ComentarioForm(forms.ModelForm):
    """
    Formulario para que los lectores envíen comentarios desde el frontend.
    Los comentarios se guardan con aprobado=False por defecto (requieren moderación).
    """
    class Meta:
        model = Comentario
        fields = ['nombre_autor', 'email_autor', 'contenido']
        labels = {
            'nombre_autor': 'Nombre',
            'email_autor':  'Correo electrónico',
            'contenido':    'Añadir comentario',
        }
        widgets = {
            'nombre_autor': forms.TextInput(attrs={
                'class':       'w-full bg-white border border-blue-300 p-3 text-gray-800 '
                               'focus:outline-none focus:border-blue-600 focus:ring-1 '
                               'focus:ring-blue-600 transition-colors rounded-md',
                'placeholder': 'Tu nombre completo',
                'required':    True,
            }),
            'email_autor': forms.EmailInput(attrs={
                'class':       'w-full bg-white border border-blue-300 p-3 text-gray-800 '
                               'focus:outline-none focus:border-blue-600 focus:ring-1 '
                               'focus:ring-blue-600 transition-colors rounded-md',
                'placeholder': 'tucorreo@empresa.com',
                'required':    True,
            }),
            'contenido': forms.Textarea(attrs={
                'class':       'w-full bg-white border border-blue-300 p-3 text-gray-800 '
                               'focus:outline-none focus:border-blue-600 focus:ring-1 '
                               'focus:ring-blue-600 resize-y transition-colors rounded-md',
                'rows':        6,
                'placeholder': 'Escribe tu comentario aquí...',
                'required':    True,
            }),
        }
