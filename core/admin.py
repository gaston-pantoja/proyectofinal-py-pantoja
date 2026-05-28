from django.contrib import admin
from .models import Proyecto

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    # Campos que se verán como columnas en el listado del panel
    list_display = ('titulo', 'tecnologias', 'creado')
    # Campos de solo lectura para evitar alteraciones accidentales de auditoría
    readonly_fields = ('creado', 'actualizado')