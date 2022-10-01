from django.db import models

# Create your models here.


"""
    create table Alumno (
        cod_alumno int not null,
        usuarioci int not null, 
        num_padre int not null,
        foto varchar(255),
        primary key (cod_alumno, usuarioci),
        foreign key (usuarioci) REFERENCES Usuario (cedula)
    );
"""