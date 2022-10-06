from django.db import models
from administracion.models import Usuario

# Create your models here.


class Alumno(models.Model):
    cod_alumno = models.IntegerField('cod_alumno',primary_key=True, null=False)
    usuarioci = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    num_padre = models.CharField('num_padre', max_length=255, null=False)
    foto = models.CharField(max_length=255)
    mac = models.CharField(max_length=255)

