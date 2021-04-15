from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
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
    if request.method == 'GET':
        form_order = OrderForm()
        form_item_factory = inlineformset_factory(Order, Item, form=ItemForm, extra=0, can_delete=True, min_num=1, validate_min=True)
        form_item = form_item_factory
        context = {
            'form_order': form_order,
            'form_item': form_item,
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
            return redirect('home')
        else:
            context = {
                'form_order': form_order,
                'form_item': form_item,
            }
        return render(request, 'order.html', context)
