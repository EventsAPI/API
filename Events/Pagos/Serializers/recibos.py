from rest_framework import serializers
from Eventos.models.recibos import Recibos

class RecibosSerializer (serializers.ModelSerializer):
    class Meta:
        model = Recibos
        fields = '__all__'