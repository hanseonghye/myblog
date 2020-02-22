from django import template

register = template.Library()


@register.simple_tag(name='define')
def define(value=None):
    return value


@register.simple_tag(name='define2')
def define2(value=None):
    if value:
        return f"({value})"
    else:
        return ""
