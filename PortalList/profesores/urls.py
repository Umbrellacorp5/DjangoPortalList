from django.contrib import admin
from django.urls import path
from profesores import views as ProfViews
from administracion import views as AdminViews


urlpatterns = [
    path('', ProfViews.ingresarProfesor, name='ingresarProfesor'),
    path('seleccionLista.html', ProfViews.seleccionLista, name='seleccionLista'),
    path('lista.html', ProfViews.lista, name='lista'),
    path('contactUs.html', AdminViews.contactUs, name='contactUs'),
    path('index.html',AdminViews.index, name='index'),
]