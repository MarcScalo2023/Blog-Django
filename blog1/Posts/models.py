from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify

class Category(models.Model):
    COLOR_CHOICES = (
        ('red', 'Rojo'),
        ('blue', 'Azul'),
        ('green', 'Verde'),
        ('yellow', 'Amarillo'),
        ('orange', 'Naranja'),
        ('purple', 'Morado'),
        ('pink', 'Rosado'),
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
        ('eliminado', 'Eliminado')
    )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = HTMLField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='borrador')
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    comments_count = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    likes_count = models.IntegerField(default=0)
    def __str__(self):
        return f"Comentario de {self.author} en {self.post.title}"

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.post.title} - {self.category.name}"  