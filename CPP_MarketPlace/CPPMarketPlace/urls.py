from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home),
    path('helloWorld/', views.helloWorld),
    path('api/products/', views.product),
    path('addProduct/', views.addItem),
    path('products/', views.products),
    path('search/', views.search, name='search'),
    path('create_product/', views.create_product, name='create_product'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
