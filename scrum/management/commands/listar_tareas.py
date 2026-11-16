from django.core.management import BaseCommand

from scrum.models import Tareas


class Command(BaseCommand):
    help = "Este comando lista las tareas creadas"

    def handle(self, *args, **options):

        tareas = Tareas.objects.all()

        for tarea in tareas:
            print(f"{tarea.id}. {tarea.nombre}")


        self.stdout.write(self.style.SUCCESS(f"ESTE COMANDO LISTA TODAS LAS TAREAS"))
