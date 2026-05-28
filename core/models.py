from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título del Proyecto")
    descripcion = models.TextField(verbose_name="Descripción")
    tecnologias = models.CharField(max_length=150, verbose_name="Tecnologías Utilizadas")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-creado"] # Los más nuevos primero

    def __str__(self):
        return self.titulo