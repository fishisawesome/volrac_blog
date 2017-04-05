from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Comment
from posts.models import Post
from django.contrib.auth.models import User

def add(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = get_object_or_404(User, pk=request.POST['user_id'])
    if request.method == 'POST':
        d = {}
        
        d['user'] = user
        d['post'] = post
        d['message'] = request.POST['message']
        
        c = Comment(**d)
        c.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))