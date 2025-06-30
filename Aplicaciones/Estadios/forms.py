# filepath: /home/ilyanthoo/trabajosAM1/proyectoFinalMT/Aplicaciones/Estadios/forms.py
from django import forms
from .models import Estadio

class EstadioForm(forms.ModelForm):
    class Meta:
        model = Estadio
        fields = ['nombre', 'direccion', 'capacidad', 'ciudad']