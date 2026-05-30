from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Proyecto

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def pages_index(request):
    # Capturamos el término y limpiamos espacios vacíos
    termino_busqueda = request.GET.get('buscar', '').strip()
    
    if termino_busqueda:
        # Partimos la frase por palabras para que si escribe de más, igual encuentre el post
        palabras = termino_busqueda.split()
        filtro_acumulado = Q()
        
        for palabra in palabras:
            # Usamos icontains que es 100% compatible con SQLite y no rompe con tildes
            filtro_acumulado |= Q(titulo__icontains=palabra)
            
        paginas = Proyecto.objects.filter(filtro_acumulado).distinct()
    else:
        paginas = Proyecto.objects.all()
        
    return render(request, "core/pages_index.html", {'paginas': paginas})

def page_detail(request, page_id):
    pagina = get_object_or_404(Proyecto, id=page_id)
    return render(request, "core/page_detail.html", {'pagina': pagina})