#Serializador
from .serializers import UserSerializer
#Modelo
from .models import Usuario
#Respuesta de Servidor
from rest_framework.response import Response
#Autenticación
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import authenticate
#Vistas empleadas
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView

class UsuarioViewSet (viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()

class LoginView (APIView):
    permission_classes = []
    
    def post (self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username = username, password = password)
        
        if user:
            return Response(
                {'token': user.auth_token.key}
            )
        else:
            return Response(
                {'error': 'Credenciales inválidas. Inicie sesión.'},
                status= status.HTTP_400_BAD_REQUEST
            )