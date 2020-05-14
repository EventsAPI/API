from rest_framework import serializers
#Modelos
from ..models.eventos import Eventos
from ..models.localidades import Localidad
#Serializadores
# from .valoraciones import ValoracionesSerializer
# from .comentarios import ComentariosSerializer
#from .localidades import LocalidadSerializer
#Estas importaciones traen los serializadores descritos en los otros ficheros python en la carpeta Serializers
#Los importamos debido a que es necesario serializar su información en este serializador EventosSerializer

class EventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos #el modelo a serializar
        fields = (
            'id',
            'afiche',
            'nombre',
            'fecha',
            'hora',
            'lugar',
            'estado',
            'organizadores',
            'localidad', #antes era eventosLocal
            'valoracion',
            'comentario'
        )
        depth = 1
    
    # def create(self, validated_data):
    #     localidades_data = validated_data.pop('eventosLocal')
    #     evento = Eventos.objects.create(**validated_data)
    #     for localidad_data in localidades_data:
    #         Localidad.objects.create(evento=evento, **localidad_data)
        
    #     return evento