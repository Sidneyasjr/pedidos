from django.db.models import Sum

from .models import Order, Item


def list_orders():
    orders = Order.objects.all()
    return orders


def total_orders():
    total = Order.objects.count()
    return total


def revenues_orders():
    revenues = Order.objects.aggregate(Sum('total'))
    return revenues['total__sum']


def detail_oder(id):
    order = Order.objects.filter(id=id).first()
    return order
