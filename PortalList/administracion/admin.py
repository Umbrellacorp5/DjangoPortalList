from django.contrib import admin

from .models import Administrador, Usuario, Tienen, Pasan, Estan, Grupo

admin.site.register(Administrador)
admin.site.register(Usuario)
admin.site.register(Tienen)
admin.site.register(Pasan)
admin.site.register(Estan)
admin.site.register(Grupo)