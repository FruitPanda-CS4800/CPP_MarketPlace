from django.test import TestCase
from .models import Product

class ProductModelTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            condition='Test Condition',
            price=9.99,
            category='Test Category'
        )
    
    def test_product_creation(self):
        """Test that a product is created with the correct attributes"""
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.description, 'Test Description') # Added assertion
        self.assertEqual(self.product.condition, 'Test Condition') # Added assertion
        self.assertEqual(float(self.product.price), 9.99) # Added assertion
        self.assertEqual(self.product.category, 'Test Category')
        self.assertEqual(self.product.image.name, '')
        self.assertIsNotNone(self.product.created)


class ProductModelTestCase2(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Calculus II',
            description='Calculus II Description', # Added field
            condition='New', # Added field
            price=19.99, # Added field
            category='Textbooks'
        )
    
    def test_product_creation_correct(self):
        """Test that a product is created with the correct attributes"""
        self.assertEqual(self.product.name, 'Calculus II')
        self.assertEqual(self.product.description, 'Calculus II Description') # Added assertion
        self.assertEqual(self.product.condition, 'New') # Added assertion
        self.assertEqual(float(self.product.price), 19.99) # Added assertion
        self.assertEqual(self.product.category, 'Textbooks')
        self.assertEqual(self.product.image.name, '')
        self.assertIsNotNone(self.product.created)

    def test_product_creation_wrong(self):
        """Test that a product is created with the correct attributes"""
        self.assertNotEqual(self.product.name, 'Math') # Modified assertion
        self.assertNotEqual(self.product.category, 'Books') # Modified assertion
        self.assertEqual(self.product.image.name, '')
        self.assertIsNotNone(self.product.created)