from enum import unique
from django.db import models
from alumnos.models import models
from profesores.models import Lista
# Create your models here.
#crea las tablas en pyhton

class Administrador(models.Model):
    codAdministrador = models.IntegerField( primary_key=True, null=False, unique=True)
    email = models.CharField(max_length=255, null=False)
    contraseña = models.CharField(max_length=255, null=False)

class Usuario(models.Model):
    cedula = models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=255, null=False)
    contraseña = models.CharField(max_length=255, null=False)
    apellido = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    codAdministrador = models.ForeignKey(Administrador,on_delete=models.CASCADE, null=False)


class Grupo(models.Model):
    codGrupo = models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=255, null=False)

class Estan(models.Model):
    codGrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, primary_key=True, null=False)
    usuarioci = models.ForeignKey(Usuario, on_delete=models.CASCADE, primary_key=True, null=False)

class Tienen(models.Model):
    codGrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, primary_key=True, null=False)
    usuarioci = models.ForeignKey(Usuario, on_delete=models.CASCADE, primary_key=True, null=False)

class Pasan(models.Model):
    codGrupo = models.ForeignKey( Grupo,on_delete=models.CASCADE, primary_key=True, null=False)
    usuarioci = models.ForeignKey(Usuario, on_delete=models.CASCADE, primary_key=True, null=False)
    cod_lista = models.ForeignKey(Lista,on_delete=models.CASCADE, primary_key=True, null=False)
    fecha = models.DateField(null=False)