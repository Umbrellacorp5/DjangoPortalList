from administracion import views
from django.urls import path


urlpatterns = [
    path('contactUs/', views.contactUs, name='contactUs'),
    path('ingresarAdministracion/', views.ingresarAdministracion, name='ingresarAdministracion'),
    path('registroAlumno/', views.registroAlumno, name='registroAlumno'),
    path('elegirAdmin/', views.elegirAdmin, name='elegirAdmin'),
    path('registroProfesor/', views.registroProfesor, name='registroProfesor'),
    path("seleccionarRegistro/", views.seleccionarRegistro, name='seleccionarRegistro'),
    path('',views.index, name='index'),
]  