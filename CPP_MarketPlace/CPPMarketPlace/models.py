from tkinter import TRUE
from django.db import models
import os
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from PIL import Image
import tempfile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def product_image_path(instance, filename):
    """Return the upload path for product images."""
    return os.path.join('product_images', str(instance.id), filename)

# Database table for products
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    condition = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to=product_image_path)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    @classmethod
    #python manage.py shell -c "from CPPMarketPlace.models import Product; Product.create_products(4)"
    #Create test products
    @classmethod
    def create_products(cls, num_products):
        for i in range(num_products):
            # Generate a temporary image file
            with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as f:
                img = Image.new('RGB', (200, 200), color='red')
                img.save(f, format='JPEG')
                f.seek(0)
                file = SimpleUploadedFile(f.name, f.read())

            # Create a new product with a unique name
            product_name = f'Product {timezone.now().strftime("%Y-%m-%d %H:%M:%S.%f")}'
            product = cls(name=product_name, category='Test Category',price=5, image=file)
            product.save()
            print(product.id)   

#Database table for User accounts
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30,default='default')
    last_name = models.CharField(max_length=30,default='default')
    profile_picture = models.ImageField(upload_to='profile_pictures', default='default/account.png', blank=True, null=True)
    about = models.TextField(max_length=2000, default="This user has not set their description.")
    date_joined = models.DateTimeField(null=True, blank=True)
    items_sold = models.IntegerField(default=0)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name, date_joined=instance.date_joined)