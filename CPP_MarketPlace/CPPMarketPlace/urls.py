from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('helloWorld/', views.helloWorld),
]
