from django.db import models

class Asientos (models.Model):
    LIBRE = 1
    OCUPADO = 3
    
    ESTADOS = (
        (LIBRE, 'Asiento libre'),
        (OCUPADO, 'Asiento ocupado')
    )
    
    estado = models.SmallIntegerField(choices=ESTADOS, default=LIBRE)

class TipoLocal (models.Model):
    GENERAL = 1
    PALCA = 3
    PLATINO = 5
    
    TIPOS = (
        (GENERAL, 'Asiento General'),
        (PALCA, 'Asiento en Palcos'),
        (PLATINO, 'Asiento Platinum')
    )
    
    tipo = models.SmallIntegerField(choices=TIPOS, default=GENERAL)
    costo = models.FloatField()

class Localidad (models.Model):
    asientos_totales = models.IntegerField()
    idAsiento = models.ForeignKey(Asientos,on_delete=models.CASCADE)
    idTipoLocal = models.ForeignKey(TipoLocal, on_delete=models.CASCADE)