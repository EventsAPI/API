from django.shortcuts import render
from .Serializers import Reservacion
from rest_framework import viewsets 
from .models import Reserva

class ReservacionViewSet(viewsets.ModelViewSet):
    queryset = Reservacion.objects.all()
    serializer_class = ReservacionSerializer
    permission_classes = []
