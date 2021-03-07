from django.shortcuts import render

# Create your views here.

# Vistas generias

from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba


class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class PruebaListView(ListView):
 #   model = MODEL_NAME
    template_name = "home/lista.html"
    context_object_name = 'lista_numeros'
    queryset = ['1', '2', '3', '4']


class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'lista_prueba'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    fields = ['titulo', 'subtitulo', 'cantidad']
