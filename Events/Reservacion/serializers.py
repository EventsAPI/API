from rest_framework import serializers
from .models import Reservas


class ReservacionSerializer(serializers.ModelSerializer):

class Meta: 
    model = Reservas
    fieds = '__all__'
    
    def create(self, validated_data):
        """
        Cree y devuelva una nueva instancia de `Reservas`, dados los datos validados.
        """
    return Reservas.objects.create(**validated_data)

    def update(self, instance, validated_data):
    
        """
            Actualice y devuelva una instancia `Reservas` existente, dados los datos validados.
        """
        
        instance.nombre = validated_data.get('nombre', instance.name)
        instance.fecha = validated_data.get('Fecha', instance.fecha) 
        instance.lugar = validated_data.get('lugar', instance.lugar)
        instance.estado = validated_data.get('estado', instance.estado)
    return instance