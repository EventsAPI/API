from rest_framework import serializers
from Eventos.models.eventos import Eventos
from .valoraciones import ValoracionesSerializer
from .comentarios import ComentariosSerializer
from .localidades import LocalidadSerializer
#Estas importaciones traen los serializadores descritos en los otros ficheros python en la carpeta Serializers
#Los importamos debido a que es necesario serializar su información en este serializador EventosSerializer

class EventosSerializer(serializers.ModelSerializer):
    valoraciones = ValoracionesSerializer (many = True , read_only = True)
    localidades = LocalidadSerializer (many = True , read_only = True)
    comentarios = ComentariosSerializer (many = True , read_only = True)
    
    class Meta:
        model = Eventos #el modelo a serializar
        fields = (
            'afiche',
            'nombre',
            'fecha',
            'hora',
            'lugar',
            'localidades',
            'estado',
            'organizadores',
            'valoraciones',
            'comentarios'
        ) 
        #todos los campos + los campos creados en el serializador para mostrar valoraciones,
        #localidades y comentarios
        depth = 1
        #la profundidad para indagar en las foráneas