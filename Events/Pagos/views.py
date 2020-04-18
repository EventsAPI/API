from django.shortcuts import render

# Create your views here.
from .serializers.pagos import PagosSerializer
#Modelo
from Eventos.models.pagos import Pagos
#ModelViewSet
from rest_framework import viewsets


class PagosViewSet(viewsets.ModelViewSet):
    queryset = Pagos.objects.all()
    serializer_class = PagosSerializer
    permissions_classes = []

