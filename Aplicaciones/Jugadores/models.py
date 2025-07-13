from django.db import models
from django.shortcuts import render, get_object_or_404

from Aplicaciones.Equipos.models import Equipo
from Aplicaciones.Temporadas.models import Temporada
from datetime import date


def detalle_equipo_temporada(request, equipo_id, temporada_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    temporada = get_object_or_404(Temporada, id=temporada_id)

    inscripciones = InscripcionJugador.objects.filter(equipo=equipo, temporada=temporada).select_related('jugador')
    total_jugadores = inscripciones.count()

    context = {
        'equipo': equipo,
        'temporada': temporada,
        'jugadores': inscripciones,
        'total_jugadores': total_jugadores
    }

    return render(request, 'jugadores/detalle_equipo_temporada.html', context)

class Jugador(models.Model):
    foto = models.FileField(upload_to='jugadores/', null=True, blank=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nacimiento = models.DateField()
    posicion = models.CharField(max_length=50)

    @property
    def edad(self):
        hoy = date.today()
        edad = hoy.year - self.nacimiento.year
        # Ajustar si el cumpleaños no ha ocurrido aún este año
        if (hoy.month, hoy.day) < (self.nacimiento.month, self.nacimiento.day):
            edad -= 1
        return edad

class InscripcionJugador(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)
    numero = models.PositiveIntegerField()  # dorsal del jugador en ese equipo
    fecha_inscripcion = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = [
            ('jugador', 'temporada'),       # Un jugador no se inscribe dos veces en una temporada
            ('equipo', 'temporada', 'numero')  # Un número solo se usa una vez por equipo en una temporada
        ]

    def __str__(self):
        return f"{self.jugador} - #{self.numero} - {self.equipo} ({self.temporada})"

    def historial_equipos(self):
        equipos = InscripcionJugador.objects.filter(jugador=self).values_list('equipo__nombre', 'temporada__nombre')
        return list(equipos)