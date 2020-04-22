from django.shortcuts import render

# Create your views here.
from .serializers.pagos import PagosSerializer
from .serializers.Recibos import RecibosSerializer
#Modelo
from Eventos.models.pagos import Pagos
from Eventos.models.recibos import Recibos
#ModelViewSet
from rest_framework import viewsets
from rest_framework import ListCreateviewsets


class PagosViewSet(viewsets.ModelViewSet):
    queryset = Pagos.objects.all()
    serializer_class = PagosSerializer
    permissions_classes = []

class RecibosListCreateViewSet(ListCreateviewsets.ModelViewSet):
    queryset = Recibos.objects.all()
    serializer_class = RecibosSerializer
    permissions_classes = []
