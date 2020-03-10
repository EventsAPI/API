from rest_framework import serializers
from Events.Eventos.models.localidades import Localidad, Asientos, TipoLocal

class AsientosSerializer (serializers.ModelSerializer):
    class Meta:
        model = Asientos
        fields = '__all__'

class TipoLocalSerializer (serializers.ModelSerializer):
    class Meta:
        model = TipoLocal
        fields = '__all__'

class LocalidadSerializer (serializers.ModelSerializer):
    asientos = AsientosSerializer (many = True , read_only = True)
    tipos = TipoLocalSerializer (many = True, read_only = True)
    
    class Meta:
        model = Localidad
        fields = (
            'asientos_totales',
            'asientos',
            'tipos'
        )
        depth = 1