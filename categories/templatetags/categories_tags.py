from django import template

from categories.models import Category

register = template.Library() 

@register.assignment_tag
def get_used_categories():
    return Category.objects.filter(post__isnull=False).order_by('title').distinct()

@register.assignment_tag
def get_categories():
    return Category.objects.order_by('title').all()