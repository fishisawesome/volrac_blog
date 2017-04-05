from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

from posts.models import Post

from ckeditor.fields import RichTextField

@python_2_unicode_compatible
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = RichTextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.message