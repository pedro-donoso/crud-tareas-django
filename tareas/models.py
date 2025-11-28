from django.db import models


class Tarea(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
