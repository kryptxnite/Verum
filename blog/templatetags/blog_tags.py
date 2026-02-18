from django import template
from blog.models import Category
from django.utils.safestring import mark_safe

import markdown

register = template.Library()


@register.simple_tag
def get_all_categories():
    return Category.objects.all()


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))