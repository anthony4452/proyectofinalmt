from django.db import models

class Estadio(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    capacidad = models.PositiveIntegerField()
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
