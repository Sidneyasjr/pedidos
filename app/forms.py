from django import forms
from django.forms.widgets import NumberInput, Select

from .models import Order, Item


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['date']
        widgets = {
            'customer': Select(
                attrs={'class': 'form-control form-control-sm'}
            ),
            'quantity': NumberInput(
                attrs={'readonly': True, 'class': 'form-control form-control-sm'}
            ),
            'total': NumberInput(
                attrs={'readonly': True, 'class': 'form-control form-control-sm'}
            )
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['order']
        widgets = {
            'product': Select(
                attrs={'oninput': 'dynamic_product(this)', 'class': 'form-control form-control-sm'}
            ),
            'price': NumberInput(
                attrs={'oninput': 'dynamic_total(this)', 'min': '0', 'class': 'form-control form-control-sm price'}
            ),
            'quantity': NumberInput(
                attrs={'oninput': 'dynamic_total(this)', 'class': 'form-control form-control-sm quantity'}
            ),
            'total': NumberInput(
                attrs={'readonly': True, 'min': '0', 'step': '0.01', 'class': 'form-control form-control-sm total'}
            ),
            'rentability': Select(
                attrs={'readonly': True, 'class': 'form-control form-control-sm'}
            )

        }
