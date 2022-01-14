from django.db import models

class Curso(models.Model):
    curso =models.CharField(max_length=100)
    comision=models.IntegerField()