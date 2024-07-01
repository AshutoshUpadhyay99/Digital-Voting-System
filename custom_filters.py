from django import template

register = template.Library()

@register.filter
def get_date(value):
    return value.date()