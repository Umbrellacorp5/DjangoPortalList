from django.contrib import admin
from administracion import views
from django.urls import path, include


urlpatterns = [
    path('contactUs/', views.contactUs, name='contactUs'),
    path('ingresarAdministracion/', views.ingresarAdministracion, name='ingresarAdministracion'),
    path('registroAlumno/', views.registroAlumno, name='registroAlumno'),
    path('elegirAdmin/', views.elegirAdmin, name='elegirAdmin'),
    path('registroProfesor/', views.registroProfesor, name='registroProfesor'),
    path("seleccionarRegistro/", views.seleccionarRegistro, name='seleccionarRegistro'),
    path("asistencia/", views.asistencia, name='asistencia'),
    path('',views.index, name='index'),

]  