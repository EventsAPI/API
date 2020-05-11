from rest_framework import serializers
from .models import Reservacion


class ReservacionSerializer(serializers.ModelSerializer):
Reservas = ReservacionSerializer(many=True)

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
        instance.estado = validated_data.get('estado', instance.estado)
        instance.Usuario = validated_data.get('nombre', instance.name) 
        instance.Localidad = validated_data.get('tipo', instance.tipo)
    return instance
