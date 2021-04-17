from django import forms
from django.forms.widgets import NumberInput, Select

from .models import Order, Item, Product


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['date']
        widgets = {
            'quantity': NumberInput(
                attrs={'readonly': True}
            ),
            'total': NumberInput(
                attrs={'readonly': True}
            )
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['order']
        widgets = {
            'product': Select(
                attrs={'oninput': 'dynamic_product(this)'}
            ),
            'price': NumberInput(
                attrs={'oninput': 'dynamic_total(this)'}
            ),
            'quantity': NumberInput(
                attrs={'oninput': 'dynamic_total(this)'}
            ),
            'total': NumberInput(
                attrs={'readonly': True}
            ),
            'rentability': Select(
                attrs={'readonly': True}
            )

        }

