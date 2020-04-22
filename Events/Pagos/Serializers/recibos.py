from rest_framework import serializers
from Eventos.models.pagos import Recibos
from .pagos import PagosSerializer


class RecibosSerializer(serializers.ModelSerializer):
    idPago = PagosSerializer(many = True , read_only = True)
  
    class Meta:
        model = Recibos #el modelo a serializar
        fields = [
            'estado',
            'idPago',
        ]

        depth = 1