from django.contrib import admin
from django.urls import path, include  # <-- Asegúrate de que figure 'include' aquí

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),    # <-- Conecta las rutas de tu app core
]