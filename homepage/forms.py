from django import forms
from .models import Product, BasketItem

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price','description',  'image']

class BasketItemForm(forms.ModelForm):
    class Meta:
        model = BasketItem
        fields = ['quantity']