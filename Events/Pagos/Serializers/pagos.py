from rest_framework import serializers
from Eventos.models.pagos import Pagos
from .Usuarios import UsuariosSerializer
from .Eventos import EventosSerializer
from .localidades import LocalidadSerializer



class PagosSerializer(serializers.ModelSerializer):
    idusuario = ValoracionesSerializer ()
    idevento = LocalidadSerializer ()

    class Meta:
        model = Pagos #el modelo a serializar
        fields = [
            'tipo_pago',
            'estado',
            'total',
            'idusuario',
            'idevento',
        ]

          depth = 1