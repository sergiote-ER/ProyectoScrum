from django.db import models


class Proyecto(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return f"{self.nombre}"


class Sprint(models.Model):
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_proyecto}"


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id}. {self.nombre}"

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'


class Programador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)

    etiquetas = models.ManyToManyField(Etiqueta, blank=True)

    def __str__(self):
        return f"{self.id}. {self.nombre}, {self.apellido1} {self.apellido2}"

    class Meta:
        verbose_name = 'Programador'
        verbose_name_plural = 'Programadores'


class Tareas(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    completada = models.BooleanField(default=False)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, blank=True, null=True)
    programador = models.ForeignKey(Programador, on_delete=models.CASCADE, blank=True, null=True)

    etiquetas = models.ManyToManyField(Etiqueta, blank=True)

    def __str__(self):
        return f"{self.id}. {self.nombre}"

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
