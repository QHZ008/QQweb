# coding:utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# AbstractUser代替models.


# 增强类，扩展原有的user信息，基于AbstractUser，
class User(AbstractUser):
    # 昵称
    nick = models.CharField(max_length=32, verbose_name='昵称', blank=True)
    # 头像
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/avatar.jpg', verbose_name='头像')
    # 朋友
    friend = models.ManyToManyField('self', blank=True, null=True, verbose_name='朋友')

    class Meta:
        verbose_name = '聊天用户'
        verbose_name_plural = '聊天用户'
        ordering = ['id']

    def __unicode__(self):
        return self.username
    pass