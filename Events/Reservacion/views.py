from .serializers import ReservasSerializer

from .models import Reservas

#ModelViewSet
from rest_framework import viewsets

class ReservacionViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer
    permission_classes = []

