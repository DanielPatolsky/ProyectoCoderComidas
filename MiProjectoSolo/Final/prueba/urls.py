from unicodedata import name
from django.urls import path
from prueba.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('inicio/', inicio, name= "Inicio"),
    path('comidas/', comidas, name= "Comidas"),
    path('restaurantes/', restaurantes, name= "Restaurantes"),
    path('ciudades/', ciudades, name= "Ciudades"),
    path('about/', about, name= "About"),
    path('nofunciona/', nofunciona, name= "Nofunciona"),
    
    #path('formulariorestaurantes/', formurestaurantes, name= "Formulariorestaurantes"),
    #path('formulariocomidas/', formucomidas, name= "Formulariocomidas"),
    #path('formulariociudades/', formuciudades, name= "Formulariociudades"),
    #path('busquedarestaurantes/', busquedarestaurantes, name= "Busquedarestaurantes"),
    #path('buscar/', buscar, name= "Buscar"),
    #path('leerciudades/', leerciudades, name= "LeerCiudades"),
    #path('eliminarciudad/<ciudad_continente>/', eliminarciudad, name= "EliminarCiudad"),
    #path('editarciudad/<ciudad_continente>/', editarciudad, name= "EditarCiudad"),

    #clases en vistas de comida
    path('comida/list/', ComidaList.as_view(), name= "List"),
    path(r'^(?P<pk>\d+)$', ComidaDetalle.as_view(), name= "Detail"),
    path(r'^nuevo$', login_required(ComidaCreacion.as_view()), name= "New"),
    path(r'^editar/(?P<pk>\d+)$', login_required(ComidaUpdate.as_view()), name= "Edit"),
    path(r'^borrar/(?P<pk>\d+)$', login_required(ComidaDelete.as_view()), name= "Eliminar"),
    #clases en vistas de restaurantes
    path('restaurante/list/', RestauranteList.as_view(), name= "ResList"),
    path(r'^(?P<pk>\d+)1$', RestauranteDetalle.as_view(), name= "ResDetail"),
    path(r'^nuevo1$', login_required (RestauranteCreacion.as_view()), name= "ResNew"),
    path(r'^editar/(?P<pk>\d+)1$', login_required(RestauranteUpdate.as_view()), name= "ResEdit"),
    path(r'^borrar/(?P<pk>\d+)1$', login_required(RestauranteDelete.as_view()), name= "ResEliminar"),
    #Login
    path('login/', login_request, name="Login"),
    path('register/', register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="Logout"),
    path('editarperfil', editarPerfil, name="EditarPerfil"),

    #path('agregarAvatar', agregarAvatar, name="AgregarAvatar"),
    

]