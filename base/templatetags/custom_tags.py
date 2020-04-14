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
    values = values.strip("/").replace("/", "|").split("|")

    url_dict = {}
    url = ""

    for value in values:
        if value:
            url += ("/" + value)
            title = value.title().strip().replace("_", " ")
            url_dict[title] = url

    return url_dict
