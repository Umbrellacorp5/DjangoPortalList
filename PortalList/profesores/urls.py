from django.contrib import admin
from django.urls import path
from profesores import views


urlpatterns = [
    path('ingresarProfesor/', views.ingresarProfesor, name='ingresarProfesor'),
    path('seleccionLista/', views.seleccionLista, name='seleccionLista'),
    path('lista/', views.lista, name='lista'),
]