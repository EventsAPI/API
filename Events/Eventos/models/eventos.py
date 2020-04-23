from django.db import models

class Eventos (models.Model):
    ACTIVO = 1
    INACTIVO = 3
    
    ESTADO = (
        (ACTIVO, 'Evento activo'),
        (INACTIVO, 'Evento inactivo')
    )
    
    afiche = models.ImageField(
        'afiche del evento',
        upload_to='eventos/afiche/',
        blank=True,
        null=True
    )
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=255)
    estado = models.SmallIntegerField(choices=ESTADO, default=ACTIVO)
    organizadores = models.CharField(max_length=150)