from __future__ import unicode_literals

import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

from categories.models import Category

from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from PIL import Image

@python_2_unicode_compatible
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = AutoSlugField(null=True, default=None, unique=True,populate_from='title')
    content = RichTextField()
    image = models.ImageField(upload_to = 'posts/%Y/%m/%d/', blank=True, null=True, default=None)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    categories = models.ManyToManyField(Category)
    tags = TaggableManager()

    def save(self):
        super(Post, self).save()

        if self.image:
            img = Image.open(self.image)

            maxsize = (600, 600)
            img.thumbnail(maxsize, Image.ANTIALIAS)
            img.save(self.image.path)

    def published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.title