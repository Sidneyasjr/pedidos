from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .forms import OrderForm, ItemForm
from .models import Product
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
    products = list(Product.objects.all())
    if request.method == 'GET':
        form_order = OrderForm()
        form_item_factory = inlineformset_factory(Order, Item, form=ItemForm, extra=1)
        form_item = form_item_factory
        context = {
            'form_order': form_order,
            'form_item': form_item,
            'products': products
        }
        return render(request, "order.html", context)
    elif request.method == 'POST':
        form_order = OrderForm(request.POST)
        form_item_factory = inlineformset_factory(Order, Item, form=ItemForm)
        form_item = form_item_factory(request.POST)
        if form_order.is_valid() and form_item.is_valid():
            order = form_order.save()
            form_item.instance = order
            form_item.save()
            return redirect('edit', order.pk)
        else:
            context = {
                'form_order': form_order,
                'form_item': form_item,
            }
        return render(request, 'order.html', context)


def update(request, id):
    products = list(Product.objects.all())
    if request.method == 'GET':
        order_bd = list_oder(id)
        if order_bd is None:
            return redirect('home')
        form_order = OrderForm(instance=order_bd)
        form_item_factory = inlineformset_factory(Order, Item, form=ItemForm, extra=1)
        form_item = form_item_factory(instance=order_bd)
        context = {
            'form_order': form_order,
            'form_item': form_item,
            'products': products
        }
        return render(request, 'order.html', context)
    elif request.method == 'POST':
        order_bd = list_oder(id)
        if order_bd is None:
            return redirect('home')
        form_order = OrderForm(request.POST, instance=order_bd)
        form_item_factory = inlineformset_factory(Order, Item, form=ItemForm)
        form_item = form_item_factory(request.POST, instance=order_bd)
        if form_order.is_valid() and form_item.is_valid():
            order = form_order.save()
            form_item.instance = order
            form_item.save()
            return redirect('edit', order_bd.pk)
        else:
            context = {
                'form_order': form_order,
                'form_item': form_item,
            }
            return render(request, 'order.html', context)


def delete(request, id):
    order = list_oder(id)
    if request.method == 'POST':
        delete_order(order)
        return redirect('home')
    return render(request, 'confirm_delete.html', {'order': order})