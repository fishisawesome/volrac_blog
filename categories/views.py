from django.shortcuts import get_object_or_404, render

from .models import Category

def category(request, slug):
    context = {}
    category = get_object_or_404(Category, slug=slug)
    context['category'] = category
    context['posts'] = category.post_set.all()
    return render(request, 'categories/detail.html', context)
