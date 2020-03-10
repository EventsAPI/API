from django.db import models

class Pagos (models.Model):
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
    
    idUsuario = models.ForeignKey('Usuarios.Usuario', on_delete=models.CASCADE)
    idEvento = models.ForeignKey('Eventos.Eventos', on_delete=models.CASCADE)