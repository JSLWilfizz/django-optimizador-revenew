# optimizador/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resultado/', views.index, name='resultados'),
]