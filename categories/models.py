from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

from autoslug import AutoSlugField

@python_2_unicode_compatible
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='title')

    def __str__(self):
        return self.title