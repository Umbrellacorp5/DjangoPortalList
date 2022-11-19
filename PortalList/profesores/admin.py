from django.contrib import admin

from .models import Profesor, Materia, Lista
admin.site.register(Profesor)
admin.site.register(Lista)
admin.site.register(Materia)