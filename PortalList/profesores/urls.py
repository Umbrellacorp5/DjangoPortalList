from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('elegirUsuario/', views.elegirUsuario),
    path('ingresarProfesor/', views.ingresarProfesor),
    path('seleccionLista/', views.seleccionLista),
    path('lista/', views.lista),
]