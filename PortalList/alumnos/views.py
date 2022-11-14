from django.shortcuts import render, redirect
from django.db import connection
from django.db import connections
from alumnos.forms import IngresarAlumno
from administracion.models import Usuario, Estan, Pasan
from profesores.models import Lista, Profesor
from alumnos.models import Alumno

'''
def asistencia(request):
   if request.method == 'POST':
        #hacer check en el checkbox con el name de la cedula del usuario ingresado
        #if (name en html) == cedula 
        checked = "checked"
        checkbox = request.form.get(cedula) #se supone que devuelve true o false
        if checkbox:
                for p in Profesor.objects.raw('Select codProfesor FROM profesores_profesor WHERE usuarioci_id=%s', [__all__]):
                        codProfesor = p.codProfesor
                for e in Estan.objects.raw('Select codGrupo_id, id FROM administracion_estan WHERE codAlumno_id = %s',[codAlumno]):
                        codGrupo = e.codGrupo_id
                for pa in Pasan.objects.raw('SELECT codLista_id, id FROM administracion_pasan WHERE codProfesor_id=%s and codGrupo_id=%s',[codProfesor, codGrupo]):
                        codLista = pa.codLista_id
                for l in Lista.objects.raw('UPDATE profesores_lista SET falta = false WHERE codLista = %s',[codLista]):
                 #agregar la asistencia en el sql
                        
                        #UPDATE profesores_lista
                        #SET falta = false
                        #WHERE CustomerID = 1;
   return render(request, 'asistencia.html')
'''


def elegirUsuario(request):
        return render(request, 'elegirUsuario.html')

def ingresarAlumno(request):

   IA = IngresarAlumno(request.POST)
   global cedula
   global codAlumno
   if request.method == "POST":
        IA.inputUsuarioIA = request.POST.get('inputUsuarioIA')
        IA.inputContraseñaIA = request.POST.get('inputContraseñaIA')

        for u in Usuario.objects.raw('SELECT usuario, cedula, contraseña FROM administracion_usuario WHERE usuario = %s and contraseña = %s',[IA.inputUsuarioIA, IA.inputContraseñaIA]):
            usuario= u.usuario
            contraseña = u.contraseña
            cedula = u.cedula
        
        for a in Alumno.objects.raw('SELECT codAlumno FROM alumnos_alumno WHERE usuarioci_id = %s',[usuario]):
                
                codAlumno = a.codAlumno

        if IA.inputUsuarioIA == usuario and  IA.inputContraseñaIA == contraseña:
                return redirect('../asistencia/')
   return render(request, 'ingresarAlumno.html') 


def asistencia(request):
        if request.method == 'POST':
                return render(request, 'asistencia.html', cedula)
        return render(request, 'asistencia.html')
