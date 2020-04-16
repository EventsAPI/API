from rest_framework import serializers
from .models import Reservas


class SerieSerializer(serializers.Serializer):

    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=255)
    estado = models.SmallIntegerField(choices=ESTADO, default=ACTIVO)
    organizadores = models.CharField(max_length=150)
    
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
        instance.fecha = validated_data.get('Fecha', fecha.name)
        instance.lugar = validated_data.get('lugar', instance.lugar)
        instance.estado = validated_data.get('estado', instance.estado)
    return instance