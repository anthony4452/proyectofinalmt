from django.urls import path
from . import views

urlpatterns = [
    path('', views.estadio, name='estadios'),  # /estadios/
    path('estadio', views.estadio),
    path('nuevoEstadio', views.nuevoEstadio),
    path('eliminarEstadio/<id>/', views.eliminarEstadio),
    path('editarEstadio/<id>/', views.editarEstadio),


]