from rest_framework import serializers
from .models import CrmContacto, CrmSolicitud
import re

class ContactoSolicitudSerializer(serializers.Serializer):
    # Campos de Contacto
    nombre = serializers.CharField(max_length=255, required=True, error_messages={
        'required': 'El nombre es obligatorio.',
        'blank': 'El nombre no puede estar vacío.'
    })
    apellido = serializers.CharField(max_length=255, required=False, allow_blank=True)
    correo = serializers.EmailField(required=True, error_messages={
        'required': 'El correo electrónico es obligatorio.',
        'invalid': 'Por favor, introduce una dirección de correo válida.'
    })
    telefono = serializers.CharField(max_length=20, required=True, error_messages={
        'required': 'El teléfono/celular es obligatorio.',
        'blank': 'El teléfono/celular no puede estar vacío.'
    })
    empresa = serializers.CharField(max_length=255, required=True, error_messages={
        'required': 'El nombre de la empresa es obligatorio.',
        'blank': 'El nombre de la empresa no puede estar vacío.'
    })

    # Campos de Solicitud
    origen = serializers.ChoiceField(choices=CrmSolicitud.ORIGEN_CHOICES, required=True, error_messages={
        'required': 'El origen de la solicitud es obligatorio.',
        'invalid_choice': 'El origen proporcionado no es válido.'
    })
    servicio_interes = serializers.ChoiceField(choices=CrmSolicitud.SERVICIO_CHOICES, required=False, allow_blank=True, allow_null=True)
    mensaje = serializers.CharField(required=False, allow_blank=True)

    def validate_telefono(self, value):
        # Validar que solo contenga números y espacios, y mínimo 6 dígitos
        cleaned_value = re.sub(r'[\s+]', '', value)
        if not cleaned_value.isdigit():
            raise serializers.ValidationError('El teléfono solo debe contener números.')
        if len(cleaned_value) < 6:
            raise serializers.ValidationError('El teléfono debe tener al menos 6 dígitos.')
        return value

    def create(self, validated_data):
        # Extraer datos
        correo = validated_data.get('correo')
        
        # 1. Buscar o crear el contacto
        contacto, created = CrmContacto.objects.update_or_create(
            correo=correo,
            defaults={
                'nombre': validated_data.get('nombre'),
                'apellido': validated_data.get('apellido'),
                'telefono': validated_data.get('telefono'),
                'empresa': validated_data.get('empresa'),
            }
        )

        # 2. Crear la solicitud asociada al contacto
        solicitud = CrmSolicitud.objects.create(
            contacto=contacto,
            origen=validated_data.get('origen'),
            servicio_interes=validated_data.get('servicio_interes'),
            mensaje=validated_data.get('mensaje'),
            estado_ventas='nuevo'
        )

        return solicitud
