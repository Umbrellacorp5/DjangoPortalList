from enum import unique
from django.db import models
from django.forms import ModelForm
# Create your models here.
#crea las tablas en pyhton
#Saca datros de la BD y se los presenta al usuario

class Administrador(models.Model):
    codAdministrador = models.IntegerField( primary_key=True, null=False, unique=True)
    email = models.CharField(max_length=255, null=False)
    contraseña = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.codAdministrador


class Usuario(models.Model):
    cedula = models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=255, null=False)
    contraseña = models.CharField(max_length=255, null=False)
    apellido = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    codAdministrador = models.ForeignKey(Administrador,on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.cedula


class Grupo(models.Model):
    codGrupo = models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=255, null=False)
    alumnos = models.ManyToManyField(to='alumnos.Alumno')

    def __str__(self):
        return self.codGrupo

class Estan(models.Model):
    codGrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=False)
    codAlumno = models.ForeignKey(to='alumnos.Alumno', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.dept_id

class Tienen(models.Model):
    codGrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=False)
    codProfesor = models.ForeignKey(to='profesores.Profesor', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.dept_id

class Pasan(models.Model):
    codGrupo = models.ForeignKey( Grupo,on_delete=models.CASCADE, null=False)
    codProfesor = models.ForeignKey(to='profesores.Profesor', on_delete=models.CASCADE, null=False)
    cod_lista = models.ForeignKey(to='profesores.Lista',on_delete=models.CASCADE, null=False)
    fecha = models.DateField(null=False)

    def __str__(self):
        return self.dept_id

