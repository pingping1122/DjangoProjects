from django.contrib import admin

# Register your models here.

# 需要注册到admin里才能在admin后台看到

from .models import Article

admin.site.register(Article)
