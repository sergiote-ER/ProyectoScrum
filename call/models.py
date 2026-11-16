from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)

class Jugadore(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    rango = models.CharField(max_length=30)
    partidas = models.IntegerField()
    victorias = models.IntegerField()
    nivel = models.IntegerField()
    puntuacion = models.FloatField()
    activo = models.BooleanField()

    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'

    def __str__(self):
        return f"{self.nombre}, {self.edad} años, rango {self.rango}, {self.partidas} partidas, {self.victorias} victorias, nivel {self.nivel}"