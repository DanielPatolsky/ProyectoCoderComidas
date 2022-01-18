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
]