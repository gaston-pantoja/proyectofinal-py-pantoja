from django import forms
from .models import Proyecto
from ckeditor.widgets import CKEditorWidget

class ProyectoForm(forms.ModelForm):
    descripcion = forms.CharField(widget=CKEditorWidget(), label="Descripción")

    class Meta:
        model = Proyecto
        fields = ['titulo', 'descripcion', 'imagen', 'tecnologias']