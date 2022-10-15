from django.http import HttpResponse
from django.shortcuts import render


def asistencia(request):
    return render(request, 'admin.html')

def elegirUsuario(request):
    return render(request, 'admin.html')

def ingresarAlumno(request):
    return render(request, 'admin.html')