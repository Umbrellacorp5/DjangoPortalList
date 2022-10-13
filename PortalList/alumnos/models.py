from django.db import models
from django.forms import ModelForm
from administracion.models import Administrador

# Create your models here.


class Alumno(models.Model):
    codAlumno = models.IntegerField(primary_key=True, null=False)
    #usuarioci = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    numPadre = models.CharField(max_length=255, null=False)
    foto = models.CharField(max_length=255)
    mac = models.CharField(max_length=255)
    cedula = models.IntegerField(null=False, unique=True)
    nombre = models.CharField(max_length=255, null=False)
    usuario = models.CharField(max_length=255, null=False)
    #contrasenia, lo maneja django (?)
    apellido = models.CharField(max_length=255, null=False)
    nombre = models.CharField(max_length=255, null=False)
    email  = models.EmailField(max_length=70,blank=True,unique=True)
    codadministrador = models.ForeignKey(Administrador,on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.codAlumno

class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'alumnos']
