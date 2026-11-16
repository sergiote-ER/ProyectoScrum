from django.test import TestCase
from datetime import date
from .models import *


class TareaTest(TestCase):
    pass

    def test_suma(self):
        resultado = 4 + 4
        self.assertEqual(resultado, 8)

    def test_resta(self):
        resultado = 10 - 5
        self.assertEqual(resultado, 5)

    def test_comparacion(self):
        comprobacion = True
        nombre = "Francisco"
        nombre2 = "francisco"
        if nombre != nombre2:
            comprobacion = False
        self.assertTrue(comprobacion)

    def setUp(self):
        # Estos objetos estarán disponibles en cada test
        self.programador = Programador.objects.create(
            nombre="Francisco"
        )

        self.sprint = Sprint.objects.create(
            fecha_inicio=date(2026, 10, 28)
        )

    def test_crear_tarea(self):
        tarea = Tareas.objects.create(
            nombre="Desarrollar el login",
            fecha_inicio=date(2026, 10, 28),
            completa=False,
            sprint=self.sprint,
            programador=self.programador
        )

        self.assertEqual(tarea.nombre, "Desarrollar el login")
        self.assertFalse(tarea.completada)
        self.assertEqual(tarea.sprint, self.sprint)
        self.assertEqual(tarea.programador, self.programador)
