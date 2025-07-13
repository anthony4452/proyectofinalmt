from django.urls import path
from . import views

urlpatterns = [
    path('', views.temporadas, name='temporadas'),            # /temporadas/
    path('nuevaTemporada', views.nuevaTemporada),  # /temporadas/nueva/
]
