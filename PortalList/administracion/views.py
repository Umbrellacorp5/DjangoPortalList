from django.forms import ModelForm
from django.shortcuts import render
#from administracion.forms import RegistroAlumno
from administracion.urls import ingresarAdministracion
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

from django.http import FileResponse
import io
from django.db import connections
import os
from django.db.models import Avg
from decorators import allowed_users, allowed_users_home
from administracion.forms import CrearUsuario
from administracion.forms import CrearProfesor

# Create your views here.
#Definir ue ejecutar y que enviar al cliente, enviar html
#request handler, toma una solicitud del front y la contesta

def admin(request):
    return render(request, admin.html),

def ingresarAdministracion(request):
    return render(request, ingresarAdministracion.html),
    

    #-------------------------------------------------------LogIn Administraciòn---------------------------------------------------
@unauthenticated_user

def ingresarAdministracion(request):
    if request.method == 'POST':
        cajaEmail = request.POST.get('cajaEmail')
        cajaContraseña = request.POST.get('cajaContraseña')

        user = authenticate(request, cajaEmail=cajaEmail, cajaContraseña=cajaContraseña)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "El usuario o la contraseña no son correctas")
        

    return render(request, 'ingresarAdministracion/admin.html')


#--------------------------------------------Register Profesor---------------------------------
@login_required(login_url = 'registroProfesor')
@allowed_users(allowed_roles=['admin'])
def registroProfesor(request):
    CrearUsuario = UserCreationForm(request.POST or None) 
    FormProfesor = CrearProfesor(request.POST or None, request.FILES or None)
    context = {'teacher_form': FormProfesor,'CrearUsuario':CrearUsuario, 'page_title':'add student'}
    if request.method == 'POST':
        if CrearUsuario.is_valid and FormProfesor.is_valid():
            user = CrearUsuario.save()
            teacher = FormProfesor.save()
            teacher.user =user
            teacher.save()
            # username = student_form.cleaned_data.get('username')
            # email = student_form.cleaned_data.get('email')
            # password1 = student_form.cleaned_data.get('password1')
            # password2 = student_form.cleaned_data.get('password2')
            # name = student_form.cleaned_data.get('name')
            # name = student_form.cleaned_data.get('phone')
            # passport = request.FILES['profile_pic']
            # fs = FileSystemStorage()
            # filename = fs.save(passport.name, passport)
            # passport_url = fs.url(filename)
            group = Group.objects.get(name = 'teacher')
            user.groups.add(group)
            messages.success(request, "Successfully Teacher Added")
        else:
            messages.success(request, "Teacher Couldn't  Added")
            
            
    return render(request, 'registration_template/add_teacher.html',context)





