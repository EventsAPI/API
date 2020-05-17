from rest_framework import serializers
#Modelos
from ..models.pagos import Pagos

class PagosSerializer (serializers.ModelSerializer):
    owner_p = serializers.StringRelatedField(default = serializers.CurrentUserDefault()) #Valor por parte de RestFramework para conocer al owner_p (usuario) actualmente logueado
    class Meta:
        model = Pagos
        fields = [
            'id',
            'tipoPago',
            'estado',
            'total',
            'owner_p',
            'evento',
            'localidad',
        ]
        read_only_fields = ['owner_p']