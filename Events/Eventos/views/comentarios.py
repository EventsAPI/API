from rest_framework import viewsets
#Modelo
from ..models.comentarios import Comentarios
#Serializador
from ..serializers.comentarios import ComentariosSerializer

class ComentariosViewSet (viewsets.ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer
    permission_classes = []
    
    def perform_create(self, serializer):
        serializer.save()