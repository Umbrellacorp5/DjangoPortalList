from enum import unique
from django.db import models
from django.forms import ModelForm
# Create your models here.
#crea las tablas en pyhton
#Saca datros de la BD y se los presenta al usuario

class Administrador(models.Model):
    codAdministrador = models.IntegerField(primary_key=True, null=False, default=1)
    email = models.CharField(max_length=255, null=False)
    contraseña = models.CharField(max_length=255, null=False)



class Usuario(models.Model):
    cedula = models.IntegerField(primary_key=True, null=False)
    usuario = models.CharField(max_length=255, null=False)
    nombre = models.CharField(max_length=255, null=False)
    contraseña = models.CharField(max_length=255, null=False)
    apellido = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    codAdministrador = models.ForeignKey(Administrador,on_delete=models.CASCADE)



class Grupo(models.Model):
    codGrupo = models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=255, null=False)
    alumnos = models.ManyToManyField(to='alumnos.Alumno')



class Estan(models.Model):
    class Meta:
        unique_together = (('codGrupo', 'codAlumno'),)

    codGrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=False, primary_key=True)
    codAlumno = models.ForeignKey(to='alumnos.Alumno', on_delete=models.CASCADE, null=False)

'''

    class Meta:
        unique_together = (("codGrupo","codAlumno"))


    def __str__(self):
        return self.dept_id
'''
class Tienen(models.Model):
    class Meta:
        unique_together = (('codGrupo', 'codProfesor'),)

    codGrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=False, primary_key=True)
    codProfesor = models.ForeignKey(to='profesores.Profesor', on_delete=models.CASCADE, null=False)
   

'''
    class Meta:
        unique_together = (("codGrupo","codProfesor"))


    def __str__(self):
        return self.dept_id
'''
class Pasan(models.Model):
    class Meta:
        unique_together = (('codGrupo', 'codProfesor','codLista'),)

    codGrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=False, primary_key=True)
    codProfesor = models.ForeignKey(to='profesores.Profesor', on_delete=models.CASCADE, null=False)
    codLista = models.ForeignKey(to='profesores.Lista',on_delete=models.CASCADE, null=False)
    fecha = models.DateField(null=False)
'''

    class Meta:
        unique_together = (("codGrupo","codProfesor","codLista"))

    def __str__(self):
        return self.dept_id
'''


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
'''
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
'''
'''

class MiMateria(models.Model):
    prim = models.CharField(max_length=255, primary_key=True, null=False)
    Materia = models.CharField(max_length=255, choices=MATERIAS_CHOICES, default='Selecciona', null=False)

'''
