from django.db import models
from alumnos.models import models
from profesores.models import models
# Create your models here.

class Administrador(models.Model):
    cod_administrador = models.CharField(max_length=100, primary_key=True)
    email = models.CharField(max_length=255)
    Contrasenia = models.CharField(max_length=255)

class Usuario(models.Model):
    cedula = models.CharField(max_length=100, primary_key=True)
    email = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    usuario = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    Contrasenia = models.CharField(max_length=255)
    cod_administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)

"""
        
    create table Grupo (
        cod_grupo int not null,
        nombre varchar(255),
        primary key (cod_grupo)
        );
        
        
        create table Lista (
           cod_lista int not null,
            falta boolean,
            justificada boolean,
            llegada_tarde boolean, 
            primary key (cod_lista)
            ); 
            
            
         create table Materia (
             cod_materia int not null,
             nombre varchar(255),
             horario int not null,
             cod_profesor int not null,
             PRIMARY KEY (cod_materia, cod_profesor),
             FOREIGN KEY (cod_profesor) REFERENCES Profesor(cod_profesor)
             );
    
    
    create table Estan (
        cod_grupo int not null,
        usuarioci int not null,
        PRIMARY KEY (usuarioci,cod_grupo),
        FOREIGN KEY (cod_grupo) REFERENCES Grupo (cod_grupo)
        foreign key (usuarioci) references Usuario (cedula)
        );
        
        create table Tienen (
             cod_grupo int not null,
        usuarioci int not null,
        PRIMARY KEY (usuarioci,cod_grupo),
        FOREIGN KEY (cod_grupo) REFERENCES Grupo (cod_grupo),
        FOREIGN KEY (usuarioci) REFERENCES Usuario (cedula)
            );
            
         create table Pasan (
             cod_grupo int not null,
             usuarioci int not null,
             cod_lista int not null,
             fecha date,
             PRIMARY KEY (usuarioci,cod_grupo, cod_lista),
             FOREIGN KEY (cod_lista) REFERENCES Lista (cod_lista)
             );
"""