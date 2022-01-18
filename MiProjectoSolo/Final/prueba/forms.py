from django import forms

class FormuRestaurantes(forms.Form):
    pais =forms.CharField(max_length=100)
    nombre =forms.CharField(max_length=100)

class FormuComidas(forms.Form):
    pais =forms.CharField(max_length=100)
    comida =forms.CharField(max_length=100)

class FormuCiudades(forms.Form):
    pais =forms.CharField(max_length=100)
    continente =forms.CharField(max_length=100)
