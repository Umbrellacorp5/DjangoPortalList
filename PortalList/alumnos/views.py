from django.http import HttpResponse
from django.shortcuts import render


def asistencia(request):
    if request.method == 'GET':
        return render(request, 'asistencia.html')

def elegirUsuario(request):
    if request.method == 'GET':
        return render(request, 'elegirUsuario.html')

def ingresarAlumno(request):
    if request.method == 'GET':
        return render(request, 'ingresarAlumno.html')