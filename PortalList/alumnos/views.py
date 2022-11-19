from django.shortcuts import render, redirect
from alumnos.forms import IngresarAlumno
from administracion.models import Usuario
from profesores.views import cambiarLista
from alumnos.models import Alumno


def elegirUsuario(request):
        return render(request, 'elegirUsuario.html')


def ingresarAlumno(request):
   IA = IngresarAlumno(request.POST)
   global cedula
   global codAlumno
   if request.method == "POST":
        IA.inputUsuarioIA = request.POST.get('inputUsuarioIA')
        IA.inputContraseñaIA = request.POST.get('inputContraseñaIA')
        for u in Usuario.objects.raw('SELECT usuario, cedula, contraseña FROM administracion_usuario WHERE usuario = %s and contraseña = %s',[IA.inputUsuarioIA, IA.inputContraseñaIA]):
            usuario= u.usuario
            contraseña = u.contraseña
            cedula = u.cedula
        for a in Alumno.objects.raw('SELECT codAlumno FROM alumnos_alumno WHERE usuarioci_id = %s',[usuario]):
                codAlumno = a.codAlumno
        if IA.inputUsuarioIA == usuario and  IA.inputContraseñaIA == contraseña:
                return redirect('../asistencia/')
   return render(request, 'ingresarAlumno.html') 


def asistencia(request):
        if request.method == 'POST':
                cambiarLista(cedula)
                return render(request, 'asistencia.html')
        return render(request, 'asistencia.html')
