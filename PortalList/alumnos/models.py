from django.db import models
from django.forms import ModelForm
from administracion.models import Usuario

# Create your models here.


class Alumno(models.Model):
    codAlumno = models.IntegerField(primary_key=True, null=False)
    usuarioci = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    numPadre = models.CharField(max_length=255, null=False)
    foto = models.CharField(max_length=255)
    mac = models.CharField(max_length=255)

    def __str__(self):
        return self.codAlumno

class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'alumnos']
