from django.db import models

# Create your models here.

class Comics(models.Model):

    titulo = models.CharField(max_length = 100)
    guionista = models.CharField(max_length = 40)
    dibujante = models.CharField(max_length = 40)
    otros_artistas = models.CharField(max_length = 100)
    editorial = models.CharField(max_length = 50)

class Editorial(models.Model):
    nombre = models.CharField(max_length = 50)
    país = models.CharField(max_length = 40)

class Guionista(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)

class Dibujante(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)