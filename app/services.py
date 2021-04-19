from .models import Order, Item


def list_orders():
    orders = Order.objects.all()
    return orders


def total_orders():
    total = Order.objects.count()
    return total


def revenues_orders():
    items = Item.objects.all()
    revenues = []
    for item in items:
        price = item.price
        quantity = item.quantity
        total = quantity * price
        revenues.append(total)
    return sum(revenues)


def total_order(order):
    items = Item.objects.filter(order=order)
    for item in items:
        price = item.price
        quantity = item.quantity
        total = quantity * price
        return total


def list_oder(id):
    order = Order.objects.filter(id=id).first()
    return order


def delete_order(order):
    order.delete()
