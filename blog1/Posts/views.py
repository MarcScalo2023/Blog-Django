from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.template.loader import get_template
from django.template import Context
from django.contrib import messages
from.models import Post, Category
from.forms import CommentForm
from django.db import models
from django.urls import get_urlconf, resolve

def detalle_articulo(request, slug):
    articulo = get_object_or_404(Post, slug=slug, status='publicado')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.post = articulo
            form.save()
            messages.success(request, 'Comentario agregado con éxito')
            return redirect('detalle_articulo', slug=slug)
    else:
        form = CommentForm()
    
    return render(request, 'detalle_articulo.html', {'articulo': articulo, 'form': form})

def categorias(request):
    categorias = Category.objects.all()
    return render(request, 'categorias.html', {'categorias': categorias})

def debug_urls(request):
    try:
        urlconf = get_urlconf()
        resolver = resolve('/', urlconf=urlconf)
        url_tree = resolver.urlconf.url_patterns
        output = []
        for entry in url_tree:
            output.append(str(entry.pattern))
        return HttpResponse('\n'.join(output))
    except Exception as e:
        return HttpResponse('Error: {}'.format(e))
    


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    mensaje = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre