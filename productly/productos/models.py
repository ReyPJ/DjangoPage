from django.db import models
from django.utils import timezone
from django import forms
# Create your models here.


class Categoria(models.Model):
    # cadena de texto limita, hay que indicarle cuanto ocn max_length
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    # Opciones de on_delete=
    # CASCADE: elimina el producto
    # PROTECT: lanza un error
    # RESTRIC: solo elimina si no existen productos
    # SET_NULL: actualiza a valor nulo
    # SET_DEFAULT: asigna valor por defecto (hay que pasarlo como argumento nombrado)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )
    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
