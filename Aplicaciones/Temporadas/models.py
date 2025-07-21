from django.db import models
#from Aplicaciones.TablaPosiciones.models import TablaPosicion
#from Aplicaciones.Equipos.models import Equipo
#from Aplicaciones.Partidos.models import Partido

# Create your models here.
class Temporada(models.Model):
    nombreliga = models.CharField(max_length=100)
    nombretorneo = models.CharField(max_length=100)
    año = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    reglamento = models.FileField(upload_to='reglamentos/', null=True, blank=True)

    #def equipos(self):
        #return Equipo.objects.filter(temporada=self)

   # def partidos(self):
        #return Partido.objects.filter(temporada=self)

    #def tabla_posiciones(self):
        #return TablaPosicion.objects.filter(temporada=self)

    def __str__(self):
        return self.nombretorneo
