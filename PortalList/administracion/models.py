from enum import unique
from django.db import models
from alumnos.models import Alumno
from profesores.models import Lista, Profesor
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

'''
class Usuario(models.Model):
    cedula = models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=255, null=False)
    contraseña = models.CharField(max_length=255, null=False)
    apellido = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    codAdministrador = models.ForeignKey(Administrador,on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.cedula
'''

class Grupo(models.Model):
    codGrupo = models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=255, null=False)
    alumnos = models.ManyToManyField(Alumno)

    def __str__(self):
        return self.codGrupo

class Estan(models.Model):
    codGrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=False)
    codAlumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.dept_id

class Tienen(models.Model):
    codGrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=False)
    codProfesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.dept_id

class Pasan(models.Model):
    codGrupo = models.ForeignKey( Grupo,on_delete=models.CASCADE, null=False)
    codProfesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=False)
    cod_lista = models.ForeignKey(Lista,on_delete=models.CASCADE, null=False)
    fecha = models.DateField(null=False)

    def __str__(self):
        return self.dept_id



'''  <option>Matemáticas</option>
              <option>Sistemas Operativos I</option>
              <option>Sistemas Operativos II</option>
              <option>Sistemas Operativos III</option>
              <option>A.D.A</option>
              <option>Gestión de Proyecto</option>
              <option>Formación Empresarial</option>
              <option>Filosofía</option>
              <option>Sociología</option>
              <option>Inglés</option>
              <option>Base de Datos I</option>
              <option>Base de Datos II</option>
              <option>Programación I</option>
              <option>Programación II</option>
              <option>Programación III</option>
              <option>Redes datos y seguridad</option>
              <option>Economía</option>
              <option>A.P.T</option>
              <option>Laboratorio Equipos Informatico</option>
              <option>Geometría</option>
              <option>Diseño Web</option> '''

MATERIAS_CHOICES = (
    ('Matemáticas','MATEMÁTICAS'),
    ('Sistemas Operativos I', 'PROGRAMACIONI'),
    ('Sistemas Opertativos II','ECONOMIA'),
    ('Sistemas Opertativos III','INGLES'),
    ('A.D.A','SOCIOLOGIA'),
    ('Gestión de Proyecto','SOCIOLOGIA'),
    ('Formación Empresarial','SOCIOLOGIA'),
    ('Filosofía','SOCIOLOGIA'),
    ('Sociología','SOCIOLOGIA'),
    ('Inglés','SOCIOLOGIA'),
   ('Base de Datos I','MATEMATICAS'),
    ('Base de Datos II', 'PROGRAMACIONI'),
    ('Programación I','ECONOMIA'),
    ('Programación II','INGLES'),
    ('Programación III','SOCIOLOGIA'),
    ('sociologia','SOCIOLOGIA'),
    ('sociologia','SOCIOLOGIA'),
    ('sociologia','SOCIOLOGIA'),
    ('sociologia','SOCIOLOGIA'),
    ('sociologia','SOCIOLOGIA'),
)

class MiMateria(models.Model):
  Materia = models.CharField(max_length=6, choices=MATERIAS_CHOICES, default='Selecciona')