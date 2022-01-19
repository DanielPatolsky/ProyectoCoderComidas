from unicodedata import name
from django.urls import path
from prueba.views import *


urlpatterns = [
    path('inicio/', inicio, name= "Inicio"),
    path('comidas/', comidas, name= "Comidas"),
    path('restaurantes/', restaurantes, name= "Restaurantes"),
    path('ciudades/', ciudades, name= "Ciudades"),
    path('formulariorestaurantes/', formurestaurantes, name= "Formulariorestaurantes"),
    path('formulariocomidas/', formucomidas, name= "Formulariocomidas"),
    path('formulariociudades/', formuciudades, name= "Formulariociudades"),
    path('busquedarestaurantes/', busquedarestaurantes, name= "Busquedarestaurantes"),
    path('buscar/', buscar, name= "Buscar"),
    path('leerciudades/', leerciudades, name= "LeerCiudades"),
    path('eliminarciudad/<ciudad_continente>/', eliminarciudad, name= "EliminarCiudad"),
    path('editarciudad/<ciudad_continente>/', editarciudad, name= "EditarCiudad"),
    #clases en vistas
    path('comida/list/', ComidaList.as_view(), name= "List"),

    path(r'^(?P<pk>\d+)$', ComidaDetalle.as_view(), name= "Detail"),
    path(r'^nuevo$', ComidaCreacion.as_view(), name= "New"),
    path(r'^editar/(?P<pk>\d+)$', ComidaUpdate.as_view(), name= "Edit"),
    path(r'^borrar/(?P<pk>\d+)$', ComidaDelete.as_view(), name= "Eliminar"),
    #Login
    path('login/', login_request, name="Login"),
    path('register/', register, name="Register"),
    

]