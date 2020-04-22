from django.db import models

class Asientos (models.Model):
    LIBRE = 1
    OCUPADO = 3
    
    ESTADOS = (
        (LIBRE, 'Asiento libre'),
        (OCUPADO, 'Asiento ocupado')
    )
    
    estado = models.SmallIntegerField(choices=ESTADOS, default=LIBRE)

class Localidad (models.Model):
    GENERAL = 1
    Oro = 3
    PLATINO = 5
    
    TIPOS = (
        (GENERAL, 'Asiento General'),
        (Oro, 'Asiento en Oro'),
        (PLATINO, 'Asiento Platinum')
    )
    
    tipo = models.SmallIntegerField(choices=TIPOS, default=GENERAL)
    costo = models.FloatField()

    idAsiento = models.ForeignKey(Asientos, on_delete=models.CASCADE)
