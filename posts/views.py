from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Post

def index(request):
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    context = {}
    context['latest_posts'] = latest_posts
    return render(request, 'posts/index.html', context)

def new(request):
    if request.method == 'POST':
        args = {}
        args['user'] = User.objects.get(pk=request.POST['user_id'])
        args['title'] = request.POST['title']
        args['content'] = request.POST['content']
        args['pub_date'] = timezone.now()
        post = Post(**args)
        post.save()

        return HttpResponseRedirect(reverse('posts:index'))

    context = {}
    context['base'] = 'layout.html'
    return render(request, 'posts/new.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {}
    context['post'] = post

    if request.user.is_authenticated():
        context['user'] = request.user

    return render(request, 'posts/detail.html', context)