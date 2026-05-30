from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Proyecto
from django.contrib.auth.decorators import login_required

# Importaciones necesarias para las Clases Basadas en Vista (CBV) y el Mixin de seguridad
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


@login_required
def page_detail(request, page_id):
    pagina = get_object_or_404(Proyecto, id=page_id)
    return render(request, "core/page_detail.html", {'pagina': pagina})

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def pages_index(request):
    
    termino_busqueda = request.GET.get('buscar', '').strip()
    
    if termino_busqueda:
        
        palabras = termino_busqueda.split()
        filtro_acumulado = Q()
        
        for palabra in palabras:
            
            filtro_acumulado |= Q(titulo__icontains=palabra)
            
        paginas = Proyecto.objects.filter(filtro_acumulado).distinct()
    else:
        paginas = Proyecto.objects.all()
        
    return render(request, "core/pages_index.html", {'paginas': paginas})


# CBV 1: Creación de páginas 
class PageCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    template_name = 'core/page_form.html'
    fields = ['titulo', 'descripcion', 'imagen']
    success_url = reverse_lazy('pages_index')

    def form_valid(self, form):
       
        form.instance.autor = self.request.user
        return super().form_valid(form)

# CBV 2: Edición de páginas
class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto
    template_name = 'core/page_form.html'
    fields = ['titulo', 'descripcion', 'imagen']
    success_url = reverse_lazy('pages_index')

# CBV EXTRA: Borrado de páginas
class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    template_name = 'core/page_confirm_delete.html'
    success_url = reverse_lazy('pages_index')