from ast import ListComp
import email
from django.forms import ModelForm
from django.shortcuts import render, redirect
from administracion.forms import IngresarAdminsitracion
from django.db import connection
#from administracion.forms import RegistroAlumno
#from administracion.urls import ingresarAdministracion
#error circular
from administracion.forms import RegistroAlumno, RegistroAlumno2, RegistroAlumno3
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse
import json
from django.contrib.auth.models import Group
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.templatetags.static import static
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.core import management
from django.core.management.commands import loaddata

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.generic import View
from administracion.models import Administrador, Usuario
from django.http import FileResponse 
import io
from django.db import connections
import os
from django.db.models import Avg
from administracion.decorators import allowed_users, allowed_users_home

# Create your views here.
#Definir ue ejecutar y que enviar al cliente, enviar html
#request handler, toma una solicitud del front y la contesta


def contactUs(request):
    return render(request, 'contactUs.html')



def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')



def seleccionarRegistro(request):
    if request.method == 'GET':
        return render(request, 'seleccionarRegistro.html')

def elegirAdmin(request):
    if request.method == 'GET':
        return render(request, 'elegirAdmin.html')

def ingresarAdministracion(request):
    IA = IngresarAdminsitracion(request.POST)
    if request.method == "POST":
        IA.email = request.POST.get('email')
        IA.contraseña = request.POST.get('contraseña')
        global codAdmin
        for a in Administrador.objects.raw('SELECT email, codAdministrador, contraseña FROM administracion_administrador WHERE email = %s and contraseña = %s',[IA.email, IA.contraseña]):
            email= a.email
            contraseña = a.contraseña
            codAdmin = a.codAdministrador
        if IA.email == email and  IA.contraseña == contraseña:
                    return render(request, 'elegirAdmin.html')
    return render(request, 'ingresarAdministracion.html')
    
    
def registroAlumno(request):
    #RA3 = RegistroAlumno3(request.POST)
    #RA = {'RA1': RA1, 'RA2': RA2, 'RA3': RA3}
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        cedula = request.POST.get('cedula')
        email = request.POST.get('email')
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contraseña')
        nPadre = request.POST.get('nPadre')
        fotoAlumno = request.POST.get('fotoAlumno')
        mac=22
        
        #RA3.Grupo = request.POST.get('Grupo')
        with connection.cursor() as cursor:
           cursor.execute("INSERT INTO administracion_usuario VALUES (%s, '%s', '%s', '%s', '%s', '%s','%s');"%(cedula,email,nombre,usuario,apellido,contraseña,codAdmin))
           cursor.execute("INSERT INTO alumnos_alumno (numPadre, mac, usuarioci_id, fotoAlumno) VALUES (%s, '%s', %s ,'%s');"%((nPadre),(mac),(cedula),(fotoAlumno)))
    return render(request, 'registroAlumno.html')

def registroProfesor(request):
    if request.method == 'GET':
        return render(request,'registroProfesor.html')




