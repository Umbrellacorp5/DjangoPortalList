from django import forms
from administracion.models import Administrador
from alumnos.models import Alumno
from administracion.models import Usuario, Grupo
from django.forms import ModelForm

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
    usuario= forms.CharField(label="usuario", max_length=255, required=True)
    contraseña= forms.CharField(label="contraseña", max_length=255, required=True)

    class Meta:
        model = Usuario
        fields = ['nombre','apellido','cedula','email','usuario','contraseña']

class RegistroAlumno2(ModelForm):
    fotoAlumno =forms.ImageField(max_length=255)
    nPadre = forms.NumberInput()

    class Meta:
        model = Alumno
        fields = ['fotoAlumno','numPadre']

class RegistroAlumno3(ModelForm):
    Grupo = forms.CharField(max_length=255, required=True)

    class Meta:
        model = Grupo
        fields = '__all__'
    
            
    def __init__(self, *args, **kwargs):
            codAdministradorPK = kwargs.pop('codAdministrador', 1)
            super(RegistroAlumno, self).__init__(*args, **kwargs)
            self.fields['codAdministrador']=forms.ModelChoiceField(queryset=Administrador.objects.filter(codAdministrador=codAdministradorPK))
