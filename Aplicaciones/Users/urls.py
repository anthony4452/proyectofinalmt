# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.usuarios_list, name='usuarios_list'),
    path('crear/', views.usuarios_create, name='usuarios_create'),
    path('editar/<int:id>/', views.usuarios_edit, name='usuarios_edit'),
    path('eliminar/<int:id>/', views.usuarios_delete, name='usuarios_delete'),
]
