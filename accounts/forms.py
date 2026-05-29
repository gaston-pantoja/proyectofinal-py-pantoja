from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

# 1. Formulario de Registro con los campos explícitos solicitados
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

# 2. Formulario para actualizar datos base del Usuario
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

# 3. Formulario para actualizar Avatar y Biografía de la extensión Perfil
class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'biografia']