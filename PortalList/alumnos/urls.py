from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('alumnos/', include('alumnos.urls')),
    path('admin/', admin.site.urls),
]