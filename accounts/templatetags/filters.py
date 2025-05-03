from django import template

register = template.Library()

@register.filter
def first_name(value):
    if not value:
        return ''
    return value.strip().split(' ')[0].capitalize()