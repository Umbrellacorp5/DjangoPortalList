from django.forms import ModelForm
from django.shortcuts import render
from administracion.forms import IngresarAdminsitracion
#from administracion.forms import RegistroAlumno
#from administracion.urls import ingresarAdministracion
#error circular
from administracion.forms import RegistroAlumno
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
from administracion.models import Administrador
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
'''
def admin(request):
    return render(request, admin.html)

def contactUs(request):
    return render(request, 'admin.html')

def seleccionarRegistro(request):
    return render(request, 'admin.html')

def index(request):
    return render(request, 'admin.html')
'''

def ingresarAdministracion(request):
    IA = IngresarAdminsitracion(request)
    if request.method == "POST":
        admin = Administrador.objects.all()
        for a in admin:
            print('{0} - {1}'.format(a.email, a.contraseña))
        IA.email = request.POST.get('emailAdmin')
        IA.contraseña = request.POST.get('contraAdmin')
        if IA.email == a.email:
            print("buenazo")

    return render(request, 'ingresarAdministracion.html', {'IA': IA})

def registroAlumno(request):
    RA1 = RegistroAlumno(request.POST)
   # RA2 = RegistroAlumno2(request.POST)
   # RA3 = RegistroAlumno3(request.POST)
    #RA = {'RA1': RA1, 'RA2': RA2, 'RA3': RA3}
    if request.method == "POST":
        if RA1.is_valid(): 
            FKUser = RA1.get('codAdministrador')
            # & RA2.is_valid() & RA3.is_valid()
            RA1.save()
           # RA2.save()
           # RA3.save()
    return render(request, 'registroAlumno.html', {'RA1': RA1})





