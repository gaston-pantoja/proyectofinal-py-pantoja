from django.shortcuts import render, get_object_or_404
from .models import Proyecto

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def pages_index(request):
  
    paginas = Proyecto.objects.all()
    return render(request, "core/pages_index.html", {'paginas': paginas})

def page_detail(request, page_id):
    pagina = get_object_or_404(Proyecto, id=page_id)
    return render(request, "core/page_detail.html", {'pagina': pagina})