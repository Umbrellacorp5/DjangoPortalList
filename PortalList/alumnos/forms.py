from django import forms
from django.forms import ModelForm
from administracion.models import Usuario

class IngresarAlumno(ModelForm):
    inputUsuarioIA=forms.CharField(label="inputUsuarioIA", max_length=255, required=True)
    inputContraseñaIA=forms.CharField(label="inputContraseñaIA", max_length=255, required=True)

    class Meta:
        model = Usuario
        fields=['usuario','contraseña']

