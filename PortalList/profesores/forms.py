from django import forms
from django.forms import ModelForm
from administracion.models import Usuario


class IngresarProfesor(ModelForm):
    inputUsuarioIP=forms.CharField(label="inputUsuarioIP", max_length=255, required=True)
    inputContraseñaIP=forms.CharField(label="inputContraseñaIP", max_length=255, required=True)

    class Meta:
        model = Usuario
        fields=['usuario','contraseña']