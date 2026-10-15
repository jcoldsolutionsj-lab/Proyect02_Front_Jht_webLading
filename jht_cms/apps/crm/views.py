from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactoSolicitudSerializer
from rest_framework.permissions import AllowAny

class ContactoSolicitudAPIView(APIView):
    authentication_classes = [] # Deshabilita CSRF para endpoint público
    permission_classes = [AllowAny]
    """
    API View para recibir solicitudes desde los formularios de la Landing Page
    (Cotización y Consulta General).
    """

    def post(self, request, *args, **kwargs):
        # Pasar los datos recibidos al serializador (nuestro DTO)
        serializer = ContactoSolicitudSerializer(data=request.data)
        
        # Validar los datos estrictamente
        if serializer.is_valid():
            # El método save() llama a create() dentro del serializador
            serializer.save()
            
            return Response({
                "status": "success",
                "message": "Solicitud registrada correctamente."
            }, status=status.HTTP_201_CREATED)
        else:
            # Si hay errores, devolvemos un 400 Bad Request con el diccionario exacto de qué falló
            return Response({
                "status": "error",
                "message": "Hubo errores de validación.",
                "errores": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
