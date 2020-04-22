from rest_framework import serializers
from ..models.valoraciones import Valoraciones
#Serializador de Usuario
from Usuarios.serializers import UserSerializer

class ValoracionesSerializer (serializers.ModelSerializer):
    idUsuario = UserSerializer(many = True, read_only = True)
    
    class Meta:
        model = Valoraciones
        fields = [
            'valoracion',
            'idUsuario'
        ]
        depth = 1