from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):

    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    
    # Contenido del mensaje
    contenido = models.TextField(max_length=1000)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha_envio'] 

    def __str__(self):
        return f"De {self.emisor.username} para {self.receptor.username} - {self.fecha_envio.strftime('%d/%m/%Y %H:%M')}"