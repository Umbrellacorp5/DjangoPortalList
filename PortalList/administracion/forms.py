import email
from django import forms

class RegistroAlumno(forms.Form):
    nombre = forms.CharField(max_length=255, null=False)
    apellido = forms.CharField(max_length=255, null=False)
    cedula = forms.NumberInput(null=False)
    numeroPadre = forms.NumberInput(null=False)
    email = forms.CharField(max_length=255, null=False)
    Contraseña = forms.CharField(max_length=255, null=False)
    fotoAlumno = forms.ImageField(null=False)
    emailRegistroAlumno = forms.EmailFiel(null=False)
    usuarioRegistroAlumno = forms.CharField(max_length=255, null=False)
    contraRegistroAlumno = forms.PasswordInput(max_length=255, null=False)