from django.contrib import admin
from django.urls import path
from profesores import views


urlpatterns = [
    path('ingresarProfesor/', views.ingresarProfesor),
    path('seleccionLista/', views.seleccionLista),
    path('lista/', views.lista),
]