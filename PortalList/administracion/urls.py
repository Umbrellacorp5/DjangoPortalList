from django.contrib import admin
from administracion import views
from django.urls import path, include


urlpatterns = [
    #path('contactUs/', views.contactUs, name='contactUs'),
    path('ingresarAdministracion/', views.ingresarAdministracion, name='ingresarAdministracion'),
    path('registroAlumno/', views.registroAlumno, name='registroAlumno'),
    #path('registroProfesor/', views.registroProfesor, name='registroProfesor'),
    #path("seleccionarRegistro/", views.seleccionarRegistro, name='seleccionarRegistro'),    
    #path("",views.index, name='index'),

]  