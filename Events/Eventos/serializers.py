from rest_framework import serializers
from .models.eventos import Eventos

class EventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos #el modelo a serializar
        fields = '__all__' #todos los campos