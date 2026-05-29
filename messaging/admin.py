from django.contrib import admin
from .models import Mensaje

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    # Columnas que se van a ver en el listado del panel de admin
    list_display = ('emisor', 'receptor', 'fecha_envio', 'leido')
    
    # Filtros laterales para buscar rápido
    list_filter = ('leido', 'fecha_envio', 'emisor', 'receptor')
    
    # Barra de búsqueda por texto o nombres de usuario
    search_fields = ('contenido', 'emisor__username', 'receptor__username')