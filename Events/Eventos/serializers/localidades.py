from rest_framework import serializers
from ..models.localidades import Localidad, Asientos

class AsientosSerializer (serializers.ModelSerializer):
    class Meta:
        model = Asientos
        fields = ['id', 'estado']


class LocalidadSerializer (serializers.ModelSerializer):
    asientos = AsientosSerializer (many=True)
    
    class Meta:
        model = Localidad
        fields = [
            'id',
            'tipo',
            'costo',
            'asientos'
        ]
    
    def create(self, validated_data):
        asientos_data = validated_data.pop ('asientos')
        localidad = Localidad.objects.create(**validated_data)
        for asiento_data in asientos_data:
            Asientos.objects.create(localidad=localidad, **asiento_data)
        
        return localidad