from rest_framework import serializers
from ..models.pagos import Pagos
from ..models.recibos import Recibos
#Serializadores extra
from .recibos import RecibosSerializer

class PagosSerializer (serializers.ModelSerializer):
    #usuario = serializers.HiddenField(default = serializers.CurrentUserDefault()) #Valor por parte de RestFramework para conocer al usuario actualmente logueado
    recibos = RecibosSerializer(many=True)
    
    class Meta:
        model = Pagos
        fields = [
            'tipoPago',
            'estado',
            'total',
            #'usuario',
            'recibos',
        ]
    
    def create(self, validated_data):
        recibos_data = validated_data.pop('recibos')
        pago = Pagos.objects.create(**validated_data)
        for recibo_data in recibos_data:
            Recibos.objects.create(idPago=pago, **recibo_data)
        
        return pago