from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_page, name='posts_page'),
    path('', views.home,name='home'),
]