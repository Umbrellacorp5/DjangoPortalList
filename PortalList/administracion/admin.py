# Register your models here.
#añadir apps al panel de admin
#como se vera el admin de djago
from django.contrib import admin

from .models import Administrador, Usuario

admin.site.register(Administrador)
admin.site.register(Usuario)