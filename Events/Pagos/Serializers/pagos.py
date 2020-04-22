from rest_framework import serializers
from Pagos.models.pagos import Pagos
from .usuarios import UsuariosSerializer
from .eventos import EventosSerializer
from .localidades import LocalidadSerializer

class PagosSerializer(serializers.ModelSerializer):
    idUsuario = UsuariosSerializer(many = True , read_only = True)
    idEvento = EventosSerializer (many = True , read_only = True)
    idLocalidades = LocalidadSerializer (many = True , read_only = True)

    class Meta:
        model = Pagos #el modelo a serializar
        fields = [
            'tipoPago',
            'estado',
            'total',
            'idUsuario',
            'idEvento',
            'idLocalidad',
        ]

        depth = 1