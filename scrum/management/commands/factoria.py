import random
from logging import exception

from django.core.management import BaseCommand
from faker import Faker
from scrum.models import Tareas, Programador, Proyecto, Sprint
from datetime import date


class Command(BaseCommand):
    help = "Este comando es una factoria"

    # 10 programadores, 4 sprints, 1 proyecto, 30 tareas, las tareas tienen que usar los objetos creados anteriormente

    def handle(self, *args, **options):
        faker = Faker('es_ES')
        try:
            for i in range(10):
                programador = Programador(nombre=faker.name(), apellido1=faker.last_name())
                programador.save()

            proyecto = Proyecto(nombre="Proyecto DAW")
            proyecto.save()

            for i in range(4):
                sprint = Sprint(fecha_inicio=date.today(), id_proyecto=proyecto)
                sprint.save()

            for i in range(30):
                programadores = Programador.objects.all()
                tarea = Tareas(nombre=faker.name(), programador=random.choice(programadores), fecha_inicio=date.today())
                tarea.save()

            self.stdout.write(self.style.SUCCESS(f"Se ha creado correctamente"))

        except Exception as e:
            self.stdout.write(self.style.SUCCESS(f"Ha ocurrido un error: {e}"))
