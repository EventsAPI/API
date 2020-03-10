from django.db import models
from utils.models import InicioModel

class Perfil (InicioModel):
    FEMENINO = 1
    MASCULINO = 2
    NODEF = 3
    #Constantes para los géneros definidos en 3 opciones
    
    GENERO = (
        (FEMENINO, 'Femenino'),
        (MASCULINO, 'Masculino'),
        (NODEF, 'Sin definir')
    ) #Definición de las constantes en texto para poder mostrar
    
    usuario = models.OneToOneField('Usuarios.Usuario', on_delete=models.CASCADE)
        #el primer 'Usuarios' referencia al nombre de la aplicación en el que se encuentra el modelo Usuario.
    
    foto = models.ImageField(
        'foto de perfil',
        upload_to = 'usuarios/fotos/',
        blank = True,
        null = True
    ) #Upload_to es adónde se irán a guardar los archivos de imágenes
    genero = models.SmallIntegerField(choices= GENERO, default= NODEF) #choices escoge
    biografia = models.TextField(max_length= 500, blank= True)
    eventos_valorados = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return str(self.usuario)
    