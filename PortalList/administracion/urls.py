from django.contrib import admin
from django.urls import path, include
from administracion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contactUs/', views.contactUs),
    path('ingresarAdministracion/', views.ingresarAdministracion),
    path('registroAlumno/', views.registroAlumno),
    path('registroProfesor/', views.registroProfesor),
    path("seleccionarRegistro/", views.seleccionarRegistro),    
    path("",views.index, name='index')



]  