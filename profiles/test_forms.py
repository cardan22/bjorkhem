from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserProfileForm
from .models import UserProfile, GDPRConsent


class UserProfileFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_user_profile_form(self):
        form_data = {
            'default_full_name': 'John Doe',
            'default_phone_number': '123456789',
            'default_address1': '123 Main St',
            'default_address2': 'Apt 45',
            'default_postcode': '12345',
            'default_city': 'Cityville',
            'gdpr_consent': True,
        }

        form = UserProfileForm(data=form_data, instance=self.user.userprofile)

        self.assertTrue(form.is_valid())

        form.save()

        user_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(user_profile.default_full_name, 'John Doe')
        self.assertEqual(user_profile.default_phone_number, '123456789')
        self.assertEqual(user_profile.default_address1, '123 Main St')
        self.assertEqual(user_profile.default_address2, 'Apt 45')
        self.assertEqual(user_profile.default_postcode, '12345')
        self.assertEqual(user_profile.default_city, 'Cityville')

        gdpr_consent = GDPRConsent.objects.get(user_profile=user_profile)
        self.assertTrue(gdpr_consent.gdpr_consent)
