from rest_framework import serializers
from ..models.comentarios import Comentarios

class ComentariosSerializer (serializers.ModelSerializer):
    usuario = serializers.HiddenField(default = serializers.CurrentUserDefault()) #Valor por parte de RestFramework para conocer al usuario actualmente logueado
    
    class Meta:
        model = Comentarios
        fields = [
            'fecha',
            'usuario',
            'evento',
            'comentario',
        ]
        depth=1