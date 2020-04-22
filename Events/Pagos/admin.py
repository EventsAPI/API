from django.contrib import admin

# Registrando los modelos
from .models.pagos import Pagos
from .models.recibos import Recibos


@admin.register (Pagos)
class Pagos (admin.ModelAdmin):
    list_display = ('idUsuario', 'tipoPago', 'total',)
    list_filter = ('idEvento', 'idUsuario','idtipoPago', 'total')

@admin.register (Recibos)
class Recibos (admin.ModelAdmin):
    list_display = ('estado', 'idPago',)
    



# Register your models here.
