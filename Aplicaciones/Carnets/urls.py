
from django.urls import path
from . import views

app_name = 'carnets'  # Para usar namespace

urlpatterns = [
    # Ruta para mostrar la página con la lista de jugadores y carnets
    path('jugcarnet/', views.jugcarnet, name='jugcarnet'),

    # Ruta para generar el carnet de un jugador (POST)
    path('generar_carnet/<int:jugador_id>/', views.generar_carnet, name='generar_carnet'),

    # Puedes agregar más rutas aquí según funcionalidad
]
