from django.shortcuts import render
from django.db import connection
from django.db import connections

def asistencia(request):
    if request.method == 'GET':
        return render(request, 'asistencia.html')

def elegirUsuario(request):
    if request.method == 'GET':
        return render(request, 'elegirUsuario.html')

def ingresarAlumno(request):
    if request.method == 'GET':
        return render(request, 'ingresarAlumno.html')
    else:
        user = (request.POST['inputUsuarioIA'])
        password = (request.POST['inputContraseñaIA'])
        with connection.cursor() as cursor:
            cursor.execute("SELECT usuario, contraseña FROM administracion_usuario WHERE usuario='%s' and contraseña=%s"%(user,password))
            usuario = cursor.fetchone()
            if usuario == None:
                return render(request, 'ingresarAlumno.html')
            else:
                if usuario[0] == user and usuario[1] == password:
                    return render(request, 'asistencia.html')