# coding:utf-8
from __future__ import unicode_literals
from blog.models import User

from django.db import models

# Create your models here.


class Group(models.Model):
    # 群名
    name = models.CharField(max_length=32, verbose_name='群名')
    # 群成员，多对多。verbose_name描述
    member = models.ManyToManyField(User, verbose_name='群成员')

    class Meta:
        verbose_name = '群组'
        verbose_name_plural = '群组'
        # 按照ID排序，加负号从小到大,为元组或list类型
        ordering = ['id']

    def __unicode__(self):
        return self.name
    pass