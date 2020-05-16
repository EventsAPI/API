from rest_framework import serializers
from ..models.comentarios import Comentarios

class ComentariosSerializer (serializers.ModelSerializer):
    owner = serializers.StringRelatedField(default = serializers.CurrentUserDefault(), read_only=True) #Valor por parte de RestFramework para conocer al usuario actualmente logueado
    
    class Meta:
        model = Comentarios
        fields = ['fecha', 'comentario', 'owner']
        read_only_fields = ['fecha']