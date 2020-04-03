from rest_framework import serializers
from Eventos.models.valoraciones import Valoraciones
from .localidades import LocalidadSerializer

class ValoracionesSerializer (serializers.ModelSerializer):        
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer
    permission_classes = []
    idLocalidad = LocalidadSerializer ()

    class meta:
    model = valoraciones 
    fields= [
    'nombre',
    'evento',
    'fecha',
    'hora',
    'lugar',
    'precio',
    'idLocalidad',
    ]
     depth = 1