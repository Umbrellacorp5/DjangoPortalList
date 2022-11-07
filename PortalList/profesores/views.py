from django.shortcuts import render, redirect
from django.db import connection
from django.db import connections
from profesores.forms import IngresarProfesor
from administracion.models import Usuario, Grupo, Tienen
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse

'''
Funcionalidades: 

    -LogIn, nombreUsuario + contraseña
    -LogOut

    -Elegir Grupo
        -nombre Grupo + Materia

    -Ver Lista
        -Lista de alumnos
'''


def ingresarProfesor(request):
   IP = IngresarProfesor(request.POST)
   if request.method == "POST":
        IP.inputUsuarioIP = request.POST.get('inputUsuarioIP')
        IP.inputContraseñaIP = request.POST.get('inputContraseñaIP')
        for u in Usuario.objects.raw('SELECT usuario, cedula, contraseña FROM administracion_usuario WHERE usuario = %s and contraseña = %s',[IP.inputUsuarioIP, IP.inputContraseñaIP]):
            usuario= u.usuario
            contraseña = u.contraseña
            global profesorCI
            profesorCI= u.cedula
        if IP.inputUsuarioIP == usuario and  IP.inputContraseñaIP == contraseña:
                return redirect('../seleccionLista/')
   return render(request, 'ingresarProfesor.html')




def seleccionLista(request):
    if request.method == 'GET':
        for g in Grupo.objects.raw('SELECT codGrupo, nombre FROM administracion_grupo'):
            grupo = g.codGrupo
            profesor = profesorCI
            print(g, grupo, profesor)
            for grupos in Tienen.objects.raw('SELECT * FROM administracion_tienen WHERE codGrupo_id = %s and codProfesor_id = %s',[grupo, profesor]):
                gruposProfesor = grupos[1]
                return print(gruposProfesor) 
        
        return render(request, 'seleccionLista.html')
    elif request.method == 'POST':

        return render(request, 'seleccionLista.html')



def lista(request):
    if request.method == 'GET':
        return render(request, 'lista.html')