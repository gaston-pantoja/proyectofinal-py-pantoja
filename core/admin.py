from django.contrib import admin
from .models import Proyecto

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    # Mostramos el título, las tecnologías y nuestra nueva fecha en el listado
    list_display = ('titulo', 'tecnologias', 'fecha_creacion')
    
    # Si quieres que la fecha de creación sea de solo lectura en el formulario de edición:
    readonly_fields = ('fecha_creacion',)