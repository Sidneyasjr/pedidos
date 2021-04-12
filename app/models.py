from django.db import models


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
    price = models.FloatField('price')
    multiple = models.PositiveIntegerField('multiplo')


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('quantidade', blank=True)
    total = models.FloatField(blank=True)

    class Meta:
        verbose_name_plural = 'pedidos'
        verbose_name = 'pedido'
        ordering = ('-id',)

    def __str__(self):
        return f'Pedido Nº.: {self.pk}'


class Item(models.Model):
    RENTABILITY_CHOICES = (
        (1, 'Great'),
        (2, 'Good'),
        (3, 'Bad')
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.PositiveIntegerField('produto')
    quantity = models.PositiveIntegerField('quantidade', default=1)
    price = models.FloatField('preço')
    total = models.FloatField()
    rentability = models.IntegerField(choices=RENTABILITY_CHOICES)

    class Meta:
        verbose_name_plural = 'itens'
        verbose_name = 'item'
        ordering = ('-id',)