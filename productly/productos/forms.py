from . import models
# Esta dependencia se encargar de generar los formulario en base a modelos
from django.forms import ModelForm
from django import forms


class ProductoForm(ModelForm):
    class Meta:
        model = models.Producto
        fields = ['nombre',
                  'stock',
                  'puntaje',
                  'categoria'
                  ]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control",
                                             "title": "Nombre del producto",
                                             "placeholder": "Nombre del producto"}),

            "stock": forms.NumberInput(attrs={"class": "form-control",
                                              "title": "stock del producto",
                                              "placeholder": "Stock"}),

            "puntaje": forms.NumberInput(attrs={"class": "form-control",
                                                "title": "Puntaje del producto",
                                                "pattern": "[1-5]{1,}+.[0-9]{1, }$",
                                                "placeholder": "Calificacion"}),

            "categoria": forms.Select(attrs={"class": "form-select {{widget.attrs.clas}}"})

        }
