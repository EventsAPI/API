from rest_framework import viewsets
#modelo
from ..models.localidades import Localidad, Asientos
#serializador
from ..serializers.localidades import LocalidadSerializer, AsientosSerializer

class LocalidadViewSet (viewsets.ModelViewSet):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer
    permission_classes = []

class AsientosViewSet (viewsets.ModelViewSet):
    queryset = Asientos.objects.all()
    serializer_class = AsientosSerializer
    permission_classes = []