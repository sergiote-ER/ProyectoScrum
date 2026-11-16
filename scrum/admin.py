from django.contrib import admin

from scrum.models import Tareas, Programador, Proyecto, Etiqueta, Sprint

# Register your models here.
admin.site.register(Tareas)
admin.site.register(Programador)
admin.site.register(Sprint)
admin.site.register(Proyecto)
admin.site.register(Etiqueta)
