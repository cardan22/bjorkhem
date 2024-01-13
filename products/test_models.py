from django.test import TestCase
from .models import Category, Product, RelatedProduct


class SimpleProductModelTest(TestCase):
    def setUp(self):
        # Create a test category
        self.category = Category.objects.create(name='Test Category')

        # Create a test product
        self.product = Product.objects.create(
            name='Test Product',
            category=self.category,
            description='This is a test product.',
            image_alt='Test Image Alt Text',
            price=50
        )

        # Create another test product
        self.related_product = Product.objects.create(
            name='Related Test Product',
            category=self.category,
            description='This is a related test product.',
            image_alt='Related Test Image Alt Text',
            price=40
        )

        # Create a related product entry
        self.related_entry = RelatedProduct.objects.create(
            from_product=self.product,
            to_product=self.related_product
        )

    def test_product_str_method(self):
        self.assertEqual(str(self.product), 'Test Product')

    def test_related_product_str_method(self):
        self.assertEqual(
            str(self.related_entry),
            'Test Product -> Related Test Product'
        )

    def test_related_products_field(self):
        related_products = self.product.related_products.all()
        self.assertEqual(len(related_products), 1)
        self.assertEqual(related_products[0], self.related_product)

    def tearDown(self):
        self.category.delete()
        self.product.delete()
        self.related_product.delete()
        self.related_entry.delete()
