from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product


class BagViewsTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a test product
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.0
        )

    def test_view_bag(self):
        # Login the user
        self.client.login(username='testuser', password='testpassword')

        # Access the view_bag URL
        response = self.client.get(reverse('view_bag'))

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag(self):
        # Login the user
        self.client.login(username='testuser', password='testpassword')

        # Add a product to the bag
        response = self.client.post(
            reverse('add_to_bag', args=[self.product.id]),
            {'quantity': 2, 'redirect_url': reverse('view_bag')}
        )

        # Check that the response is a redirect
        self.assertEqual(response.status_code, 302)

        # Check that the bag session has been updated
        self.assertEqual(self.client.session['bag'][str(self.product.id)], 2)

    def test_adjust_bag(self):
        # Login the user
        self.client.login(username='testuser', password='testpassword')

        # Add a product to the bag for testing adjust_bag
        response_add_to_bag = self.client.post(
            reverse('add_to_bag', args=[self.product.id]),
            {'quantity': 1, 'redirect_url': reverse('view_bag')}
        )

        # Check if the item is added to the bag successfully
        self.assertEqual(response_add_to_bag.status_code, 302)
        self.assertEqual(self.client.session['bag'][str(self.product.id)], 1)

        # Adjust the quantity of the product in the bag
        response_adjust_bag = self.client.post(
            reverse('adjust_bag', args=[self.product.id]),
            {'quantity': 3}
        )

        # Check that the response is a redirect
        self.assertEqual(response_adjust_bag.status_code, 302)

        # Check that the bag session has been updated
        self.assertEqual(self.client.session['bag'][str(self.product.id)], 3)
