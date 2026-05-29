from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import RegistroUsuarioForm, UserUpdateForm, PerfilUpdateForm
from .models import Perfil


class RegistroUsuarioView(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'accounts/registro.html'
    success_url = reverse_lazy('login')

def form_valid(self, form):
        user = form.save()
        # El mensaje de éxito que viaja en la sesión
        messages.success(self.request, "Cuenta creada con éxito. Ya podés iniciar sesión.")
        
        # CORRECCIÓN: Forzamos la redirección inmediata a la URL de éxito
        return redirect(self.success_url)


class LoginUsuarioView(LoginView):
    template_name = 'accounts/login'   
    template_name = 'accounts/login.html'


class CambiarPasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/cambiar_password.html'
    success_url = reverse_lazy('perfil')
    
    def form_valid(self, form):
        messages.success(self.request, "Tu contraseña fue actualizada correctamente.")
        return super().form_valid(form)

@login_required
def perfil_view(request):
    
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        perfil_form = PerfilUpdateForm(request.POST, request.FILES, instance=perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect('perfil')
    else:
        user_form = UserUpdateForm(instance=request.user)
        perfil_form = PerfilUpdateForm(instance=perfil)

    context = {
        'user_form': user_form,
        'perfil_form': perfil_form,
        'perfil': perfil
    }
    return render(request, 'accounts/perfil.html', context)

from django.contrib.auth import logout # Asegurate de que esta importación esté arriba

# Vista de deslogueo directo y seguro
def logout_usuario_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Sesión cerrada correctamente.")
        return redirect('home')
    return redirect('home') # Si intentan entrar por URL, los manda a la home