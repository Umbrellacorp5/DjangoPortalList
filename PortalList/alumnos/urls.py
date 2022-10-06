from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('asistencia/', views.asistencia, name='asistencia'),
    path('elegirUsuario/', views.elegirUsuario),
    path('ingresarAlumno/', views.ingresarAlumno, name='ingresarAlumno'),
]