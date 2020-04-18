from django.shortcuts import render

from Eventos.Reservacion.models import Eventos
# Create your views here.
class ReservarEvento (CreateAPIView):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer
    permission_classes = []