from django.db import models
from django.conf import settings

class OwnerModel (models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner_p', on_delete=models.SET_NULL, blank=True, null=True)
    
    class Meta:
        abstract = True

class Pagos (OwnerModel):
    DEPOSITO = 1
    CREDITO = 3
    DEBITO = 5
    
    TIPO = (
        (DEPOSITO, 'A través de depósito bancario'),
        (CREDITO, 'A través de tarjeta de crédito'),
        (DEBITO, 'A través de tarjeta de débito')
    )
    #Tipos de pago (pueden agregarse más)
    
    PAGADO = 1
    PENDIENTE = 3
    CANCELADO = 5
    
    ESTADO = (
        (PAGADO, 'Evento pagado.'),
        (PENDIENTE, 'Pendiente de pago'),
        (CANCELADO, 'Pago cancelado')
    )
    
    tipoPago = models.SmallIntegerField(choices=TIPO, default=CREDITO)
    estado = models.SmallIntegerField(choices=ESTADO, default=PENDIENTE)
    total = models.FloatField()
    recibo = models.ForeignKey('Pagos.Recibos', related_name='pagos', on_delete=models.CASCADE)
    #El primer 'Pagos' es sobre la app de django; el segundo, el nombre del modelo.
    evento = models.ForeignKey('Eventos.Eventos', on_delete=models.CASCADE)
    localidad = models.ForeignKey('Eventos.Localidad', on_delete=models.CASCADE)