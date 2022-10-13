from django.shortcuts import render
from .forms import RegistroAlumno
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse

# Create your views here.
#Definir ue ejecutar y que enviar al cliente, enviar html
#request handler, toma una solicitud del front y la contesta

def admin(request):
    return render(request, admin.html),
    