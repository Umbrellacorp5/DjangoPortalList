
from administracion.forms import IngresarAdminsitracion
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from administracion.models import Administrador, Usuario

# Create your views here.
#Definir ue ejecutar y que enviar al cliente, enviar html
#request handler, toma una solicitud del front y la contesta

'''
Funcionalidades:

    -LogIn, nombreUsuario + contraseña
    -LogOut

    -Crear, Leer, Actualizar y Borrar Profesores
    -Crear, Leer, Actualizar y Borrar Alumnos
    -Crear, Leer, Actualizar y Borrar Grupos
    -Crear, Leer, Actualizar y Borrar Listas

Flow:
    -Admin
        Login
        crear usuario
        crear lista
        crear grupo, asignar lista
        asignar usuario a profesor/alumno

'''


def contactUs(request):
    return render(request, 'contactUs.html')



def index(request):
    
    return render(request, 'index.html')



def seleccionarRegistro(request):
    
    if request.method == 'GET':
        return render(request, 'seleccionarRegistro.html')

def elegirAdmin(request):
    if request.method == 'POST':
            return redirect('../elegirAdmin/')
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
                    return redirect('../elegirAdmin/')
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




