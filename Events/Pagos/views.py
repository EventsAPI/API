from .serializers.pagos import PagosSerializer
from .serializers.recibos import RecibosSerializer
#Modelo
from .models.pagos import Pagos
from .models.recibos import Recibos
#ModelViewSet
from rest_framework import viewsets

class PagosViewSet(viewsets.ModelViewSet):
    queryset = Pagos.objects.all()
    serializer_class = PagosSerializer
    permission_classes = []
    
    def perform_create(self, serializer):
        serializer.save()

class RecibosViewSet(viewsets.ModelViewSet):
    queryset = Recibos.objects.all()
    serializer_class = RecibosSerializer
    permission_classes = []
    
    def perform_create(self, serializer):
        serializer.save()