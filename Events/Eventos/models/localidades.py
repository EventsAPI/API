from django.db import models

class Localidad (models.Model):
    GENERAL = 1
    ORO = 3
    PLATINO = 5
    
    TIPOS = (
        (GENERAL, 'Asiento General'),
        (ORO, 'Asiento Oro'),
        (PLATINO, 'Asiento Platinum')
    )
    
    tipo = models.SmallIntegerField(choices=TIPOS, default=GENERAL)
    costo = models.FloatField()
    
    evento = models.ForeignKey('Eventos.Eventos', related_name='eventosLocal', null=True, blank=True, on_delete=models.CASCADE)

class Asientos (models.Model):
    LIBRE = 1
    OCUPADO = 3
    
    ESTADOS = (
        (LIBRE, 'Asiento libre'),
        (OCUPADO, 'Asiento ocupado')
    )
    
    estado = models.SmallIntegerField(choices=ESTADOS, default=LIBRE)
    localidad = models.ForeignKey(Localidad, related_name='asientos', null=True, blank=True, on_delete=models.CASCADE)