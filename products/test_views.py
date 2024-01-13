from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product, Category, RelatedProduct


class ProductViewsTest(TestCase):
    def setUp(self):
        # Create a test superuser
        self.superuser = User.objects.create_superuser(
            username='superuser',
            email='superuser@example.com',
            password='superuserpassword'
        )

        # Create a test product
        self.product = Product.objects.create(
            name='Test Product',
            description='Test description',
            price=19.99,
        )

        # Create a test category
        self.category = Category.objects.create(name='Test Category')

        # Create a related product
        self.related_product = Product.objects.create(
            name='Related Product',
            description='Related description',
            price=50,
        )
        RelatedProduct.objects.create(
            from_product=self.product,
            to_product=self.related_product
        )

        # Log in the test superuser
        self.client.login(username='superuser', password='superuserpassword')

    def test_add_product_view(self):
        url = reverse('add_product')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_add_product_view_with_non_superuser(self):
        # Log out the superuser
        self.client.logout()

        # Log in a regular user
        self.client.login(
            username='regularuser', password='regularuserpassword'
        )

        url = reverse('add_product')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def tearDown(self):
        # Log out the test superuser
        self.client.logout()
