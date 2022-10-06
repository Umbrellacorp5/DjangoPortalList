from django.db import models
from administracion.models import models
from profesores.models import models

# Create your models here.


class Alumno(models.Model):
    cod_alumno = models.IntegerField("cod_profesor",primary_key=True, null=False)
    usuarioci = models.ForeignKey(Usuario, on_delete=models.CASCADE, primary_key=True, null=False)
    num_padre = models.CharField("num_padre", max_length=255, null=False)
    foto = models.CharField(max_length=255)
    mac = models.CharField(max_length=255)