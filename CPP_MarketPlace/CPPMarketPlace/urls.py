from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('helloWorld/', views.helloWorld),
    path('api/products/', views.product),
    path('addProduct/', views.addItem),
    path('products/', views.products),
    path('search/', views.search, name='search')
]
