from django.contrib import admin
from django.urls import path
from alumnos import views
from administracion import views as AdminViews

urlpatterns = [
    path('asistencia.html', views.asistencia, name='asistencia'),
    path('elegirUsuario.html', views.elegirUsuario, name='elegirUsuario'),
    path('', views.ingresarAlumno, name='ingresarAlumno'),
    path('contactUs.html', AdminViews.contactUs, name='contactUs'),
    path('index.html',AdminViews.index, name='index'),
]