from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Reservacion.urls')),
] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
