from ast import Delete
import imp
from django.shortcuts import render
from prueba.forms import *
from prueba.models import *
from prueba.models import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def inicio(request):

        #Intente usar un avatar pero por alguna razon me tira error al poner esta lineas de codigo.
        #diccionario = {}
        #cantidadDeAvatares = 0
        #if request.user.is_authenticated:
        #avatar = Avatar.objects.filter( user = request.user.id)    
        #for a in avatar:
        #cantidadDeAvatares = cantidadDeAvatares + 1
        #diccionario["avatar"] = avatar[cantidadDeAvatares-1].imagen.url 
    return render(request, "inicio.html")

def comidas(request):
    return render(request, "comidas.html")

def restaurantes(request):
    return render(request, "restaurantes.html")

def ciudades(request):
    return render(request, "ciudades.html")

def about(request):
    return render(request, "about.html")

def nofunciona(request):
    return render(request, "nofunciona.html")

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

@login_required
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
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#CRUD COMIDAS-------------------------------------------------------------------#----------------------------------------------------------------#
class ComidaList(ListView):
    model= Comida
    template_name= "comidas_list.html"


class ComidaDetalle(DetailView):
    model = Comida
    template_name = "comida_detalle.html"

class ComidaCreacion(CreateView):
    model = Comida
    success_url= "../comida/list"
    fields = ["pais","comida"]

class ComidaUpdate(UpdateView):
    model = Comida
    success_url= "../comida/list"
    fields = ["pais","comida"]

class ComidaDelete(DeleteView):
    model = Comida
    success_url= "../comida/list"

#CRUD Restaurantes-------------------------------------------------------------------#----------------------------------------------------------------#
class RestauranteList(ListView):
    model= Restaurante
    template_name= "restaurantes_list.html"

class RestauranteDetalle(DetailView):
    model = Restaurante
    template_name = "restaurante_detalle.html"

class RestauranteCreacion(CreateView):
    model = Restaurante
    success_url= "restaurante/list"
    fields = ["pais","nombre"]

class RestauranteUpdate(UpdateView):
    model = Restaurante
    success_url= "../restaurante/list"
    fields = ["pais","nombre"]

class RestauranteDelete(DeleteView):
    model = Restaurante
    success_url= "../restaurante/list"

#-------------------------------------------------------------------#----------------------------------------------------------------#

def login_request(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")          
            user = authenticate(username=usuario, password = contra)
            if user is not None: 
                login(request, user)
                return render(request, "inicio.html", {"mensaje":f"BIENVENIDO, {usuario}!"})
            else:
                return render(request, "inicio.html", {"mensaje":f"DATOS INCORRECTOS!"})           
        else:
            return render(request, "inicio.html", {"mensaje":f"FORMULARIO erroneo"})
    form = AuthenticationForm() 
    return render(request, "login.html", {"form":form} )

def register(request):
      if request.method == 'POST':
            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"inicio.html" ,  {"mensaje":f"{username} Creado :)"})
      else:
            #form = UserCreationForm()             
            form = UserRegisterForm()     
      return render(request,"register.html" ,  {"form":form})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            return render(request, "inicio.html")
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
    return render(request, "editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})

@login_required
def agregarAvatar(request):
      if request.method == 'POST':
            miFormulario = AvatarFormulario(request.POST, request.FILES) 
            if miFormulario.is_valid():   
                  u = User.objects.get(username=request.user)
                  avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen'])      
                  avatar.save()
                  return render(request, "inicio.html") 
      else: 
            miFormulario= AvatarFormulario() 
      return render(request, "agregarAvatar.html", {"miFormulario":miFormulario})
