# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-03 07:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u7fa4\u540d')),
                ('member', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='\u7fa4\u6210\u5458')),
            ],
            options={
                'verbose_name': '\u7fa4\u7ec4',
                'verbose_name_plural': '\u7fa4\u7ec4',
            },
        ),
    ]