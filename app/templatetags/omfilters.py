from django import template

from utils import utils

register = template.Library()


@register.filter
def format_price(val):
    return utils.format_price(val)


@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})