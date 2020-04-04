# Para manejar las vistas, importamos las que nos otorga Rest Framework, el modelo, y el/los serializador(es) necesario(s)

#Serializador
from .serializers.eventos import EventosSerializer
#Modelo
from Eventos.models.eventos import Eventos
#ModelViewSet
from rest_framework import viewsets


class EventosViewSet(viewsets.ModelViewSet):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer
    permissions_classes = []






   
 