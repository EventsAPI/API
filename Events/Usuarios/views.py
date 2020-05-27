#Serializador
from .serializers import UserSerializer, ProfileSerializer
#Modelo
from .models import Usuario, Perfil
#Respuesta de Servidor
from rest_framework.response import Response
#Autenticación
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import authenticate
#Vistas empleadas
from rest_framework import viewsets
#Genéricas
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, get_object_or_404, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import status
from rest_framework.views import APIView
#Permisos
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class CrearUsuario (CreateAPIView):
    queryset = Usuario.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    model = Usuario
    permission_classes = []

class ListarUsuarios (ListAPIView):
    queryset = Usuario.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    model = Usuario
    permission_classes = [IsAuthenticated]

class ActualizarUsuario (UpdateAPIView):
    queryset = Usuario.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    model = Usuario
    permission_classes = [IsAdminUser]

class EliminarUsuario (DestroyAPIView):
    queryset = Usuario.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    model = Usuario
    permission_classes = [IsAdminUser]

class VerUsuario (RetrieveAPIView):
    serializer_class = UserSerializer
    model = Usuario
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        query = Usuario.objects.all()
        identificacion = self.kwargs['pk']
        return query.filter(id=identificacion)
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj

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

class VerPerfiles (ListAPIView):
    queryset = Perfil.objects.all()
    serializer_class = ProfileSerializer
    model = Perfil
    permission_classes = [IsAuthenticated]

class VerActualizarPerfil (RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    
    def get_serializer_context(self):
        context = super(VerActualizarPerfil, self).get_serializer_context()
        return context

    def get_queryset(self):
        qs = Perfil.objects.all()
        logged_in_user_profile = qs.filter(usuario=self.request.user)
        return logged_in_user_profile
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, usuario=self.request.user)
        return obj

class VerPerfil (RetrieveAPIView):
    serializer_class = ProfileSerializer
    model = Perfil
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        query = Perfil.objects.all()
        identificacion = self.kwargs['pk']
        return query.filter(id=identificacion)
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj