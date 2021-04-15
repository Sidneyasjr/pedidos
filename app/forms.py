from django import forms

from .models import Order, Item


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['date', 'quantity', 'total']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['rentability']
