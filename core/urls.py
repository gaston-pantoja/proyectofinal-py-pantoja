from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),         # Raíz del sitio (Home)
    path('about/', views.about, name='about'), # Ruta requerida about/
]