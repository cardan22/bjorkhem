from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'includes/main-nav.html')
        self.assertTemplateUsed(response, 'includes/mobile-nav.html')
        self.assertTemplateUsed(response, 'includes/newsletter.html')

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')

    def test_policy_view(self):
        response = self.client.get(reverse('policy'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/policy.html')
