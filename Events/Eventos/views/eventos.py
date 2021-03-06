# Para manejar las vistas, importamos las que nos otorga Rest Framework, el modelo, y el/los serializador(es) necesario(s)

#Vistas genéricas
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, get_object_or_404
#Serializador
from ..serializers.eventos import EventosSerializer
#Modelos
from ..models.eventos import Eventos
from Usuarios.models.usuarios import Usuario
#Email
from django.core.mail import send_mail
from django.conf import settings
#Permisos
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class CrearEvento (CreateAPIView):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer
    permission_classes = [IsAdminUser]
    
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
    permission_classes = [IsAuthenticated]

class VerEvento (RetrieveAPIView):
    """ Para ver solamente un evento """
    serializer_class = EventosSerializer
    model = Eventos
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        query = Eventos.objects.all()
        identificacion = self.kwargs['pk']
        return query.filter(id=identificacion)
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj

class ListarDepartamento (ListAPIView):
    serializer_class = EventosSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """ En esta vista se retorna solamente la búsqueda por departamentos """
        lugar = self.kwargs['lugar']
        return Eventos.objects.filter(lugar=lugar)

class BorrarEvento (DestroyAPIView):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer
    permission_classes = [IsAdminUser]

class ActualizarEvento (UpdateAPIView):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer
    permission_classes = [IsAdminUser]
