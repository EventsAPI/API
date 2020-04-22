from django.contrib import admin

# Registrando los modelos
from .models.comentarios import Comentarios
from .models.eventos import Eventos
from .models.localidades import Asientos, Localidad
from .models.valoraciones import Valoraciones

@admin.register (Comentarios)
class Comentarios (admin.ModelAdmin):
    list_display = ('idUsuario', 'comentario', 'fecha',)
    list_filter = ('fecha', 'idUsuario',)

@admin.register (Eventos)
class Eventos (admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'lugar', 'estado', 'organizadores')
    list_filter = ('lugar', 'fecha', 'estado', 'organizadores',)

@admin.register (Asientos)
class Asientos (admin.ModelAdmin):
    list_display = ('estado',)

@admin.register (Localidad)
class Localidad (admin.ModelAdmin):
    list_display = ('tipo', 'costo',)

@admin.register (Valoraciones)
class Valoraciones (admin.ModelAdmin):
    list_display = ('valoracion', 'idUsuario',)
