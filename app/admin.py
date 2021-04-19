from django.contrib import admin

from .models import Order, Customer, Product, Item


# Register your models here.


class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Customer, CustomerModelAdmin)


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'multiple')
    search_fields = ('name',)


admin.site.register(Product, ProductModelAdmin)


class ItemOrderInline(admin.TabularInline):
    model = Item
    extra = 1


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date')
    search_fields = ('id',)
    inlines = [ItemOrderInline]


admin.site.register(Order, OrderModelAdmin)
admin.site.register(Item)