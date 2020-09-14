from django.contrib import admin

# Register your models here.

from .models import Post, Article, Club

admin.site.register(Post)
admin.site.register(Article)
admin.site.register(Club)