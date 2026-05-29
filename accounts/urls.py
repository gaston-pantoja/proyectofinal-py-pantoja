from django.urls import path
from .views import (
    RegistroUsuarioView, 
    LoginUsuarioView, 
    perfil_view, 
    CambiarPasswordView, 
    logout_usuario_view  
)

urlpatterns = [
    path('login/', LoginUsuarioView.as_view(), name='login'),
    path('logout/', logout_usuario_view, name='logout'), 
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('perfil/', perfil_view, name='perfil'),
    path('perfil/password/', CambiarPasswordView.as_view(), name='cambiar_password'),
]