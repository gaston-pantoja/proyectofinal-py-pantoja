from django.urls import path
from . import views

urlpatterns = [
    # Rutas existentes basadas en funciones
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pages/', views.pages_index, name='pages_index'),
    path('pages/<int:page_id>/', views.page_detail, name='page_detail'),
    
    # Nuevas rutas basadas en Clases (CBV) para el CRUD obligatorio
    path('pages/crear/', views.PageCreateView.as_view(), name='page_create'),
    path('pages/<int:pk>/editar/', views.PageUpdateView.as_view(), name='page_update'),
    path('pages/<int:pk>/borrar/', views.PageDeleteView.as_view(), name='page_delete'),
]