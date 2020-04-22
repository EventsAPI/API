from rest_framework import viewsets
#modelo
from ..models.localidades import Localidad
#serializador
from ..serializers.localidades import LocalidadSerializer

class LocalidadViewSet (viewsets.ModelViewSet):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer
    permission_classes = []