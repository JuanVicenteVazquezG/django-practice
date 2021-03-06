from django.shortcuts import render

# Create your views here.

# Vistas generias

from django.views.generic import TemplateView, ListView


class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class PruebaListView(ListView):
 #   model = MODEL_NAME
    template_name = "home/lista.html"
    context_object_name = 'lista_numeros'
    queryset = ['1', '2', '3', '4']
