#es una clase que tiene la información que llevará uno o  más formularios en un template
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Producto




class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto 
        fields = ['codigo', 'descripcion', 'precio', 'stock','imagen']
        labels = {
            'codigo' : "codigo",
            'descripcion' : "descripcion",
            'precio' : "precio",
            'stock' : "stock",
            'imagen': "Imagen",
        }
        widgets={
            'codigo' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese una codigo',
                    'class' : 'form-control',
                    'id' : 'codigo'
                }
            ),
            'descripcion':forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese una descripcion',
                    'class' : 'form-control',
                    'id' : 'descripcion'
                }
            ),
            'precio':forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese un precio',
                    'class' : 'form-control',
                    'id' : 'precio'
                }
            ),
            'stock':forms.Select(
                attrs={
                    'class' : 'form-control',
                    'id' : 'stock'
                }
            ),
            'imagen':forms.FileInput(
                attrs={
                    'class' : 'form-control',
                    'id' : 'imagen'
                }
            )
        }