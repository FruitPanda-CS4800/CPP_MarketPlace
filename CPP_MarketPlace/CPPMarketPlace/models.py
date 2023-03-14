from django.db import models
import os

def product_image_path(instance, filename):
    """Return the upload path for product images."""
    return os.path.join('product_images', str(instance.id), filename)
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True, default='')
    image = models.ImageField(blank=True, default='', upload_to=product_image_path)
    created = models.DateTimeField(auto_now_add=True)
    