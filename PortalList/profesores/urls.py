from django.contrib import admin
from django.urls import path
from profesores import views


urlpatterns = [
    path('seleccionLista/', views.seleccionLista, name='seleccionLista'),
    path('lista/', views.lista, name='lista'),
    #path('lista/', views.enviarLista, name='enviarLista'),
    path('lista/', views.cambiarLista, name='cambiarLista'),
    path('ingresarProfesor/', views.ingresarProfesor, name='ingresarProfesor'),
    path('seleccionLista/', views.cambiarLista, name='cambiarLista'),
    
]
