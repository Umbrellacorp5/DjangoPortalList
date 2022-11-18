from django.shortcuts import render, redirect
from profesores.forms import IngresarProfesor
from profesores.models import Materia, Profesor
from administracion.models import Usuario, Grupo, Pasan, Estan
from alumnos.models import Alumno
from json import dumps


def ingresarProfesor(request):
   IP = IngresarProfesor(request.POST)
   if request.method == "POST":
        IP.inputUsuarioIP = request.POST.get('inputUsuarioIP')
        IP.inputContraseñaIP = request.POST.get('inputContraseñaIP')
        for u in Usuario.objects.raw('SELECT usuario, cedula, contraseña FROM administracion_usuario WHERE usuario = %s and contraseña = %s',[IP.inputUsuarioIP, IP.inputContraseñaIP]):
            global profesorCI
            profesorCI= u.cedula
        if IP.inputUsuarioIP == u.usuario and  IP.inputContraseñaIP == u.contraseña:
                return redirect('../seleccionLista/')
   return render(request,'ingresarProfesor.html')



def seleccionLista(request):
    if request.method == 'GET':
        for p in Profesor.objects.raw('Select codProfesor FROM profesores_profesor WHERE usuarioci_id=%s', [profesorCI]):
            codProfesor = p.codProfesor
        for m in Materia.objects.raw('Select codMateria, nombre FROM profesores_materia WHERE cod_profesor_id = %s',[codProfesor]):
            nombreMateria = m.nombre
        for g in Pasan.objects.raw('SELECT codGrupo_id, id FROM administracion_pasan WHERE codProfesor_id = %s',[codProfesor]):
            global grupo
            grupo = g.codGrupo_id
        for ng in Grupo.objects.raw('SELECT nombre, codGrupo FROM administracion_grupo WHERE codGrupo = %s',[grupo]):
            gruposProfesor = ng.nombre
        dataDictionary = {
            'NombreMateria': nombreMateria,
            'NombreGrupo': gruposProfesor,
        }
        dataGrupoJSON = dumps(dataDictionary) 
        return render(request, 'seleccionLista.html',{'datajs': dataGrupoJSON})
    if request.method=='POST':
        return redirect('../lista/')

    
def lista(request):
    if request.method == 'GET':
        for al in Estan.objects.raw(' SELECT id, codAlumno_id from administracion_estan WHERE codGrupo_id = %s',[grupo]):
            alumnos = al.codAlumno
            print(alumnos)
            print(alumnos.codAlumno)
            for cod in alumnos.codAlumno:
                for alumnoI in Alumno.objects.raw('SELECT usuarioci_id, fotoAlumno FROM alumnos_alumno WHERE codAlumno = %i', [cod]):
                    alumnoCI = alumnoI.ususarioci_id
                    alumnoFoto = alumnoI.fotoAlumno
                    for ci in alumnoCI:
                        for alumnoUsuario in Usuario.objects.raw('SELECT cedula, nombre, apellido FROM administracion_usuario WHERE cedula = %i',[ci]):
                            Alumnosdict = {
                                'alumCI' : alumnoUsuario.cedula,
                                'alumNombre' :alumnoUsuario.nombre,

                            }
            return render(request,'lista.html')


'''
def lista(request):
    if request.method == 'GET':
        
        Checkboxes work a little bit different from other form inputs, so if you examine a post 
        sent from a form that includes a checkbox, there are two possibilities...

        <input type="checkbox" name="cb1"/>
        if the checlbox is checked, your queryset will look like:
            queryset = {'cb1' : 'on'}
        if it is not checked:
            queryset = {}
        So, you have to check the existence of the related form element name:
        if 'cb1' in queryset:
            "item is selected"
        else:
            "item is not selected"
        
        #if 'cedula' in queryset:
        #
        return render(request, 'lista.html')
        '''


def enviarLista(request):
    if request.method == 'POST':
        print(request)
    return print('termino')



def cambiarLista(cialumno):
    #recibe la ci del alumno
    #cambia 
    alumno = cialumno
    return ({alumno})