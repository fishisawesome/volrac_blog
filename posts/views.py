from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Post
from categories.models import Category
from .forms import PostForm

def index(request):
    latest_posts = Post.objects.order_by('-pub_date')
    context = {}
    context['posts'] = latest_posts
    return render(request, 'posts/index.html', context)

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            
            post.user = User.objects.get(pk=request.POST['user_id'])
            post.save()

            categories = request.POST.getlist('categories')
            for category_id in categories:
                category = Category.objects.filter(pk=category_id).get()
                post.categories.add(category)

            post.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('posts:index'))
    
    return render(request, 'posts/new.html')


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {}
    context['post'] = post

    if request.user.is_authenticated():
        context['user'] = request.user

    return render(request, 'posts/detail.html', context)

def tag(request, tag):
    context = {}
    context['category'] = tag
    context['page_title'] = "Latest Posts for {}".format(tag)
    context['page_heading'] = context['page_title']
    context['posts'] = Post.objects.filter(tags__slug=tag).order_by('-pub_date').all()
    return render(request, 'posts/index.html', context)