from django.db import models

class Arbitro(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    nacionalidad = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    experiencia = models.PositiveIntegerField(help_text="Años de experiencia")

    def __str__(self):
        return self.nombre
