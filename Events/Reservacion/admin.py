from django.contrib import admin
from .models import Reservacion 
class AdminReservacion (admin.ModelAdmin):


    list_display=["nombre", "fecha", "lugar"]

class Meta: 
    model: Reservacion 


class Meta: 
    model: Reservacion 

admin.register(Reservacion, AdminReservacion)