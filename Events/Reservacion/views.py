from django.shortcuts import render
from .Serializers import Reservacion
from rest_framework import viewsets 
from .models import Reservacion

class ReservacionView (ModelAPIView):
    queryset = Reservacion.objects.all()
    serializer_class = ReservarSerializer
    permission_classes = []