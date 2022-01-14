from django.shortcuts import render
from prueba.models import Curso
# Create your views here.

def padre(request):
    return render(request, "padre.html")

def prueba(request):
    cursoaux = Curso.objects.all
    return render(request, "hijo.html", {"cursos":cursoaux})

def comidas(request):
    return render(request, "comidas.html")


