from django.contrib import admin
from administracion import views
from django.urls import path, include


urlpatterns = [
    path('contactUs.html', views.contactUs, name='contactUs'),
    path('ingresarAdministracion.html', views.ingresarAdministracion, name='ingresarAdministracion'),
    path('registroAlumno.html', views.registroAlumno, name='registroAlumno'),
    path('elegirAdmin.html', views.elegirAdmin, name='elegirAdmin'),
    path('registroProfesor.html', views.registroProfesor, name='registroProfesor'),
    path("seleccionarRegistro.html", views.seleccionarRegistro, name='seleccionarRegistro'),    
    path('',views.index, name='index'),

]  