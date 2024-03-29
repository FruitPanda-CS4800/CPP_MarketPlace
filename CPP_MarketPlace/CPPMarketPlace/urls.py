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
    path('products/', views.products, name='products'),
    path('products/<str:category_name>/', views.products_by_category, name='products_by_category'),
    path('search/', views.search, name='search'),
    path('create_product/', views.create_product, name='create_product'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('account_settings/', views.account_settings, name='account_settings'),
    path('account/<int:account_id>/', views.account_detail, name='account'),
    path('chat/', views.chat_page,name='test'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
