import email
from django import forms

class RegistroAlumno(forms.Form):
    nombre = forms.CharField(max_length=255, null=False)
    apellido = forms.CharField(max_length=255, null=False)
    cedula = forms.NumberInput(null=False)
    numeroPadre = forms.NumberInput(null=False)
    email = forms.CharField(max_length=255, null=False)
    Contraseña = forms.CharField(max_length=255, null=False)
