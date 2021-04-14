from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .forms import OrderForm, ItemForm
from .models import Customer, Product, Item
from .services import *


@login_required(login_url="/login/")
def index(request):
    orders = list_orders()
    total = total_orders()
    revenues = revenues_orders()
    context = {'orders': orders, 'total': total, 'revenues': revenues}

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def create(request):
    if request.method == 'POST':
        form_order = OrderForm(request.POST)
        form_item = ItemForm(request.POST)
        if form_order.is_valid():
            customer = form_order.cleaned_data["customer"]
            customer_bd = Customer.objects.get(id=customer)
            new_order = Order.objects.create(customer=customer_bd)
            if form_item.is_valid():
                product = form_item.cleaned_data["product"]
                product_bd = Product.objects.get(id=product)
                quantity = form_item.cleaned_data["quantity"]
                price = form_item.cleaned_data["price"]
                total = form_item.cleaned_data["price"]
                Item.objects.create(order=new_order, product=product_bd, quantity=quantity, price=price, total=total,
                                    rentability='1')
        return redirect('home')
    else:
        form_order = OrderForm()
        form_item = ItemForm()
    return render(request, 'order.html', {'form_order': form_order, 'form_item': form_item})
