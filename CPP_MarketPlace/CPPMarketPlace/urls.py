from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home),
    path('helloWorld/', views.helloWorld),
    path('api/products/', views.product),
    path('addProduct/', views.addItem),
    path('products/', views.products),
    path('search/', views.search, name='search')
]

urlpatterns += staticfiles_urlpatterns()
