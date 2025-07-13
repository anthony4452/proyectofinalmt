from django.db import models
from Aplicaciones.Jugadores.models import Jugador
from Aplicaciones.Equipos.models import Equipo
from Aplicaciones.Temporadas.models import Temporada

class Traspaso(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    desde_equipo = models.ForeignKey(Equipo, related_name='salidas', on_delete=models.SET_NULL, null=True)
    hacia_equipo = models.ForeignKey(Equipo, related_name='entradas', on_delete=models.SET_NULL, null=True)
    temporada_origen = models.ForeignKey(Temporada, on_delete=models.CASCADE)
    fecha_traspaso = models.DateField()

    def __str__(self):
        return f"{self.jugador} - {self.desde_equipo} → {self.hacia_equipo}"
