# Para manejar las vistas, importamos las que nos otorga Rest Framework, el modelo, y el/los serializador(es) necesario(s)

#Vistas genéricas
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
#Serializador
from ..serializers.eventos import EventosSerializer
#Modelos
from ..models.eventos import Eventos
from Usuarios.models.usuarios import Usuario
#Email
from django.core.mail import send_mail
from django.conf import settings

class CrearEvento (CreateAPIView):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer
    permission_classes = []
    
    #Envío de Email al crear evento
    
    def create(self, request, *args, **kwargs):
        usuario = Usuario.objects.all()
        respuesta = super(CrearEvento, self).create(request, *args, **kwargs)
        
        subject = '¡Nuevos eventos acercándose!'
        message = 'Tenemos nuevos eventos a la espera. Cuando puedas, ingresa a nuestra página.'
        from_email = 'API Events <noreply {}>'.format(settings.EMAIL_HOST_USER)
        
        for usuarios in usuario:
            to_list = [usuarios.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            
        return respuesta

class ListarEvento (ListAPIView):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer
    model = Eventos
    permission_classes = []

class ListarDepartamento (ListAPIView):
    serializer_class = EventosSerializer
    permission_classes = []
    
    def get_queryset(self):
        """ En esta vista se retorna solamente la búsqueda por departamentos """
        lugar = self.kwargs['lugar']
        return Eventos.objects.filter(lugar=lugar)

class BorrarEvento (DestroyAPIView):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer
    permission_classes = []

class ActualizarEvento (UpdateAPIView):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer
    permission_classes = []
