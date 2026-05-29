from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Proyecto(models.Model):
    
    titulo = models.CharField(max_length=200)
    tecnologias = models.CharField(max_length=200)
    
    
    descripcion = RichTextField()
    
    
    imagen = models.ImageField(upload_to='blogs/', null=True, blank=True)
    
    
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo