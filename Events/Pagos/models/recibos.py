from django.db import models

class Recibos (models.Model):
    PAGADO = 1
    DEVUELTO = 3
    CANCELADO = 5
    
    ESTADO = (
        (PAGADO, 'Recibo pagado'),
        (DEVUELTO, 'Recibo con devolución'),
        (CANCELADO, 'Recibo cancelado, dinero devuelto')
    )
    #Posibles estados del recibo
    
    estado = models.SmallIntegerField(choices=ESTADO, default=PAGADO)
    
    idPago = models.ForeignKey('Pagos.Pagos', related_name='recibos' ,on_delete=models.CASCADE)
    #El primer 'Pagos' es sobre la app de django; el segundo, el nombre del modelo.