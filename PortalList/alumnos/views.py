from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from django.db import connections
from django.shortcuts import render, redirect
from alumnos.forms import IngresarAlumno


def asistencia(request):
    if request.method == 'GET':
        return render(request, 'asistencia.html')

def elegirUsuario(request):
    if request.method == 'GET':
        return render(request, 'elegirUsuario.html')

def ingresarAlumno(request):
    if request.method == 'GET':
        return render(request, 'ingresarAlumno.html')


def ingresarAlumno(request):
    IA = ingresarAlumno(request.POST)
    print(IA)
    if request.method == "POST":
        IA.inputUsuarioIA = request.POST.get('inputUsuarioIA')
        IA.inputContraseñaIA = request.POST.get('inputContraseñaIA')
        with connection.cursor() as cursor:
           cursor.execute("SELECT email FROM alumnos_alumno WHERE usuario = '%s' and contraseña = '%s'"% ((IA.inputUsuarioIA), (IA.inputContraseñaIA)))
           select_email= cursor.fetchone()
           email = ' '.join(str(e) for e in select_email)
           cursor.execute("SELECT contraseña FROM alumnos_alumno WHERE usuario = '%s' and contraseña = '%s'" % ((IA.inputUsuarioIA), (IA.inputContraseñaIA)))
           select_contraseña= cursor.fetchone()
           contraseña = ' '.join(str(c) for c in select_contraseña)

        if IA.email == email and IA.contraseña == contraseña:
            return redirect(elegirUsuario)
    return render(request, 'ingresarAlumno.html', {'IA': IA})