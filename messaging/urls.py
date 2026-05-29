from django.urls import path
from .views import bandeja_view

urlpatterns = [
    path('', bandeja_view, name='bandeja'),
]