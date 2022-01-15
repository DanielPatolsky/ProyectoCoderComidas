from django.shortcuts import render
# Create your views here.

def inicio(request):
    return render(request, "inicio.html")


def comidas(request):
    return render(request, "comidas.html")

def restaurantes(request):
    return render(request, "restaurantes.html")


