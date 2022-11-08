from django.shortcuts import render, redirect
from django.db import connection
from django.db import connections
from alumnos.forms import IngresarAlumno
from administracion.models import Usuario
import tkinter as tk
from tkinter import ttk

def asistencia(request):
        
   if request.method == 'POST':
        
        #hacer check en el checkbox con el name de la cedula del usuario ingresado
        #if (name en html) == cedula 
        checked = "checked"
        checkbox = request.form.get(cedula) #se supone que devuelve true o false
        
        if checkbox:
                #agregar la asistencia en el sql
                return
   return render(request, 'asistencia.html')
               

def elegirUsuario(request):
        return render(request, 'elegirUsuario.html')

def ingresarAlumno(request):
   IA = IngresarAlumno(request.POST)
   if request.method == "POST":
        IA.inputUsuarioIA = request.POST.get('inputUsuarioIA')
        IA.inputContraseñaIA = request.POST.get('inputContraseñaIA')
        global cedula
        for u in Usuario.objects.raw('SELECT usuario, cedula, contraseña FROM administracion_usuario WHERE usuario = %s and contraseña = %s',[IA.inputUsuarioIA, IA.inputContraseñaIA]):
            usuario= u.usuario
            contraseña = u.contraseña
            cedula = u.cedula
            

        if IA.inputUsuarioIA == usuario and  IA.inputContraseñaIA == contraseña:
                return redirect('../asistencia/')
   return render(request, 'ingresarAlumno.html')