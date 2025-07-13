from django.urls import path
from . import views

urlpatterns = [
    path('', views.temporadas, name='temporadas'),            # /temporadas/
    path('nuevaTemporada/', views.nuevaTemporada, name='nueva_temporada'),  # /temporadas/nuevaTemporada/
    path('guardarTemporada/', views.guardarTemporada, name='guardar_temporada'),
    path('editarTemporada/<int:id>/', views.editarTemporada, name='editar_temporada'),
    path('eliminarTemporada/<int:id>/', views.eliminarTemporada, name='eliminar_temporada'),
    path('guardarEdicionTemporada/<int:id>/', views.guardarEdicionTemporada, name='guardar_edicion_temporada'),

    path('ver_pdf/<int:id>/', views.ver_pdf, name='ver_pdf'),


]