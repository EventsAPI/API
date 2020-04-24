from django.db import models
from rest_framework import Serializer   

class Reservas (models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=255)
    estado = models.SmallIntegerField(choices=ESTADO, default=ACTIVO)
    organizadores = models.CharField(max_length=150)
    
    estado = models.SmallIntegerField(choices=ESTADO, default=LIBRE)
    idUsuario = models.ForeignKey('Usuarios.Usuario', on_delete=models.CASCADE)
    idLocalidad = models.ForeignKey('Eventos.Eventos', on_delete=models.CASCADE)
    
    class Meta: 
        ordering = ['nombre']
      
    #El primer 'Eventos' es sobre la app Django; el segundo, sobre el modelo Eventos.
