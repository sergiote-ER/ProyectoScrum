from django.core.management import BaseCommand

from scrum.models import Tareas, Etiqueta, Programador
from datetime import date


class Command(BaseCommand):
    help = "Este comando hace tareas de prueba"

    def handle(self, *args, **options):
        try:
            # Creacion de etiquetas
            etiqueta = Etiqueta(nombre="12345")
            etiqueta.save()
            self.stdout.write(self.style.SUCCESS(f"La etiqueta con nombre: {etiqueta.nombre} ha sido creada correctamente"))

            programador = Programador(nombre="Sergio2", apellido1="Sergio", apellido2="Sergio")
            programador.save()
            self.stdout.write(self.style.SUCCESS(f"El programador {programador.nombre} {programador.apellido1} {programador.apellido2} ha sido creada correctamente"))


            # Creacion de tareas
            tareas = Tareas(nombre="Tarea de Sergio", fecha_inicio=date.today(), programador=programador)
            tareas.save()

            tareas.etiquetas.add(etiqueta)

            self.stdout.write(self.style.SUCCESS(f"La tarea con nombre: {tareas.nombre} ha sido creada correctamente"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Se ha producido un error al crear la tarea: {e} "))
