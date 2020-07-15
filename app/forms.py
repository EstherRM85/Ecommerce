from django import forms
from .models import Producto,Carrito

class ProduForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','descripcion','precio']

class CarritoForm(forms.ModelForm):
    class Meta:
        model = Carrito 
        fields = ['cantidad']
                         
