from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Post

def index(request):
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    context = {}
    context['latest_posts'] = latest_posts
    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {}
    context['post'] = post

    if request.user.is_authenticated():
        context['user'] = request.user

    return render(request, 'posts/detail.html', context)