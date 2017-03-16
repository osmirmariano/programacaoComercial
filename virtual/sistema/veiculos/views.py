from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from veiculos.models import Veiculo

def index(request):
    
    lista = ""
    for ultimo in Veiculo.objects.all():
        lista += ultimo.marca
    
    
    return HttpResponse(lista) 