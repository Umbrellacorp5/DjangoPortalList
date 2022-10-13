from django.shortcuts import render
from alumnos.forms import RegistroAlumno
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
from decorators import allowed_users, unauthenticated_user,allowed_users_homeç
from administracion.forms import *
from administracion.forms import TeacherForm

# Create your views here.
#Definir ue ejecutar y que enviar al cliente, enviar html
#request handler, toma una solicitud del front y la contesta

def admin(request):
    return render(request, admin.html),
    

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
    user_form = CreateUserForm(request.POST or None) 
    teacher_form = TeacherForm(request.POST or None, request.FILES or None)
    context = {'teacher_form': teacher_form,'user_form':user_form, 'page_title':'add student'}
    if request.method == 'POST':
        if user_form.is_valid and teacher_form.is_valid():
            user = user_form.save()
            teacher = teacher_form.save()
            teacher.user =user
            teacher.save()
           
            group = Group.objects.get(name = 'teacher')
            user.groups.add(group)
            messages.success(request, "Successfully Teacher Added")
        else:
            messages.success(request, "Teacher Couldn't  Added")
            
            
    return render(request, 'registration_template/add_teacher.html',context)