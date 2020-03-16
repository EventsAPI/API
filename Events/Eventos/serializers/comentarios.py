from rest_framework import serializers
from Eventos.models.comentarios import Comentarios

class ComentariosSerializer (serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = '__all__'