from django.db import models
from Aplicaciones.Jugadores.models import Jugador

class Carnet(models.Model):
    jugador = models.OneToOneField(Jugador, on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_carnets/')
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carnet de {self.jugador.nombres}"
