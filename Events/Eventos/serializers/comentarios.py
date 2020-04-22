from rest_framework import serializers
from ..models.comentarios import Comentarios

class ComentariosSerializer (serializers.ModelSerializer):
    idUsuario = serializers.HiddenField(default = serializers.CurrentUserDefault()) #Valor por parte de RestFramework para conocer al usuario actualmente logueado
    
    class Meta:
        model = Comentarios
        fields = [
            'fecha',
            'comentario',
            'idUsuario'
        ]
        depth = 1