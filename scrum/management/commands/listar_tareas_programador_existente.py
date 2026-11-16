from django.core.management import BaseCommand

from scrum.models import Tareas, Programador
from datetime import date


class Command(BaseCommand):
    help = "Este comando lista las tareas creadas"

    def handle(self, *args, **options):
        try:
            programador = Programador.objects.get(pk=1)
            tareas = Tareas(nombre="Tarea con programador", fecha_inicio=date.today(), programador=programador)
            tareas.save()
            self.stdout.write(self.style.SUCCESS(f"La tarea con nombre: {tareas.nombre} ha sido creada correctamente"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Se ha producido un error al crear la tarea: {e} "))

