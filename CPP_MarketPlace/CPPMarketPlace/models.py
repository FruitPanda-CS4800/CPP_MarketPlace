from django.db import models
import os
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from PIL import Image
import tempfile

def product_image_path(instance, filename):
    """Return the upload path for product images."""
    return os.path.join('product_images', str(instance.id), filename)
# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, blank=True, null=True, default='')
    image = models.ImageField(blank=True, null=True, default='', upload_to=product_image_path)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
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
    