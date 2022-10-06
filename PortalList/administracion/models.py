from django.db import models
from alumnos.models import models
from profesores.models import models
# Create your models here.
#crea las tablas en pyhton

class Administrador(models.Model):
    cod_administrador = models.IntegerField("cod_administrador", primary_key=True, null=False)
    email = models.CharField(max_length=255, null=False)
    contraseña = models.CharField(max_length=255, null=False)

class Usuario(models.Model):
    cedula = models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=255, null=False)
    contraseña = models.CharField(max_length=255, null=False)
    apellido = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    cod_administrador = models.ForeignKey("cod_administrador", Administrador, on_delete=models.CASCADE, null=False)


class Grupo(models.Model):
    cod_grupo = models.IntegerField("cod_grupo",primary_key=True, null=False)
    nombre = models.CharField(max_length=255, null=False)

class Estan(models.Model):
    cod_grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, primary_key=True, null=False)
    usuarioci = models.ForeignKey(Usuario, on_delete=models.CASCADE, primary_key=True, null=False)

class Tienen(models.Model):
    cod_grupo = models.ForeignKey("cod_grupo", Grupo, on_delete=models.CASCADE, primary_key=True, null=False)
    usuarioci = models.ForeignKey(Usuario, on_delete=models.CASCADE, primary_key=True, null=False)

class Pasan(models.Model):
    cod_grupo = models.ForeignKey("cod_grupo", Grupo, on_delete=models.CASCADE, primary_key=True, null=False)
    usuarioci = models.ForeignKey(Usuario, on_delete=models.CASCADE, primary_key=True, null=False)
    cod_lista = models.ForeignKey("cod_grupo", Grupo, on_delete=models.CASCADE, primary_key=True, null=False)
    fecha = models.DateField(null=False)