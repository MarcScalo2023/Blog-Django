from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Posts/posts_page.html')


def posts_page(request):
    posts = Post.objects.all()
    return render(request, 'Posts/posts_page.html', {'posts': posts})