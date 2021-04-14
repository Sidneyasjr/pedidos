from django import forms

from .models import Customer, Product


class OrderForm(forms.Form):
    customer = forms.ChoiceField(label='Cliente',
                                 choices=[('0', 'Selecione o cliente')] + [(customer.id, customer.name) for customer in
                                                                           Customer.objects.all()])


class ItemForm(forms.Form):
    product = forms.ChoiceField(label='Prduto',
                                choices=[('0', 'Selecione o produto')] + [(product.id, product.name) for product in
                                                                          Product.objects.all()])
    quantity = forms.IntegerField(label='Quantidade')
    price = forms.FloatField(label='Praço')
    total = forms.FloatField(label='Total')
    rentability = forms.ChoiceField(label='Rentabilidade')
