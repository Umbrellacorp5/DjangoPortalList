from django.db import models



class Profesor(models.Model):
    codProfesor = models.IntegerField(primary_key=True, null=False, unique = True)
    usuarioci = models.ForeignKey( to='administracion.Usuario',on_delete=models.CASCADE, null=False)
    cargo = models.CharField(max_length=255, null=False)
    antiguedad = models.CharField(max_length=255, null=False)
    
    def __int__(self):
        return str(self.codProfesor + ' ' + self.usuarioci)


class Lista(models.Model):
    codLista = models.IntegerField(primary_key=True, null=False)
    falta = models.BooleanField(default=False, null=False)
    justificada = models.BooleanField(default=False, null=False)
    llegada_tarde = models.BooleanField(default=False, null=False)


class Materia(models.Model):
    codMateria = models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=255, null=False)
    cod_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nombre