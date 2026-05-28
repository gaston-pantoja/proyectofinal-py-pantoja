from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),         
    path('about/', views.about, name='about'),
    path('pages/', views.pages_index, name='pages_index'),
    path('pages/<int:page_id>/', views.page_detail, name='page_detail'),
]