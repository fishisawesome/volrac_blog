# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 00:25
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0009_auto_20170405_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
