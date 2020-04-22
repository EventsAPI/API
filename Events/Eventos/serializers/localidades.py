from rest_framework import serializers
from ..models.localidades import Localidad, Asientos

class AsientosSerializer (serializers.ModelSerializer):
    class Meta:
        model = Asientos
        fields = '__all__'


class LocalidadSerializer (serializers.ModelSerializer):
    idAsiento = AsientosSerializer (many=True, read_only=True)
    
    class Meta:
        model = Localidad
        fields = [
            'tipo',
            'costo',
            'idAsiento'
        ]