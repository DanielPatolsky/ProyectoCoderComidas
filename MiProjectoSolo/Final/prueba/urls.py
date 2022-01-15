from unicodedata import name
from django.urls import path
from prueba.views import *


urlpatterns = [
    path('inicio/', inicio, name= "Inicio"),
    path('comidas/', comidas, name= "Comidas"),
    path('restaurantes/', restaurantes, name= "Restaurantes"),
]