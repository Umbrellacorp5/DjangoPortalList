from enum import unique
from django.db import models
from alumnos.models import models
from administracion.models import models

# Create your models here.

class Profesor(models.Model):
    cod_profesor = models.IntegerField("cod_profesor", primary_key=True, null=False, unique = True)
    usuarioci = models.ForeignKey('administracion.Usuario', on_delete=models.CASCADE, primary_key=True, null=False)
    cargo = models.CharField(max_length=255, null=False)
    antiguedad = models.CharField(max_length=255, null=False)
    #UniqueConstraint(fields=['cod_profesor'], name='co_profesor') #no sé si está bien
    #UniqueConstraint(fields=['cod_profesor'], name='c_profesor') #no sé si está bien 
    #alter table Profesor
	#add CONSTRAINT co_profesor UNIQUE (cod_profesor) 
    #alter table Profesor 
    #add constraint c_profesor UNIQUE (cod_profesor)

class Lista(models.Model):
    cod_lista = models.IntegerField("cod_lista",primary_key=True, null=False)
    falta = models.BooleanField(default=False, null=False)
    justificada = models.BooleanField(default=False, null=False)
    llegada_tarde = models.BooleanField(default=False, null=False)

class Materia(models.Model):
    cod_materia = models.IntegerField("cod_materia", primary_key=True, null=False)
    nombre = models.CharField("num_padre", max_length=255, null=False)
    horario = models.IntegerField()
    cod_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, primary_key=True, null=False)