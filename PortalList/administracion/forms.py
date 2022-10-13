import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroAlumno(forms.Form):
    nombre = forms.CharField(max_length=255, null=False)
    apellido = forms.CharField(max_length=255, null=False)
    cedula = forms.NumberInput(null=False)
    numeroPadre = forms.NumberInput(null=False)
    Contraseña = forms.CharField(max_length=255, null=False)
    fotoAlumno = forms.ImageField(null=False)
    emailRegistroAlumno = forms.EmailField(null=False)
    usuarioRegistroAlumno = forms.CharField(max_length=255, null=False)
    contraRegistroAlumno = forms.CharField(widget = forms.PasswordInput(), null=False) 

class registroProfesor(forms.form):
    nombreProfesor = forms.CharField(max_length=255, null=False)
    apellidoProfesor =  forms.CharField(max_length=255, null=False)
    cedulaProfesor = forms.NumberInput(null=False)
    emailRegistroProfesor = forms.EmailField(null=False)
    usuarioRegistroProfesor = forms.NumberInput(null=False)
    contraRegistroProfesor = forms.CharField(widget = forms.PasswordInput())

class ingresarAdministracionF(forms.form):
    emailAdmin = forms.EmailField(null=False)
    contraAdmin = forms.CharField(widget = forms.PasswordInput())

class contactUs(forms.form):
    fname = forms.CharField(max_length=255, null=False)
    lname = forms.CharField(max_length=255, null=False)
    email = forms.EmailField(null=False)
    ciudad_list = ['Paysandú','Salto', 'Montevideo']
    ciudad = forms.ChoiceField(choices=ciudad_list)
    tema = forms.Textarea(max_length=500, null=False)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1']
    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'

