from rest_framework import serializers
from .models import Reservacion


class ReservacionSerializer(serializers.ModelSerializer):
Reservas = ReservacionSerializer(many=True)

class Meta: 
    model = Reservas
    fields = [
            'estado',
            'idUsuario',
            'idLocalidad'
        ]
    depth=1