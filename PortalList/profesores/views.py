from django.shortcuts import render
from django.db import connection
from django.db import connections

# Create your views here.

def ingresarProfesor(request):
    if request.method == 'GET':
        return render(request, 'ingresarProfesor.html')
    else:
        user = (request.POST['inputUsuarioIP'])
        password = (request.POST['inputContraseñaIP'])
        with connection.cursor() as cursor:
            cursor.execute("SELECT usuario, contraseña FROM administracion_usuario WHERE usuario='%s' and contraseña=%s"%(user,password))
            usuario = cursor.fetchone()
            if usuario == None:
                return render(request, 'ingresarProfesor.html')
            else:
                if usuario[0] == user and usuario[1] == password:
                    return render(request, 'seleccionLista.html')

def seleccionLista(request):
    if request.method == 'GET':
        return render(request, 'seleccionLista.html')

def lista(request):
    if request.method == 'GET':
        return render(request, 'lista.html')