from django.db import models

from utils import utils


class Customer(models.Model):
    name = models.CharField('nome', max_length=100)

    class Meta:
        verbose_name_plural = 'clientes'
        verbose_name = 'cliente'
        ordering = ('id',)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('nome', max_length=100)
    price = models.DecimalField('preço', max_digits=15, decimal_places=2)
    multiple = models.PositiveIntegerField('multiplo', default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'produtos'
        verbose_name = 'produto'
        ordering = ('id',)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField('date', null=True, blank=True, auto_now_add=True)
    quantity = models.PositiveIntegerField('quantidade', null=True, blank=True)
    total = models.FloatField(null=True, blank=True)

    def get_total_format(self):
        return utils.format_price(self.total)

    get_total_format.short_description = 'Total'

    class Meta:
        verbose_name_plural = 'pedidos'
        verbose_name = 'pedido'
        ordering = ('-id',)

    def __str__(self):
        return f'Pedido: {self.pk}'


class Item(models.Model):
    RENTABILITY_CHOICES = (
        (1, 'Ótima'),
        (2, 'Boa'),
        (3, 'Ruim')
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('quantidade', null=False, blank=False)
    price = models.DecimalField('preço', max_digits=15, decimal_places=2, null=False, blank=False)
    total = models.DecimalField(max_digits=15, decimal_places=2, null=False, blank=False)
    rentability = models.IntegerField(choices=RENTABILITY_CHOICES, null=False, blank=False, default=2)

    class Meta:
        verbose_name_plural = 'itens'
        verbose_name = 'item'
        ordering = ('-id',)

    def __str__(self):
        return f'Item: {self.pk} - {self.order}'
