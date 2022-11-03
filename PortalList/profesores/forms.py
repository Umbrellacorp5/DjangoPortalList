from django import forms
from django.forms import ModelForm
from administracion.models import Usuario, Grupo


class IngresarProfesor(ModelForm):
    inputUsuarioIP=forms.CharField(label="inputUsuarioIP", max_length=255, required=True)
    inputContraseñaIP=forms.CharField(label="inputContraseñaIP", max_length=255, required=True)

    class Meta:
        model = Usuario
        fields=['usuario','contraseña']

class Grupo(ModelForm):
    codGrupo=forms.IntegerField(label="inputUsuarioIP")
    Nombre=forms.CharField(label="inputContraseñaIP")
    Alumnos=forms.IntegerField(label="inputContraseñaIP")

    class Meta:
        model = Grupo
        fields=['codGrupo','Nombre','Alumnos']