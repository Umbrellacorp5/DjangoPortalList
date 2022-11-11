from administracion.forms import IngresarAdminsitracion
from django.db import connection
from django.shortcuts import redirect, render
from administracion.models import Administrador

'''
Asistencia:
    -Premisa, no se puede llegar a la lista en la BD con la informacion de alumno

    -Posible solucion:
        -No llegar desde el alumno a la lista en db sino guardar la CI y tratar de llevarla a la funcion Lista de Profesores
            -Asistencia Post debe guardar la CI de alumno
            -La CI de ese alumno debe llegar a view de Lista
            -Donde este esa CI cambiar el select de falta a False (default True)
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
    if request.method == 'GET':
        return render(request,'registroProfesor.html')




