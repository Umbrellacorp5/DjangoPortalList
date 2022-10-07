from django.contrib import admin
from django.urls import path, include
from alumnos import views
from profesores import views
from administracion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contactUs/', views.contactUs),
    path('ingresarAdministrador/', views.ingresarAdministrador),
    path('registroAlumno/', views.registroAlumno),
    path('registroProfesor/', views.registroProfesor),
    path('seleccionarRegistro/', views.seleccionarRegistro),
    
    path('',include('authentication.urls')),
]