from django.test import TestCase
from .models import Product

class ProductModelTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            category='Test Category'
        )
    
    def test_product_creation(self):
        """Test that a product is created with the correct attributes"""
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.category, 'Test Category')
        self.assertEqual(self.product.image.name, '')
        self.assertIsNotNone(self.product.created)
