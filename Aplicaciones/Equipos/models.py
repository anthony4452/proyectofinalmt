from django.db import models
from Aplicaciones.Temporadas.models import Temporada

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    logo = models.FileField(upload_to='logos/', null=True, blank=True)
    fundacion = models.DateField()
    presidente = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre

class ParticipacionEquipo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)
    fecha_registro = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('equipo', 'temporada')
