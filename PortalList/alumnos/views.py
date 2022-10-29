from django.shortcuts import render
from django.db import connection
from django.db import connections
from alumnos.forms import IngresarAlumno
from administracion.models import Usuario

def asistencia(request):
        return render(request, 'asistencia.html')

def elegirUsuario(request):
        return render(request, 'elegirUsuario.html')

def ingresarAlumno(request):
   IA = IngresarAlumno(request.POST)
   if request.method == "POST":
        IA.inputUsuarioIA = request.POST.get('inputUsuarioIA')
        IA.inputContraseñaIA = request.POST.get('inputContraseñaIA')
        for u in Usuario.objects.raw('SELECT usuario, cedula, contraseña FROM administracion_usuario WHERE usuario = %s and contraseña = %s',[IA.inputUsuarioIA, IA.inputContraseñaIA]):
            usuario= u.usuario
            contraseña = u.contraseña
        if IA.inputUsuarioIA == usuario and  IA.inputContraseñaIA == contraseña:
                return render(request, 'asistencia.html')
   return render(request, 'ingresarAlumno.html')