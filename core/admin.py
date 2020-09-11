from django.contrib import admin

# Register your models here.

from .models import Post, Article

admin.site.register(Post)
admin.site.register(Article)