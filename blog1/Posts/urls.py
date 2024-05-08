from django.urls import path
from . import views

urlpatterns = [
    path('', views.detalle_articulo, name='detalle_articulo'),
    path('post/<slug:slug>/', views.detalle_articulo, name='detalle_articulo'),
    path('categories/', views.categorias, name='categorias'),
    path('debug_urls/', views.debug_urls, name='debug_urls'),
]