from django.contrib import admin
from django.urls import path, include
from administracion import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('ingresarAdministracion/', views.ingresarAdministracion, name='ingresarAdministracion'),
    path('registroAlumno/', views.registroAlumno, name='registroAlumno'),
    path('registroProfesor/', views.registroProfesor, name='registroProfesor'),
    path("seleccionarRegistro/", views.seleccionarRegistro, name='seleccionarRegistro'),    
    path("",views.index, name='index')



]  