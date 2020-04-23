from rest_framework import serializers
from ..models.valoraciones import Valoraciones

class ValoracionesSerializer (serializers.ModelSerializer):
    usuario = serializers.HiddenField(default = serializers.CurrentUserDefault()) #Toma el valor del usuario logueado actualmente
    
    class Meta:
        model = Valoraciones
        fields = [
            'valoracion',
            'evento',
            'usuario'
        ]
        depth = 1