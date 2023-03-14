from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True, default='')
    image = models.ImageField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    