from rest_framework import viewsets
#Modelo
from ..models.valoraciones import Valoraciones
#Serializador
from ..serializers.valoraciones import ValoracionesSerializer
#Permisos
from rest_framework.permissions import IsAuthenticated

class ValoracionesViewSet (viewsets.ModelViewSet):
    queryset = Valoraciones.objects.all()
    serializer_class = ValoracionesSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save()