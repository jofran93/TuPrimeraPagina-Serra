from django.db import models

# Create your models here.

class cliente(models.Model): #Modelo num 1
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    dni = models.IntegerField()
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)

class productos(models.Model): #Modelo num 2
    SKU = models.CharField(max_length=50)
    Precio = models.IntegerField()

class empleados(models.Model): #Modelo num 3
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    workId = models.CharField(max_length=20)