from rest_framework import viewsets
#Modelo
from ..models.comentarios import Comentarios
#Serializador
from ..serializers.comentarios import ComentariosSerializer
#Permisos
from rest_framework.permissions import IsAuthenticated

class ComentariosViewSet (viewsets.ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super(ComentariosViewSet, self).get_serializer_context()
        return context