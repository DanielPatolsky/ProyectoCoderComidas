from django.db import models

class Comida(models.Model):
    pais =models.CharField(max_length=100)
    comida =models.CharField(max_length=100)

    def __str__(self):

        return f"Pais: {self.pais} Comida: {self.comida}"

class Restaurante(models.Model):
    pais =models.CharField(max_length=100)
    nombre =models.CharField(max_length=100)

    def __str__(self):

        return f"Pais: {self.pais} Nombre: {self.nombre}"

class Ciudad(models.Model):
    pais = models.CharField(max_length=100)
    continente = models.CharField(max_length=100)

    def __str__(self):
        return f"Pais: {self.pais} Continente: {self.continente}"
        