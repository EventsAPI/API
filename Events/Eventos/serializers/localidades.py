from rest_framework import serializers
from ..models.localidades import Localidad, Asientos

class AsientosSerializer (serializers.ModelSerializer):
    class Meta:
        model = Asientos
        fields = '__all__'


class LocalidadSerializer (serializers.ModelSerializer):
    idAsiento = AsientosSerializer (many = True)
    
    class Meta:
        model = Localidad
        fields = '__all__'
        depth = 1
    
    def create(self, validated_data):
        asiento_validated_data = validated_data.pop('idAsiento')
        localidad = Localidad.objects.create(**validated_data)
        asiento_set_serializer = self.fields['idAsiento']
        
        for each in asiento_validated_data:
            each['idAsiento'] = localidad
        asientos = asiento_set_serializer.create(asiento_validated_data)
        
        return localidad