# Para manejar las vistas, importamos las que nos otorga Rest Framework, el modelo, y el/los serializador(es) necesario(s)

#Vistas genéricas
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
#Serializador
from ..serializers.eventos import EventosSerializer
#Modelo
from ..models.eventos import Eventos

class CrearEvento (CreateAPIView):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer
    permission_classes = []

class ListarEvento (ListAPIView):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer
    model = Eventos
    permission_classes = []

class ListarDepartamento (ListAPIView):
    serializer_class = EventosSerializer
    permission_classes = []
    
    def get_queryset(self):
        """ En esta vista se retorna solamente la búsqueda por departamentos """
        lugar = self.kwargs['lugar']
        return Eventos.objects.filter(lugar=lugar)

class BorrarEvento (DestroyAPIView):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer
    permission_classes = []

class ActualizarEvento (UpdateAPIView):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer
    permission_classes = []
