from django.shortcuts import render
from .models import Proyecto  # Importamos nuestro modelo

def home(request):
    # Traemos todos los proyectos guardados en la base de datos
    proyectos = Proyecto.objects.all()
    # Se los pasamos al template dentro del contexto (diccionario)
    return render(request, "core/home.html", {'proyectos': proyectos})

def about(request):
    return render(request, "core/about.html")