import email
from django import forms

class Administrador(forms.Form):
    cod_administrador = forms.IntegerField(primary_key=True)
    email = forms.CharField(max_length=255, null=False)
    Contraseña = forms.CharField(max_length=255, null=False)

class Usuario(forms.Form):
     cedula = forms.IntegerField(primary_key=True)
     nombre = forms.CharField(max_length=255, null=False)
     Contraseña = forms.CharField(max_length=255, null=False)
     apellido = forms.CharField(max_length=255, null=False)
     email = forms.CharField(max_length=255, null=False)