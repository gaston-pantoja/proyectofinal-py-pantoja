from django.contrib import admin
from .models import Proyecto

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    
    list_display = ('titulo', 'tecnologias', 'fecha_creacion')
    
    
    readonly_fields = ('fecha_creacion',)