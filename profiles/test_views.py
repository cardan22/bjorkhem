from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserProfile
from checkout.models import Order

class ProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_order_history_view(self):
        # Ensure the UserProfile for the user exists
        profile, created = UserProfile.objects.get_or_create(user=self.user)

        # Create an order for the user
        order = Order.objects.create(order_number='123', user_profile=profile)

        response = self.client.get(reverse('order_history', args=[order.order_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
