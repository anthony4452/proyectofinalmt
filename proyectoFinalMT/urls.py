
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Aplicaciones.Usuarios.urls')),
    path('estadios/', include('Aplicaciones.Estadios.urls')),
    path('arbitros/', include('Aplicaciones.Arbitros.urls')),
    path('temporadas/', include('Aplicaciones.Temporadas.urls')),
]
