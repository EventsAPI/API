from rest_framework import serializers
from Events.Eventos.models.valoraciones import Valoraciones

class ValoracionesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Valoraciones
        fields = '__all__'