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


class ProductModelTestCase2(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Calculus II',
            category='Textbooks'
        )
    
    def test_product_creationCorrect(self):
        """Test that a product is created with the correct attributes"""
        self.assertEqual(self.product.name, 'Calculus II')
        self.assertEqual(self.product.category, 'Textbooks')
        self.assertEqual(self.product.image.name, '')
        self.assertIsNotNone(self.product.created)

    def test_product_creationWrong(self):
        """Test that a product is created with the correct attributes"""
        self.assertEqual(self.product.name, 'Math')
        self.assertEqual(self.product.category, 'Books')
        self.assertEqual(self.product.image.name, '')
        self.assertIsNotNone(self.product.created)

