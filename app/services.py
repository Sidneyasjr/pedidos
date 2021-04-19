from .models import Order, Item


def list_orders():
    orders = Order.objects.all()
    return orders


def count_orders():
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


def total_order(id):
    items = Item.objects.filter(order=id)
    for item in items:
        price = item.price
        quantity = item.quantity
        total = quantity * price
        return total


def quantity_order(id):
    return Item.objects.filter(order=id).count()


def list_oder(id):
    order = Order.objects.filter(id=id).first()
    return order


def delete_order(order):
    order.delete()
