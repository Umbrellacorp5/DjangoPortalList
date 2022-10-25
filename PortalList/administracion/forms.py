import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from administracion.models import Administrador
from alumnos.models import Alumno
from profesores.models import Materia
from profesores.models import Profesor
from administracion.models import Estan, Tienen, Pasan, Usuario, Grupo
from django.forms import ModelForm, widgets
from django.contrib.auth.models import User

class IngresarAdminsitracion(ModelForm):
    email=forms.CharField(label="Nombre", max_length=255, required=True)
    contraseña=forms.CharField(label="Nombre", max_length=255, required=True)

    class Meta:
        model = Administrador
        fields=['email','contraseña']

class RegistroAlumno(ModelForm):
    nombre= forms.CharField(label="Nombre", max_length=255, required=True)
    apellido= forms.CharField(label="Apellido", max_length=255, required=True)
    cedula= forms.CharField(label="cedula", max_length=255, required=True)
    email= forms.CharField(label="email", max_length=255, required=True)
    usuario= forms.CharField(max_length=255, required=True)
    contraseña= forms.CharField(max_length=255, required=True)

    class Meta:
        model = Usuario
        fields = ['nombre','apellido','cedula','email','usuario','contraseña']

    def __init__(self, *args, **kwargs):
        codAdministradorPK = kwargs.pop('codAdministrador', 1)
        super(RegistroAlumno, self).__init__(*args, **kwargs)
        self.fields['codAdministrador']=forms.ModelChoiceField(queryset=Administrador.objects.filter(codAdministrador=codAdministradorPK))

'''
class RegistroAlumno2(ModelForm):
    fotoAlumno =forms.ImageField(max_length=255)
    nPadre = forms.NumberInput()

    class Meta:
        model = Alumno
        fields = '__all__'

class RegistroAlumno3(ModelForm):
    Grupo = forms.CharField(max_length=255, required=True)

    class Meta:
        model = Grupo
        fields = '__all__'
'''

'''
class registroProfesor(forms.form):
    nombreProfesor = forms.CharField(max_length=255, null=False)
    apellidoProfesor =  forms.CharField(max_length=255, null=False)
    cedulaProfesor = forms.NumberInput(null=False)
    emailRegistroProfesor = forms.EmailField(null=False)
    usuarioRegistroProfesor = forms.NumberInput(null=False)
    contraRegistroProfesor = forms.CharField(widget = forms.PasswordInput())
'''
'''
class ingresarAdministracionF(forms.form):
    emailAdmin = forms.EmailField(null=False)
    contraAdmin = forms.CharField(widget = forms.PasswordInput())
'''
'''
class contactUs(forms.form):
    fname = forms.CharField(max_length=255, null=False)
    lname = forms.CharField(max_length=255, null=False)
    email = forms.EmailField(null=False)
    ciudad_list = ['Paysandú','Salto', 'Montevideo']
    ciudad = forms.ChoiceField(choices=ciudad_list)
    tema = forms.Textarea(max_length=500, null=False)
'''
'''
class CrearUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1']
    
    def __init__(self, *args, **kwargs):
        super(CrearUsuario, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
'''
'''
class CrearProfesor(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CrearProfesor, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['nombre'].widget.attrs['placeholder'] = "Nombre"
        self.fields['apellido'].widget.attrs['class'] = 'form-control'
        self.fields['apellido'].widget.attrs['placeholder'] = "Apellido"
        self.fields['cedula'].widget.attrs['class'] = 'form-control'
        self.fields['cedula'].widget.attrs['placeholder'] = "Cédula"
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = "Email"
        self.fields['materias'].widget.attrs['class'] = 'form-control'
        self.fields['materias'].widget.attrs['placeholder'] = "Materias"
        self.fields['grupos'].widget.attrs['class'] = 'form-control'
        self.fields['grupos'].widget.attrs['placeholder'] = "Grupos"
        '''
'''
#Mirar lo de materias y grupo en models
    class Meta:
        model = Profesor
        fields = ['nombre','apellido','cedula','email']

    class Meta:
        model = Materia
        fields = ['codMateria','nombre','horario','cod_profesor']
'''