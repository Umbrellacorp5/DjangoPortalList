from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminPL/', views.adminPL),
    path('contactUs/', views.contactUs),
    path('ingresarAdministrador/', views.ingresarAdministrador),
    path('registroAlumno/', views.registroAlumno),
    path('registroProfesor/', views.registroProfesor),
    path('seleccionarRegistro/', views.seleccionarRegistro),
    
    path('',include('authentication.urls')),
]