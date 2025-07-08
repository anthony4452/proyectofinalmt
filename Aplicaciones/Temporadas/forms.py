from django import forms
from .models import Temporada

class TemporadaForm(forms.ModelForm):
    class Meta:
        model = Temporada
        fields = '__all__'
        widgets = {
            'nombreliga': forms.TextInput(attrs={'class': 'form-control'}),
            'nombretorneo': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }