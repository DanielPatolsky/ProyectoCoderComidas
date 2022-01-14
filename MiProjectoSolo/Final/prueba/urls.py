from django.urls import path
from prueba.views import *


urlpatterns = [
    path('', padre),
    path('hijo1/', prueba, name='hijo1'),
    path('comidas/', comidas),

]