# blog/blog/models.py
from django.db import models
from django.utils import timezone


class Almacen(models.Model):
    id = models.AutoField (primary_key = True)
    ISBC = models.CharField(unique=True, max_length=150)
    producto = models.CharField(max_length=150)
    descripcion = models.TextField ()
    precio = models.DecimalField (max_digits=10, decimal_places=2)


    def __str__(self):
        return self.producto

class proovedor(models.Model):

    empresa = models.CharField(unique=True, max_length=150)
    CUIL_empresa = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    telefono = models.DecimalField (max_digits=100, decimal_places=0)


    def __str__(self):
        return self.empresa


class stock_engreso(models.Model):
    entrega = models.CharField(unique=True, max_length=150)
    empresa_de = models.ForeignKey(proovedor, on_delete = models.CASCADE)
    producto_entrada = models.ForeignKey(Almacen, on_delete = models.CASCADE)
    cant_ingreso = models.DecimalField (max_digits=100, decimal_places=0)
    fecha_ingreso = models.DateTimeField(
        default=timezone.now)


    def publish(self):
        self.fecha_ingreso = timezone.now()
        self.save()


    def __str__(self):
        return self.entrega


class stock_venta(models.Model):
    venta_numero = models.CharField(unique=True, max_length=150)
    producto_salida = models.ForeignKey(Almacen, on_delete = models.CASCADE)
    cant_vendida = models.DecimalField(max_digits=100, decimal_places=0)
    fecha_vendido = models.DateTimeField(
        default=timezone.now)


    def publish(self):
        self.fecha_vendido = timezone.now()
        self.save()


    def __str__(self):
        return self.venta_numero


