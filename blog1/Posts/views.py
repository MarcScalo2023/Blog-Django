from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, "Posts/home.html", {'posts': posts})


def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, "Posts/post.html", {'post': post})
