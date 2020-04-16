from django.db import models

class Reservas (models.Model):
    LIBRE = 1
    RESERVADO = 2
    
    ESTADO = (
        (LIBRE, 'Asiento libre'),
        (RESERVADO, 'Asiento reservado')
    )
       
    afiche = models.ImageField
    (
        'afiche del evento',
        upload_to='eventos/afiche/',
        blank=True,
        null=True
    )
    estado = models.SmallIntegerField(choices=ESTADO, default=LIBRE)
    
   
    
    idUsuario = models.ForeignKey('Usuarios.Usuario', on_delete=models.CASCADE)
    idLocalidad = models.ForeignKey('Eventos.Eventos', on_delete=models.CASCADE)
    #El primer 'Eventos' es sobre la app Django; el segundo, sobre el modelo Eventos.
