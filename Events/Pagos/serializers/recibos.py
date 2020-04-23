from rest_framework import serializers
#Modelo
from ..models.recibos import Recibos

class RecibosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recibos #el modelo a serializar
        fields = [
            'id',
            'estado',
        ]