from administracion.forms import IngresarAdminsitracion
from django.db import connection
from django.shortcuts import redirect, render
from administracion.models import Administrador


def contactUs(request):
    return render(request, 'contactUs.html')


def index(request):
    
    return render(request, 'index.html')


def seleccionarRegistro(request):
        return render(request, 'seleccionarRegistro.html')


def elegirAdmin(request):
    if request.method == 'POST':
            return redirect('../elegirAdmin/')
    return render(request, 'elegirAdmin.html')


def ingresarAdministracion(request):
    global IA
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
        
        with connection.cursor() as cursor:
           cursor.execute("INSERT INTO administracion_usuario VALUES (%s, '%s', '%s', '%s', '%s', '%s','%s');"%(cedula,email,nombre,usuario,apellido,contraseña,codAdmin))
           cursor.execute("INSERT INTO alumnos_alumno (numPadre, mac, usuarioci_id, fotoAlumno) VALUES (%s, '%s', %s ,'%s');"%((nPadre),(mac),(cedula),(fotoAlumno)))
    return render(request, 'registroAlumno.html')

def registroProfesor(request):
    if request.method == 'POST':
        nombre = request.POST.get('InputUsuarioIP')
        apellido = request.POST.get('inputContraseñaIP')
        cedula = request.POST.get('inputCIIP')
        email = request.POST.get('emailRegistroProfesor')
        usuario = request.POST.get('usuarioRegistroProfesor')
        contraseña = request.POST.get('contraRegistroProfesor')
        cargo =  request.POST.get('cargo')
        antiguedad =  request.POST.get('Antiguedad')
         
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO administracion_usuario VALUES (%s, '%s', '%s', '%s', '%s', '%s','%s');"%(cedula,email,nombre,usuario,apellido,contraseña,codAdmin))
            cursor.execute("INSERT INTO profesores_Profesor (usuarioci_id, cargo, antiguedad) VALUES (%s, '%s', '%s');"%((cedula), (cargo), (antiguedad)))
    return render(request, 'registroProfesor.html')



