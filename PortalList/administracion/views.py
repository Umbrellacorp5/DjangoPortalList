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
'''

from administracion.forms import CrearUsuario
from administracion.forms import CrearProfesor
from administracion.decorators import unauthenticated_user
'''
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


'''
def ingresarAdministracion(request):
    IA = IngresarAdminsitracion(request.POST)
    if request.method == "POST":
        IA.email = request.POST.get('email')
        IA.contraseña = request.POST.get('contraseña')
        with connection.cursor() as cursor:
           cursor.execute("SELECT email FROM administracion_administrador WHERE email = '%s' and contraseña = '%s'"% ((IA.email), (IA.contraseña)))
           select_email= cursor.fetchone()
           email = ' '.join(str(e) for e in select_email)
           cursor.execute("SELECT contraseña FROM administracion_administrador WHERE email = '%s' and contraseña = '%s'" % ((IA.email), (IA.contraseña)))
           select_contraseña= cursor.fetchone()
           contraseña = ' '.join(str(c) for c in select_contraseña)
           cursor.execute("SELECT codAdministrador FROM administracion_administrador WHERE email = '%s' and contraseña = '%s'"% ((IA.email), (IA.contraseña)))
           select_cod= cursor.fetchone()
           global codAdmin
           codAdmin = ' '.join(str(o) for o in select_cod)
           

        if IA.email == email and IA.contraseña == contraseña:
            return redirect(elegirAdmin)
    return render(request, 'ingresarAdministracion.html', {'IA': IA})
'''

def ingresarAdministracion(request):
    if request.method == 'GET':
        return render(request, 'ingresarAdministracion.html')
    else:
        email = (request.POST['email'])
        password = (request.POST['contraseña'])
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT email, contraseña FROM administracion_administrador WHERE email='%s' and contraseña='%s' "%(email,password))
            usuario = cursor.fetchone()
            print(usuario[1]) #usuario[0] para email y [1] para pass
            cursor.execute(
                "SELECT codAdministrador FROM administracion_administrador WHERE email='%s' and contraseña='%s'"%(email,password))
            codAdmin = cursor.fetchone()
            print(codAdmin[0])#cod de admin, no se lo de global
            
            if usuario == None:
                return render(request, 'ingresarAdministracion.html')
            else:
                if usuario[0] == email and usuario[1] == password:
                    return render(request, 'elegirAdmin.html')
    
def registroAlumno(request):
    RA1 = RegistroAlumno(request.POST)
    RA2 = RegistroAlumno2(request.POST)
    #RA3 = RegistroAlumno3(request.POST)
    #RA = {'RA1': RA1, 'RA2': RA2, 'RA3': RA3}
    if request.method == "POST":
        RA1.nombre = request.POST.get('nombre')
        RA1.apellido = request.POST.get('apellido')
        RA1.cedula = request.POST.get('cedula')
        RA1.email = request.POST.get('email')
        RA1.usuario = request.POST.get('usuario')
        RA1.contraseña = request.POST.get('contraseña')
        RA2.nPadre = request.POST.get('nPadre')
        RA2.fotoAlumno = request.POST.get('fotoAlumno')
        mac=22
        
        #RA3.Grupo = request.POST.get('Grupo')
        with connection.cursor() as cursor:
           cursor.execute("INSERT INTO administracion_usuario (cedula, email, nombre, usuario, apellido, contraseña, codAdministrador_id) VALUES (%s, '%s', '%s', '%s', '%s', '%s','%s');"%((RA1.cedula),(RA1.email),(RA1.nombre),(RA1.usuario),(RA1.apellido),(RA1.contraseña),(codAdmin)))
           #cursor.execute("INSERT INTO alumnos_alumno (numPadre, fotoAlumno, usuarioci_id, mac) VALUES (%s, '%s', %s, '%s');"%((RA2.nPadre),(RA2.fotoAlumno),(RA1.cedula),(mac)))
        #with connection.cursor() as cursor:
        #   cursor.execute("INSERT INTO administracion_usuario (cedula, email, nombre, usuario, apellido, contraseña, codAdministrador_id) VALUES ('%s', '%s', '%s', '%s', '%s', '%s','%s');"%((RA1.cedula),(RA1.email),(RA1.nombre),(RA1.usuario),(RA1.apellido),(RA1.contraseña),(codAdmin)))
           
            #FKUser = RA1.get('codAdministrador')
            # & RA2.is_valid() & RA3.is_valid()
           # RA2.save()
           # RA3.save()
    return render(request, 'registroAlumno.html', {'RA1': RA1})


def registroProfesor(request):
    if request.method == 'GET':
        return render(request,'registroProfesor.html')




