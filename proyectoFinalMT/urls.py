from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Aplicaciones.Usuarios.urls')),
    path('estadios/', include('Aplicaciones.Estadios.urls')),
    path('arbitros/', include('Aplicaciones.Arbitros.urls')),
    path('temporadas/', include('Aplicaciones.Temporadas.urls')),
    path('jugadores/', include('Aplicaciones.Jugadores.urls')),
    path('equipos/', include('Aplicaciones.Equipos.urls')),

]

# Esta línea sirve para mostrar imágenes en desarrollo
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler403 = 'proyectoFinalMT.views.error_403_view'
