# blog/blog/models.py
from django.db import models
from django.utils import timezone


class Almacen(models.Model):
    ISBC = models.CharField(unique=True, max_length=150)
    producto = models.CharField(max_length=150)
    descripcion = models.TextField ()
    precio = models.DecimalField (max_digits=10, decimal_places=2)


    def __str__(self):
        return self.producto

class stock_entrada(models.Model):
    proovedor = models.CharField(unique=True, max_length=150)
    producto_entrante= models.CharField(unique=True, max_length=100)
    cant_ingreso = models.DecimalField (max_digits=100, decimal_places=0)
    fecha_ingreso = models.DateTimeField(
        default=timezone.now)


    def publish(self):
        self.fecha_ingreso = timezone.now()
        self.save()


    def __str__(self):
        return self.fecha_ingreso


class stock_salida(models.Model):
    producto_salida = models.CharField(unique=True, max_length=150)
    cant_vendida = models.DecimalField(max_digits=100, decimal_places=0)
    fecha_vendido = models.DateTimeField(
        default=timezone.now)


    def publish(self):
        self.fecha_vendido = timezone.now()
        self.save()


    def __str__(self):
        return self.fecha_vendido


class proovedor(models.Model):
    empresa = models.CharField(unique=True, max_length=150)
    CUIL_empresa = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    telefono = models.DecimalField (max_digits=100, decimal_places=0)
