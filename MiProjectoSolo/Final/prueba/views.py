from django.shortcuts import render
from prueba.forms import *
from prueba.models import *
from prueba.models import *
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def comidas(request):
    return render(request, "comidas.html")

def restaurantes(request):
    return render(request, "restaurantes.html")

def ciudades(request):
    return render(request, "ciudades.html")

#-------------------------------------------------------------------#----------------------------------------------------------------#

def formurestaurantes(request):
    if request.method == "POST":
        miFormulario = FormuRestaurantes(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            restaurante = Restaurante(pais= informacion["pais"], nombre= informacion["nombre"])
            restaurante.save()
            return render(request, "inicio.html")
    else:
        miFormulario = FormuRestaurantes()
    return render(request, "formurestaurantes.html",{"miFormulario":miFormulario})
#-------------------------------------------------------------------#----------------------------------------------------------------#

def formucomidas(request):
    if request.method == "POST":
        miFormulario2 = FormuComidas(request.POST)
        if miFormulario2.is_valid():
            informacion = miFormulario2.cleaned_data
            comida = Comida(pais = informacion["pais"], comida = informacion["comida"])
            comida.save()
            return render(request, "inicio.html")
    else:
            miFormulario2 = FormuComidas()
    return render(request, "formucomidas.html",{"miFormulario":miFormulario2})
#-------------------------------------------------------------------#----------------------------------------------------------------#

def formuciudades(request):
    if request.method == "POST":
        miFormulario3 = FormuCiudades(request.POST)
        if miFormulario3.is_valid():
            informacion = miFormulario3.cleaned_data
            ciudad = Ciudad(pais = informacion["pais"], continente = informacion["continente"])
            ciudad.save()
            return render(request, "inicio.html")
    else:
            miFormulario3 = FormuCiudades()
    return render(request, "formuciudades.html",{"miFormulario":miFormulario3})


#-------------------------------------------------------------------#----------------------------------------------------------------#
def busquedarestaurantes(request):
    return render(request, "busquedarestaurantes.html")

def buscar(request):
    if request.GET["pais"]:
        pais = request.GET["pais"]
        restaurantes = Restaurante.objects.filter(pais__icontains=pais)
        return render(request, "resultadobusqueda.html",{"restaurantes":restaurantes, "pais":pais})   
    else:
        respuesta= "Mandame informacion "
    return HttpResponse(respuesta)
#-------------------------------------------------------------------#----------------------------------------------------------------#


def leerciudades(request):
    ciudades = Ciudad.objects.all()
    contexto = {"ciudades":ciudades}
    return render(request,"leerciudades.html", contexto)

def eliminarciudad(request, ciudad_continente):
    ciudadqueborro = Ciudad.objects.get(continente=ciudad_continente)
    ciudadqueborro.delete()
    ciudades = Ciudad.objects.all()
    return render(request, "leerciudades.html", {"ciudades":ciudades})

def editarciudad(request, ciudad_continente):
    ciudad = Ciudad.objects.get(continente=ciudad_continente)
    if request.method == "POST":
        miFormulario3 = FormuCiudades(request.POST)
        if miFormulario3.is_valid():
            informacion = miFormulario3.cleaned_data

            ciudad.pais = informacion["pais"]
            ciudad.continente = informacion["continente"]

            ciudad.save()

            return render(request, "inicio.html")
    else:
            miFormulario3 = FormuCiudades(initial={"pais":ciudad.pais,  "continente":ciudad.continente})
    return render(request, "editarciudad.html",{"miFormulario":miFormulario3, "ciudad_continente":ciudad_continente})


#-------------------------------------------------------------------#----------------------------------------------------------------#