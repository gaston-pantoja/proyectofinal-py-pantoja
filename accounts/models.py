from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    # Vincula este perfil directamente a un usuario único de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    
    # Campos obligatorios solicitados por el pliego
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True)
    biografia = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"Perfil de: {self.user.username}"