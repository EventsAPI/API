from rest_framework import viewsets
#Modelo
from ..models.valoraciones import Valoraciones
#Serializador
from ..serializers.valoraciones import ValoracionesSerializer

class ValoracionesViewSet (viewsets.ModelViewSet):
    queryset = Valoraciones.objects.all()
    serializer_class = ValoracionesSerializer
    permission_classes = []
    
    def perform_create(self, serializer):
        serializer.save()