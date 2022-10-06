import email
from django import forms

class RegistroAlumno(forms.Form):
    nombre = forms.CharField(max_length=255, null=False)
    apellido = forms.CharField(max_length=255, null=False)
    cedula = forms.NumberInput(null=False)
    numeroPadre = forms.NumberInput(null=False)
    Contraseña = forms.CharField(max_length=255, null=False)
    fotoAlumno = forms.ImageField(null=False)
    emailRegistroAlumno = forms.EmailField(null=False)
    usuarioRegistroAlumno = forms.CharField(max_length=255, null=False)
    contraRegistroAlumno = forms.CharField(widget = forms.PasswordInput())

class registroProfesor(forms.form):
    nombreProfesor = forms.CharField(max_length=255, null=False)
    apellidoProfesor =  forms.CharField(max_length=255, null=False)
    cedulaProfesor = forms.NumberInput(null=False)
    emailRegistroProfesor = forms.EmailField(null=False)
    usuarioRegistroProfesor = forms.NumberInput(null=False)
    contraRegistroProfesor = forms.CharField(widget = forms.PasswordInput())

class ingresarAdministracion(forms.form):
    emailAdmin = forms.EmailField(null=False)
    contraAdmin = forms.CharField(widget = forms.PasswordInput())

class contactUs(forms.form):
    fname = forms.CharField(max_length=255, null=False)
    lname = forms.CharField(max_length=255, null=False)
    email = forms.EmailField(null=False)
    ciudad_list = ['Paysandú','Salto', 'Montevideo']
    ciudad = forms.ChoiceField(choices=ciudad_list)
    tema = forms.Textarea(max_length=500, null=False)
