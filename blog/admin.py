# coding:utf-8
from django.contrib.auth.admin import UserAdmin as BUserAdmin
from django.contrib import admin
from models import *

# Register your models here.


# 普通用户管理
class UserAdmins(BUserAdmin):
    list_display = ('username', 'nick')
    # 编辑用户中的设置
    fields = (
        ('基本内容', {'fields': ('username', 'password', 'nick', 'avatar', 'friend')}),
        ('权限', {'fields': ('is_superuser')})
    )
    # 增加用户中的设置
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'nick', 'avatar', 'friend', 'is_superuser'),
        })
    )
    pass

# 添加注册
admin.site.register(User, BUserAdmin)