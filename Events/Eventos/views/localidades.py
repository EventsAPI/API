#Vistas genéricas
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework import viewsets
#modelo
from ..models.localidades import Localidad, Asientos
#serializador
from ..serializers.localidades import LocalidadSerializer, AsientosSerializer
#Permisos
from rest_framework.permissions import IsAdminUser, IsAuthenticated

#Vistas para Localidad
class CrearLocalidad (CreateAPIView):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer
    permission_classes = [IsAdminUser]

class ListarLocalidad (ListAPIView):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class MostrarLocalidad (RetrieveAPIView):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class BorrarLocalidad (DestroyAPIView):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer
    permission_classes = [IsAdminUser]

class ActualizarLocalidad (UpdateAPIView):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer
    permission_classes = [IsAdminUser]

#Vistas para Asientos
class AsientosViewSet (viewsets.ModelViewSet):
    queryset = Asientos.objects.all()
    serializer_class = AsientosSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]