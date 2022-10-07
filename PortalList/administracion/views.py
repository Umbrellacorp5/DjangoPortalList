from django.shortcuts import render
from .forms import RegistroAlumno
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
#Definir ue ejecutar y que enviar al cliente, enviar html

def admin(request):
    return render(request, admin.html)