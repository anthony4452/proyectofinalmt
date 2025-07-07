from django import forms
from .models import Arbitro

class ArbitroForm(forms.ModelForm):
    class Meta:
        model = Arbitro
        fields = ['nombre', 'cedula', 'nacionalidad', 'edad', 'experiencia']
