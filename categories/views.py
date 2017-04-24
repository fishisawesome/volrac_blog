from django.shortcuts import get_object_or_404, render

from .models import Category

def category(request, slug):
    context = {}
    category = get_object_or_404(Category, slug=slug)
    context['category'] = category
    context['page_title'] = "Latest Posts for {}".format(category.title)
    context['page_heading'] = context['page_title']
    context['posts'] = category.post_set.order_by('-pub_date').all()
    return render(request, 'posts/index.html', context)
