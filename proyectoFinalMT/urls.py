from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Aplicaciones.Usuarios.urls')),
    path('estadios/', include('Aplicaciones.Estadios.urls')),
    path('arbitros/', include('Aplicaciones.Arbitros.urls')),
    path('temporadas/', include('Aplicaciones.Temporadas.urls')),
    path('jugadores/', include('Aplicaciones.Jugadores.urls')),
    path('equipos/', include('Aplicaciones.Equipos.urls')),

]

handler403 = 'proyectoFinalMT.views.error_403_view'
