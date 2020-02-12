from django import template

register = template.Library()

@register.simple_tag(name='define')
def define(value=None):
    return value