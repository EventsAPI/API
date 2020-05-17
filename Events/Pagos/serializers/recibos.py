from rest_framework import serializers
#Modelos
from ..models.recibos import Recibos
from ..models.pagos import Pagos
#Serializador
from .pagos import PagosSerializer

class RecibosSerializer(serializers.ModelSerializer):
    pagos = PagosSerializer(many = True)
    
    class Meta:
        model = Recibos #el modelo a serializar
        fields = [
            'id',
            'estado',
            'pagos'
        ]
    
    def create(self, validated_data):
        pagos_data = validated_data.pop('pagos')
        recibo = Recibos.objects.create(**validated_data)
        for pago_data in pagos_data:
            Pagos.objects.create(recibo=recibo, **pago_data)
        
        return recibo