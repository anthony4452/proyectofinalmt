from django.db import models
from Aplicaciones.Temporadas.models import Temporada

# Create your models here.
class Fecha(models.Model):
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)
    numero = models.PositiveIntegerField()
    fecha_programada = models.DateField()

    class Meta:
        unique_together = ('temporada', 'numero')
        ordering = ['numero']

    def __str__(self):
        return f"Fecha {self.numero} - {self.temporada}"