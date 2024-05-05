

# Create your models here.
from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = HTMLField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', through='PostCategory')
    status = models.CharField(max_length=20, choices=[('borrador', 'Borrador'), ('publicado', 'Publicado'), ('eliminado', 'Eliminado')], default='borrador')
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    comments_count = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    color = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class PostCategory(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

class Comment(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    likes_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"