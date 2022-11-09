from django.contrib import admin
from django.urls import path, re_path
from profesores import views




urlpatterns = [
    path('seleccionLista/', views.seleccionLista, name='seleccionLista'),
    path('lista/', views.lista, name='lista'),
    path('ingresarProfesor/', views.ingresarProfesor, name='ingresarProfesor'),
    path('landing/', views.send_dictionary, name='send_dictionary'),
]
