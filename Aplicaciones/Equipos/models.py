from django.db import models
from Aplicaciones.Temporadas.models import Temporada

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    logo = models.FileField(upload_to='logos/')
    fundacion = models.DateField()
    presidente = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre
