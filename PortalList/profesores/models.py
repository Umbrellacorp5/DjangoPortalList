from django.db import models

# Create your models here.


"""
    create table Profesor(
        cod_profesor int not null unique,
        usuarioci int NOT NULL,
        cargo varchar(255),
        antiguedad varchar(255),
        PRIMARY KEY (cod_profesor, usuarioci),
        FOREIGN KEY (usuarioci) REFERENCES Usuario (cedula)
        ); 
"""