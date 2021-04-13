from .models import Order
from django.db.models import Sum


def list_orders():
    orders = Order.objects.all()
    return orders


def total_orders():
    total = Order.objects.count()
    return total


def revenues_orders():
    revenues = Order.objects.aggregate(Sum('total'))
    return revenues['total__sum']

