

# Register your models here.
from django.contrib import admin
from .models import Category, Post, Comment, PostCategory
# Registra los modelos aquí
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostCategory)