from django.shortcuts import render
from django.db import connection
from django.db import connections
from profesores.forms import IngresarProfesor
from administracion.models import Usuario

def ingresarProfesor(request):
   IP = IngresarProfesor(request.POST)
   if request.method == "POST":
        IP.inputUsuarioIP = request.POST.get('inputUsuarioIP')
        IP.inputContraseñaIP = request.POST.get('inputContraseñaIP')
        for u in Usuario.objects.raw('SELECT usuario, cedula, contraseña FROM administracion_usuario WHERE usuario = %s and contraseña = %s',[IP.inputUsuarioIP, IP.inputContraseñaIP]):
            usuario= u.usuario
            contraseña = u.contraseña
        if IP.inputUsuarioIP == usuario and  IP.inputContraseñaIP == contraseña:
                return render(request, 'seleccionLista.html')
   return render(request, 'ingresarProfesor.html')

def seleccionLista(request):
    if request.method == 'GET':
        return render(request, 'seleccionLista.html')

def lista(request):
    if request.method == 'GET':
        return render(request, 'lista.html')