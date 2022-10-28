from django.contrib import admin

# Register your models here.
from .models import Profesor, Materia, Lista
admin.site.register(Profesor)
admin.site.register(Lista)
admin.site.register(Materia)