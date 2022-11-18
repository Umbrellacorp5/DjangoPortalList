from django.db import models



class Alumno(models.Model):
    codAlumno = models.IntegerField(primary_key=True, null=False)
    usuarioci = models.ForeignKey(to='administracion.Usuario', on_delete=models.CASCADE, null=False)
    numPadre = models.CharField(max_length=255, null=False)
    fotoAlumno = models.ImageField(upload_to='profile_images', default='blank-profile-picture.jpg')
    mac = models.CharField(max_length=255)

    def __int__(self):
        return str(self.codAlumno + ' ' + self.usuarioci)
