# Register your models here.
#añadir apps al panel de admin
from django.contrib import admin

from .models import Administrador

admin.site.register(Administrador)