from django.contrib import admin

from .models import Pregunta, CategoriaPregunta, Opcion

admin.site.register(Pregunta)
admin.site.register(CategoriaPregunta)
admin.site.register(Opcion)