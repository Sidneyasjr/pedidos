import locale

from django import template

register = template.Library()

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


@register.filter(name='format_monetary')
def format_monetary(value):
    if value is None:
        return 'R$ 0,00'
    return locale.currency(value, grouping=True)


@register.filter(name='format_date')
def format_date(date):
    return date.strftime('%d/%m/%Y')