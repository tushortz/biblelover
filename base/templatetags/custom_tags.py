from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='split')
@stringfilter
def split(value, arg):
    return value.split(arg)


@register.filter(name='as_breadcrumbs')
@stringfilter
def as_breadcrumbs(values):
    values = values.replace("/", " ").strip().split(" ")

    url_dict = {"Home": "/"}
    url = ""

    for value in values:
        url += ("/" + value)
        url_dict[value.title().strip()] = url

    return url_dict
