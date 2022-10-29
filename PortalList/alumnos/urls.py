from django.contrib import admin
from django.urls import path
from alumnos import views
from administracion import views as AdminViews

urlpatterns = [
    path("ingresarAlumno/", views.ingresarAlumno, name='ingresarAlumno'),
    path("elegirUsuario/", views.elegirUsuario, name='elegirUsuario'), 
    path("asistencia/", views.asistencia, name='asistencia'), 
]