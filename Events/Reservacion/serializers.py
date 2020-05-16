from rest_framework import serializers
from .models import Reservas


class ReservasSerializer(serializers.Serializer):

    class Meta:
        model = Reservas
        fields = [
            'idAsientos',
            'estado',
            'idUsuario',
            'idLocalidad'
        ]

    def create(self, validated_data):
          reserva_data = validated_data.pop('reserva')
          asiento = Reservas.objects.create(**reserva_data)
          estado = Reservas.objects.create(reserva=Reservacion, estado=validated_data.pop('estado'))

   
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.Asientos = request.data.get("Asientos")
        Asientos . estado (idAsientos = Asientos,  ** Asientos_data ) 
        estado = instance.Asientos
        instance.save()


        """
            Actualice y devuelva una instancia `Reservas` existente, dados los datos validados.
        """ 
        instance.estado = validated_data.get('estado', instance.estado)
        instance.idUsuario = validated_data.get('idUsuario', instance.idUsuairo) 
        instance.idLocalidad = validated_data.get('idLocalidad', instance.idLocalidad)
        instance.save()
       
        return instance