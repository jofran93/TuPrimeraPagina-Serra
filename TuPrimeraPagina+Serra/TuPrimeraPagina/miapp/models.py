from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    dni = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    sku = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    dni = models.CharField(max_length=10)    
    email = models.CharField(max_length=50)
    
