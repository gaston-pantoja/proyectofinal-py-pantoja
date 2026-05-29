from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mensaje
from .forms import MensajeForm

@login_required
def bandeja_view(request):
    # Consultas optimizadas filtrando por el operador autenticado
    recibidos = Mensaje.objects.filter(receptor=request.user)
    enviados = Mensaje.objects.filter(emisor=request.user)

    # Procesamiento del formulario de envío directo
    if request.method == 'POST':
        form = MensajeForm(request.POST, user=request.user)
        if form.is_valid():
            mensaje_instancia = form.save(commit=False)
            mensaje_instancia.emisor = request.user  # Asignamos al creador del POST
            mensaje_instancia.save()
            messages.success(request, "Mensaje enviado con éxito al operador.")
            return redirect('bandeja')
    else:
        form = MensajeForm(user=request.user)

    context = {
        'recibidos': recibidos,
        'enviados': enviados,
        'form': form
    }
    return render(request, 'messaging/bandeja.html', context)