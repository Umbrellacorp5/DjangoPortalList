import json
from django.http import HttpResponse, JsonResponse
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
            global grupo1
            grupo1= ng.codGrupo
        dataDictionary = {
            'NombreMateria': nombreMateria,
            'NombreGrupo': gruposProfesor,
        }
        dataGrupoJSON = dumps(dataDictionary) 
        return render(request, 'seleccionLista.html',{'datajs': dataGrupoJSON})
    if request.method=='POST':
        return redirect('../lista/')


def lista(request):
    '''         
    1-conseguir la lista de codAlumnos
    2-conseguir los usuarios
    3-hacer una lista con los datos de esos usuarios(ci,nombre,apellido,foto)
    4-enviar lista al html de lista
    '''
    if request.method == 'GET':
        #falta recibir la lista de alumnos y enviarla al html
        Asx = []
        Asx1 = []
        Asx2 = []
        i=-1
        q=-1
        for cod in Estan.objects.raw('SELECT * FROM administracion_estan WHERE codGrupo_id = %s',[grupo1]):
            gruposAlumno = cod.codAlumno_id
            Asx.append(gruposAlumno)
            i+=1
            for ua in Alumno.objects.raw('Select codAlumno, usuarioci_id, fotoAlumno FROM alumnos_alumno WHERE codAlumno = %s',[Asx[i]]):
                
                UsuariosAlumno = ua.usuarioci_id
                Asx1.append(UsuariosAlumno)
                q+=1
                for ud in Usuario.objects.raw('Select cedula, nombre, apellido FROM administracion_usuario WHERE cedula = %s',[Asx1[q]]):
                
                    UsuariosDatos= ud.nombre, ud.cedula, ud.apellido
                    Asx2.append(UsuariosDatos)

    
    print('---')
    print(Asx)
    print('---')
    print(Asx1)
    print('---')
    print(Asx2)
    print('---')


    dictionary = {}
    dictOfAlumnos = Convert(Asx2, dictionary)
    print('qqqqqqqqqqq')
    print(dictOfAlumnos)
    print('qqqqqqqqqqq')
    dataGrupoJSON = dumps(dictOfAlumnos)
    print(dataGrupoJSON)
    return render(request,'lista.html',{'dictOfAlumnos' : dataGrupoJSON})
        

    

    


def cambiarLista(cialumno):
    #falta cambiar la checkbox del alumno con esta ci
    '''
    1-mandar ci del alumno al html lista con la pagina cargada
    2-escuchar el cambio de la ci por cada alumno
    2-cambiar el checkbox con id y name ci de False(falta) a True(asistencia)
    '''
    alumno = cialumno
    return ({alumno})


def enviarLista(request):
    #falta enviar la lista a la BD
    '''
    1-recibir los datos de cada alumno en la lista
    2-cargar cada alumno en la bd lista
    '''
    if request.method == 'POST':
        print(request)
    return print('termino')

def Convert(tup, di):
    for a, b, c in tup:
        di.setdefault(a, []).append(b)
        di.setdefault(a, []).append(c)
        #di.setdefault(a, []).append(d)
    return di