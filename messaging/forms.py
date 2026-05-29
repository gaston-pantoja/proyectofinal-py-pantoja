from django import forms
from django.contrib.auth.models import User
from .models import Mensaje

class MensajeForm(forms.ModelForm):

    receptor = forms.ModelChoiceField(
        queryset=User.objects.none(),
        label="Destinatario",
        widget=forms.Select(attrs={
            'style': 'background-color: #222; color: #fff; border: 1px solid #333; padding: 0.5rem; border-radius: 4px; width: 100%;'
        })
    )
    
    contenido = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Escribe tu mensaje técnico aquí...',
            'style': 'background-color: #222; color: #fff; border: 1px solid #333; padding: 0.5rem; border-radius: 4px; width: 100%; resize: none;'
        })
    )

    class Meta:
        model = Mensaje
        fields = ['receptor', 'contenido']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['receptor'].queryset = User.objects.exclude(id=user.id)