from django.db import models

class Reservacion (models.Model):


    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=255)
    organizadores = models.CharField(max_length=150)
    
 
    class Meta: 
        ordering = ['nombre']
      
    #El primer 'Eventos' es sobre la app Django; el segundo, sobre el modelo Eventos.
