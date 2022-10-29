from django.contrib import admin
from django.urls import path
from profesores import views



urlpatterns = [
    path('seleccionLista/', views.seleccionLista, name='seleccionLista'),
    path('lista/', views.lista, name='lista'),
    path("ingresarProfesor/", views.ingresarProfesor, name='ingresarProfesor'),
]