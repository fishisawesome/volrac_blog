from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm

def index(request):
    latest_posts = Post.objects.order_by('-pub_date')
    context = {}
    context['latest_posts'] = latest_posts
    return render(request, 'posts/index.html', context)

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = User.objects.get(pk=request.POST['user_id'])
            post.save()
            return HttpResponseRedirect(reverse('posts:index'))
        # args = {}
        # args['user'] = User.objects.get(pk=request.POST['user_id'])
        # args['title'] = request.POST['title']
        # args['content'] = request.POST['content']
        # args['pub_date'] = timezone.now()
        # post = Post(**args)
        # post.save()
    else:
        form = PostForm()
    
    return render(request, 'posts/new.html', {'form': form})


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {}
    context['post'] = post

    if request.user.is_authenticated():
        context['user'] = request.user

    return render(request, 'posts/detail.html', context)