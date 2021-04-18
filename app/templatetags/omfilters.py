import locale

from django import template

register = template.Library()

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')


@register.filter(name='format_monetary')
def format_monetary(value):
    if value is None:
        return 'R$ 0,00'
    return locale.currency(value, grouping=True)
