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


# Create your views here.
#Definir ue ejecutar y que enviar al cliente, enviar html
#request handler, toma una solicitud del front y la contesta

def admin(request):
    return render(request, admin.html),
    

    #-------------------------------------------------------LogIn Administraciòn---------------------------------------------------


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