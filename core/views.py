from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Proyecto

# Importaciones necesarias para las Clases Basadas en Vista (CBV) y el Mixin de seguridad
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# ==========================================
# 1. VISTAS BASADAS EN FUNCIONES (Existentes)
# ==========================================

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


# CBV 1: Creación de páginas (Cumple con el uso de Mixin y bloqueo de seguridad)
class PageCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    template_name = 'core/page_form.html'
    fields = ['titulo', 'descripcion', 'imagen']
    success_url = reverse_lazy('pages_index')

    def form_valid(self, form):
       
        form.instance.autor = self.request.user
        return super().form_valid(form)

# CBV 2: Edición de páginas (Garantiza que para editar debas estar logueado)
class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto
    template_name = 'core/page_form.html'
    fields = ['titulo', 'descripcion', 'imagen']
    success_url = reverse_lazy('pages_index')

# CBV EXTRA: Borrado de páginas (Por si querés sumarlo desde el frontend)
class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    template_name = 'core/page_confirm_delete.html'
    success_url = reverse_lazy('pages_index')