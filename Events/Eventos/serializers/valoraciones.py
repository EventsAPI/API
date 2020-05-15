from rest_framework import serializers
from ..models.valoraciones import Valoraciones

class ValoracionesSerializer (serializers.ModelSerializer):
    owner_v = serializers.StringRelatedField(default = serializers.CurrentUserDefault()) #Toma el valor del usuario logueado actualmente
    
    class Meta:
        model = Valoraciones
        fields = ['owner_v', 'valoracion']