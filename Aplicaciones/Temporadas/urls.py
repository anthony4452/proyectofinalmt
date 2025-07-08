from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_temporadas, name='lista_temporadas'),            # /temporadas/
    path('nueva/', views.crear_temporada, name='crear_temporada'),         # /temporadas/nueva/
    path('editar/<int:pk>/', views.editar_temporada, name='editar_temporada'),  # /temporadas/editar/5/
    path('eliminar/<int:pk>/', views.eliminar_temporada, name='eliminar_temporada'),  # /temporadas/eliminar/5/
]
