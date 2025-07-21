from django.db import models
from Aplicaciones.Carnets.models import Carnet

class Correos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    destinatario = models.EmailField()
    asunto = models.TextField(max_length=100)
    mensaje = models.TextField(max_length=1000)
    carnet = models.ForeignKey(Carnet, on_delete=models.CASCADE)  # Relacionado al carnet
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
