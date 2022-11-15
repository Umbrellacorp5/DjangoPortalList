from django import forms
from administracion.models import Administrador
from administracion.models import Usuario
from django.forms import ModelForm

class IngresarAdminsitracion(ModelForm):
    email=forms.CharField(label="Nombre", max_length=255, required=True)
    contraseña=forms.CharField(label="Contraseña", max_length=255, required=True)

    class Meta:
        model = Administrador
        fields=['email','contraseña']
        

class RegistroAlumno(ModelForm):
    nombre= forms.CharField(label="Nombre", max_length=255, required=True)
    apellido= forms.CharField(label="Apellido", max_length=255, required=True)
    cedula= forms.CharField(label="cedula", max_length=255, required=True)
    email= forms.CharField(label="email", max_length=255, required=True)
    usuario= forms.CharField(label="usuario", max_length=255, required=True)
    contraseña= forms.CharField(label="contraseña", max_length=255, required=True)

    class Meta:
        model = Usuario
        fields = ['nombre','apellido','cedula','email','usuario','contraseña']
